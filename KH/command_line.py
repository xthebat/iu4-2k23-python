from c_header_view import *

class CommandLine_output:
    def __init__(self):
        """Constructor"""
        pass

    # вывод всех функций
    def output_functions(self, functions: list[ParsedFunction]):
        ...

    # вывод всех директив
    def output_directives(self, defines: list[ParsedDefine]):
        ...

    # вывод локальных переменных, объявленных внутри inline-функций
    def output_InlineVariables(self, variables: list[ParsedInlineVariable]):
        ...

    # вывод всех объявлений типов
    def output_types(self, types: list[ParsedTypeDef]):
        ...

    # вывод всех структур
    def output_structeres(self, bonus: list[ParsedStruct]):
        ...


class CommandLine_input:
    def __init__(self):
        """Constructor"""
        pass

    # функция для обработки входного файла, возвращает тип входного файла и путь к файлу
    def input_file(self, file: str) -> tuple(int, str):
        ...

    # функция для обработки входных параметров из командной строки
    def input_commands(self, args: list[str]) -> dict:
        ...
