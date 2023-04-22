import dataclasses
from dataclasses import dataclass
from typing import Self

from stream07.streams import DataBinaryIO


class Serializable:

    @classmethod
    def deserialize(cls, stream: DataBinaryIO) -> Self:
        raise NotImplementedError


class Integer(int, Serializable):
    """Class adds deserialize method to default int class"""

    __size__: int
    __signed__: bool

    @classmethod
    def deserialize(cls, stream: DataBinaryIO):
        return cls(stream.read_uint(cls.__size__, cls.__signed__))


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
    """Class adds deserialize method to default str class"""

    @classmethod
    def deserialize(cls, stream: DataBinaryIO):
        return cls(stream.read_string())


@dataclass
class Struct(Serializable):
    """Class adds deserialize method to dataclass from fields definition"""

    def __init_subclass__(cls, **kwargs):
        # Make class subclass validation
        assert dataclasses.is_dataclass(cls), f"Class should be marked as dataclass to be Serializable, got {cls}"
        invalids = [field.name for field in dataclasses.fields(cls) if not issubclass(field.type, Serializable)]
        assert not invalids, \
            f"All class fields must be inherited from Serializable, fields not serializable: {invalids}"
        super().__init_subclass__(**kwargs)

    @classmethod
    def deserialize(cls, stream: DataBinaryIO):
        kwargs = {field.name: field.type.deserialize(stream) for field in dataclasses.fields(cls)}
        # noinspection PyArgumentList
        return cls(**kwargs)
