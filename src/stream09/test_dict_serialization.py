import json
from dataclasses import dataclass, asdict

from stream07.serialization import AsciiString, Int32, Struct
from stream07.streams import DataBinaryIO


def test_point_json():
    @dataclass
    class Point:
        x: int
        y: int

    # serialize
    expected = Point(1, 2)
    d0 = asdict(expected)
    text = json.dumps(d0)

    # deserialize
    d1 = json.loads(text)
    actual = Point(**d1)

    assert actual == expected


def test_point_binary():
    @dataclass
    class Point(Struct):
        name: AsciiString
        x: Int32
        y: Int32

    @dataclass
    class Rectangle(Struct):
        name: AsciiString
        lb: Point
        rt: Point

    stream = DataBinaryIO.from_bytes(
        b"ThisIsARectangle\x00"
        b"LeftBottom\x00\x13\x37\x00\x00\xDE\xAD\x00\x00"
        b"RightTop\x00\x01\x00\x00\x00\x02\x00\x00\x00"
        b"END-OF-PYTHON"
    )

    actual = Rectangle.deserialize(stream)

    end_value = stream.read(3)
    assert end_value == b"END"

    expected = Rectangle.new(
        name="ThisIsARectangle",
        lb=Point.new(name="LeftBottom", x=14099, y=44510),
        rt=Point.new(name="RightTop", x=1, y=2),
    )

    assert actual == expected
