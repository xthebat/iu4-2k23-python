import dataclasses
from dataclasses import dataclass
from typing import Self

from stream07.streams import DataBinaryIO


class Serializable:

    @classmethod
    def deserialize(cls, stream: DataBinaryIO) -> Self:
        raise NotImplementedError


class Integer(int, Serializable):
    __size__: int
    __signed__: bool

    @classmethod
    def deserialize(cls, stream: DataBinaryIO):
        return stream.read_uint(cls.__size__, cls.__signed__)


class Int8(Integer):
    __size__ = 1
    __signed__ = True


class Int16(Integer):
    __size__ = 2
    __signed__ = True


class Int32(Integer):
    __size__ = 4
    __signed__ = True


class UInt8(Integer):
    __size__ = 1
    __signed__ = False


class UInt16(Integer):
    __size__ = 2
    __signed__ = False


class UInt32(Integer):
    __size__ = 4
    __signed__ = False


class AsciiString(str, Serializable):
    @classmethod
    def deserialize(cls, stream: DataBinaryIO):
        return stream.read_string()


@dataclass
class Struct(Serializable):

    @classmethod
    def new(cls, **kwargs) -> Self:
        kwargs = {field.name: field.type(kwargs[field.name]) for field in dataclasses.fields(cls)}
        # noinspection PyArgumentList
        return cls(**kwargs)

    @classmethod
    def deserialize(cls, stream: DataBinaryIO):
        def _deserialize_field(field: dataclasses.Field):
            assert issubclass(field.type, Serializable), f"Fields must be inherited from Serializable"
            value = field.type.deserialize(stream)
            print(f"{field.type} = {value}")
            return value

        assert dataclasses.is_dataclass(cls), f"Can only deserialize dataclasses, got {cls}"
        kwargs = {field.name: _deserialize_field(field) for field in dataclasses.fields(cls)}
        return cls.new(**kwargs)
