from dataclasses import dataclass


class Dummy:
    pass


dummy = Dummy()


class ParameterlessClass:

    def __init__(self):
        self.state = None


parameterless = ParameterlessClass()


class Normalizable:

    def norm(self) -> int:
        raise NotImplementedError


class Point(Normalizable):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def norm(self):
        return self.x ** 2 + self.y ** 2


class Vector(Normalizable):

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def norm(self) -> int:
        return self.end.norm() ** 2 + self.start.norm() ** 2


@dataclass(unsafe_hash=True, frozen=True)
class PointDataclass(Normalizable):
    x: int = 0
    y: int = 0

    def norm(self):
        return self.x ** 2 + self.y ** 2


def main():
    point = Point(10, 20)
    vector = Vector(Point(10, 20), Point(20, 30))
    norm_list: list[Normalizable] = [point, vector]
    length = sum(it.norm() for it in norm_list)


if __name__ == '__main__':
    main()
