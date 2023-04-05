from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def deserialize(cls, stream: Stream):
        pass

# class Deserializer:
#
#     def deserialize(self, stream) -> Any:
#         if ...:
#             concreate_deserializer = PointDeserializer()
#         elif ...:
#             pass
#         return concreate_deserializer.deserialize(stream)
#
#
# class PointDeserializer:
#
#     def deserialize(self, stream) -> Point:
#         pass
