from io import BytesIO
from typing import Self, Literal, Callable, Generic, TypeVar, TypeAlias


class Readable:

    def read(self, n: int) -> bytes:
        raise NotImplementedError


class FilteredBinaryIO(Readable):

    @classmethod
    def from_bytes(cls, data: bytes, **kwargs) -> Self:
        return cls(BytesIO(data), **kwargs)

    def __init__(self, stream, **kwargs):
        self._stream = stream

    def read(self, n: int):
        return self._stream.read(n)


class CountingBinaryIO(FilteredBinaryIO):

    def __init__(self, stream, **kwargs):
        super().__init__(stream, **kwargs)
        self.count = 0

    def read(self, n: int):
        self.count += n
        return super().read(n)


T = TypeVar("T")
Reduce: TypeAlias = Callable[[T, bytes], T]


class ReduceBinaryIO(FilteredBinaryIO, Generic[T]):

    def __init__(self, stream, reduce: Reduce, init: T, **kwargs):
        super().__init__(stream, **kwargs)
        self._reduce = reduce
        self._result = init

    def read(self, n: int):
        data = super().read(n)
        self._result = self._reduce(self._result, data)
        return data

    @property
    def result(self) -> T:
        return self._result


class DataBinaryIO(FilteredBinaryIO):

    def __init__(self, stream, byteorder: Literal["little", "big"] = "little"):
        super().__init__(stream)
        self._byteorder = byteorder

    def read_uint(self, size: int, signed: bool = False):
        return int.from_bytes(self.read(size), byteorder=self._byteorder, signed=signed)

    def read_int8(self) -> int:
        return self.read_uint(1, True)

    def read_int16(self) -> int:
        return self.read_uint(2, True)

    def read_int32(self) -> int:
        return self.read_uint(4, True)

    def read_uint8(self) -> int:
        return self.read_uint(1)

    def read_uint16(self) -> int:
        return self.read_uint(2)

    def read_uint32(self) -> int:
        return self.read_uint(4)

    def read_string(self, term: int = 0) -> str:
        buffer = []
        value = self.read_uint8()
        while value != term:
            buffer += chr(value)
            value = self.read_uint8()
        return "".join(buffer)
