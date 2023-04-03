# Файл содержит описание объектов для парсинга .h файла
from dataclasses import dataclass


@dataclass
class Parse_object():
    name: str
    line_number: int
    file_name: str
    key_word: str  # func or define or typedef


@dataclass
class Parse_define(Parse_object):
    value: str  # can be 15, (1 << 20), uint16_t etc.


@dataclass
class Parce_func(Parse_object):
    return_type: str
    input_arg: dict  # 'variable' = int
    number_arg: int
    is_variable_arg: bool  # int func(int a, ...); ????
    func_key_words: str  # static, volatile, const, extern


@dataclass
class Parce_typedef(Parse_object):
    target_type: str
