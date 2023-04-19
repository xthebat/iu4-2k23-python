import json
from dataclasses import dataclass, asdict
from typing import Callable, Iterable






class ServerClient:

    def __init__(self):
        self._connected = False
        ...


    def connect(self):
        pass

    def send_request(self):
        pass

    def ...




@dataclass(frozen=True)
class Define:
    """
    Экземпляры: найденные define

    #define BUF_SIZE 128
    """

    line_no: int
    """Номер строки"""

    name: str
    """Имя дефайна"""

    value: str
    """Значение дефайна"""

    @staticmethod
    def from_line(line_no: int, line: str) -> "Define":
        token = line.strip().split(" ", maxsplit=2)
        assert token[0] == "#define"
        return Define(line_no, token[1], token[2])

    def find_element(self) -> str:
        return self.__search(...)

    def __search(self, ident: int) -> list[str]:
        pass

    def _protected_search(self, ident: int) -> list[str]:
        pass


@dataclass(frozen=True)
class MyFunction:
    name: str


@dataclass(frozen=True)
class AllElements:
    """Общий класс для хранения списков классов."""

    functions: tuple[MyFunction] = tuple()

    @staticmethod
    def from_line(text: str):
        ...
        functions = tuple()
        return AllElements(functions)

    # def __post_init__(self):
    #     self.function_list = []
    #     self.define_list = []
    #     self.typedef_list = []

    # def create_list(self):
    #     self.function_list = []
    #     self.define_list = []
    #     self.typedef_list = []

    # # функции добавления нового элемента в списки по классам
    # def add_function(self, func: Function):
    #     self.function_list.append(func)


class Something:

    def __init__(self):
        pass

    def print_define(self, filename: str) -> list:
        define_list = Define.__Define_find_element(self, filename)


class Function:
    # name: str
    # return_type: int

    C_STYLE = "test"

    def __init__(self, name: str, return_type: str, args: dict) -> None:
        self.name = name
        self.return_type = return_type
        self.args = args


def find(iterable: Iterable, predicate: Callable):
    return next((it for it in iterable if predicate(it)), None)


def test_func():
    for data_type in data_types:
        if it := find(modifiers, lambda i: line.startswith(i + data_type + space)):
            return it + data_type + space


class Analyzer:
    def __init__(self, text: str):
        self._file_str = filestr
        self._analyzed_data = None


def main():
    define = Define(102, "BUF_SIZE", "128")
    print(define)

    d = asdict(define)
    print(d)

    defines = [
        Define(102, "BUF_SIZE", "128"),
        Define(102, "BUF_SIZE", "128"),
        Define(102, "BUF_SIZE", "128")
    ]

    json.dumps(map(asdict, defines))

    # # define.name = "fdsfa"
    #
    # d = dict()
    # d[define] = 102

    f0 = Function("x", "str", {})

    print(f"{f0.name=}")
    f1 = Function("y", "str", {})
    print(f"{f1.name=}")
    print(f"{f0.name=}")
    f0.name = "fdsasd"
    print(f"{f1.name=}")

    print(f0.C_STYLE)
    print(f1.C_STYLE)
    print(Function.C_STYLE)

    # print(d[define])

    # all_elements = AllElements()
    # # all_elements.create_list()
    # all_elements.add_function()
    #
    # element = define.find_element()
    # Define.find_element(define)
    #
    # define._protected_search()


if __name__ == '__main__':
    main()
