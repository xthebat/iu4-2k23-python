import zlib

from stream07.streams import DataBinaryIO, ReduceBinaryIO


def test_serializer():
    input_data = b"\xDE\xAD\xBE\xEFMy test string\x00\xFE\xAD"

    stream = DataBinaryIO.from_bytes(input_data)
    assert stream.read_uint32() == 0xEFBEADDE
    assert stream.read_string() == "My test string"
    assert stream.read_uint16() == 0xADFE

    counting = ReduceBinaryIO.from_bytes(
        input_data,
        reduce=lambda length, data: length + len(data),
        init=0)

    crc32 = ReduceBinaryIO.from_bytes(
        input_data,
        reduce=lambda crc, data: zlib.crc32(data, crc),
        init=0
    )

    stream = DataBinaryIO(crc32, byteorder="big")
    assert stream.read_uint32() == 0xDEADBEEF
    assert stream.read_string() == "My test string"
    assert stream.read_uint16() == 0xFEAD

    assert crc32.result == zlib.crc32(input_data)

    # assert counting.result == len(input_data)
