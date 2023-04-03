from dataclasses import dataclass


@dataclass
class Function:
    numb_line: int
    name_function: str
    value_function: str
    variable_function: dict  # ключ - имя переменной, значение - тип переменной

    # функции, выводящие значения для конкретной функции
    def out_name_func(self) -> str:
        return self.name_function

    def out_numb_line(self) -> int:
        return self.numb_line

    def out_value_func(self) -> str:
        return self.value_function

    def out_variable(self) -> dict:
        return self.variable_function


@dataclass
class Define:
    name_define: str = ''


@dataclass
class Typedef:
    name_typedef: str = ''


class ParsFunction:

    # функции, достающие из строки нужные элементы (имя функции, возвращаемый тип и т.д.)
    def ent_line(self, funct_line: str) -> int:
        ...
        return 0

    def ent_name(self, funct_line: str) -> str:
        ...
        return ''

    def ent_value(self, funct_line: str) -> str:
        ...
        return ''

    def ent_variable(self, funct_line: str) -> str:
        ...
        return ''

    # проверка, подходит ли данная строчка для разбиения
    def line_function(self) -> bool:
        ...
        return True

    # метод, по результату проверки раскидывающий аргументы из строчки
    # на вход значение проверки, сама строчкА, номер этой строки
    # возвращает собранный экземпляр (не уверена в данном методе)
    def line_parse(self, exam: bool, line: str, num: int):
        ...
        return Function