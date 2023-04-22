import dataclasses
from abc import ABC
from dataclasses import dataclass
from typing import Generic, Callable, Any

from bonus.common import safe_issubclass, get, getitem2args
from bonus.types import Int8, Int16, Int32, UInt8, UInt16, UInt32, T
from stream07.streams import DataBinaryIO


class SerializerInterface(Generic[T]):

    def deserialize(self, cls: type[T], stream: DataBinaryIO) -> T:
        """
        Function deserialize class `cls` from binary `stream` to object.

        :param cls: Target deserialization class.
        :param stream: Stream to read object from.
        :return: Deserialized object.
        """
        raise NotImplementedError


class AbstractSerializer(SerializerInterface[T], ABC):
    """Abstract serializer for generic class T"""

    def __init__(self, context: SerializerInterface):
        self._context = context
        """top level serializer context"""


ConditionPredicate = Callable[[Any], bool]


class BasicSerializer(SerializerInterface[T]):
    """Top level basic serializer for any registered class"""

    def __init__(self):
        self._serializers = dict[ConditionPredicate, type[AbstractSerializer]]()
        """Registered Serializers"""

        self._cache = dict[Any, AbstractSerializer]()
        """Class to Serializers factory cache"""

    def register(self, condition: ConditionPredicate, factory: type[AbstractSerializer] = None):
        """
        Function registers new deserializer by `condition`, i.e. if `condition` met during deserialization then
        deserializer made by specified `factory` will be used for class deserialization. Also found classes cached
        into internal dictionary.

        :param condition: Condition to use specified deserializer made by `factory`
        :param factory: Factory to make deserializer
        :return: Registrator to use as decorator or nothing
        """

        # If class not specified - use it as decorator
        if factory is None:
            def registrator(_factory: type[AbstractSerializer]):
                # Call this function itself but as direct registration (else branch)
                self.register(condition, _factory)

            return registrator

        # otherwise direct call of registration
        else:
            # TODO: Check on already registered serializer ... somehow
            self._serializers[condition] = factory

    def deserialize(self, cls: type[T], stream: DataBinaryIO) -> T:
        # TODO: Check we have serializer
        if s := self._cache.get(cls):
            return s.deserialize(cls, stream)

        factory = get(factory for condition, factory in self._serializers.items() if condition(cls))
        assert factory, f"Serializer for {cls} not found"

        return self._cache \
            .setdefault(cls, factory(self)) \
            .deserialize(cls, stream)


serializer = BasicSerializer()
"""Instance for basic serializer, if required other serializer can be made"""


class IntSerializer(AbstractSerializer[int]):
    __size__: int
    __signed__: bool

    @getitem2args
    def __class_getitem__(cls, bits: int, signed: bool):
        prefix = "U" if signed else ""
        return type(f"{prefix}Int{bits}Serializer", (cls,), dict(__size__=bits // 8, __signed__=signed))

    def deserialize(self, context, stream: DataBinaryIO) -> T:
        return stream.read_uint(self.__size__, self.__signed__)


serializer.register(lambda it: it == Int8, IntSerializer[8, True])
serializer.register(lambda it: it == Int16, IntSerializer[16, True])
serializer.register(lambda it: it == Int32, IntSerializer[32, True])
serializer.register(lambda it: it == UInt8, IntSerializer[8, False])
serializer.register(lambda it: it == UInt16, IntSerializer[16, False])
serializer.register(lambda it: it == UInt32, IntSerializer[32, False])


@serializer.register(lambda it: safe_issubclass(it, str))
class AsciiStringSerializer(AbstractSerializer[str]):
    def deserialize(self, context, stream: DataBinaryIO) -> str:
        return stream.read_string()


@serializer.register(lambda it: dataclasses.is_dataclass(it))
class StructSerializer(AbstractSerializer[dataclass]):
    def deserialize(self, cls: type[dataclass], stream: DataBinaryIO) -> dataclass:
        kwargs = {
            field.name: self._context.deserialize(field.type, stream)
            for field in dataclasses.fields(cls)
        }
        # noinspection PyArgumentList
        return cls(**kwargs)
