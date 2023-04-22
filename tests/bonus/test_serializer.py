from dataclasses import dataclass

from bonus.serialization import serializer, Int32, UInt16
from stream07.streams import DataBinaryIO


def test_serializer():
    @dataclass
    class Point:
        name: str
        x: Int32
        y: Int32

    @dataclass
    class Rectangle:
        name: str
        ident: UInt16
        lb: Point
        rt: Point

    stream = DataBinaryIO.from_bytes(
        b"ThisIsARectangle\x00"
        b"\x22\x03"
        b"LeftBottom\x00\x13\x37\x00\x00\xDE\xAD\x00\x00"
        b"RightTop\x00\x01\x00\x00\x00\x02\x00\x00\x00"
        b"END-OF-PYTHON"
    )

    actual = serializer.deserialize(Rectangle, stream)

    end_value = stream.read(3)
    assert end_value == b"END"

    expected = Rectangle(
        "ThisIsARectangle",
        0x322,
        Point("LeftBottom", 14099, 44510),
        Point("RightTop", 1, 2),
    )
    
    print(actual)

    assert actual == expected
