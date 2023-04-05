# Файл выполняет разбор входного файлика
# Модуль выполняет Александр Шишурин git: 4i4urin
from dataclasses import dataclass

from parse_types import ParseObject, ParceTypedef, ParceFunc, ParseDefine


# Notes
# На вход парсера поступает список строк, каждая строка имеет свой номер как во входнмом файле
# пустые строки -- NONE
# парсер заполняет список объектов

@dataclass
class Parser:
    # read input string fill private list of objects for parse
    def parse_string(self, string_list: list[str]):
        pass

    def get_object_list(self) -> list[ParseObject]:
        pass

    def __take_typedef(self) -> ParceTypedef:
        pass

    def __take_func(self) -> ParceFunc:
        pass

    def __take_define(self) -> ParseDefine:
        pass

    __parse_obj_list: list[ParseObject]

    __ctypes_set = {"auto", "char", "const", "double", "enum", "extern", "float", "inline", "int", "long", "register",
                    "short", "signed", "static", "struct", "union", "unsigned", "void", "volatile"}

    __parce_keywords = {"#define", "typedef", ";"}
