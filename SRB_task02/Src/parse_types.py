# Файл содержит описание объектов для парсинга .h файла
from dataclasses import dataclass
from enum import Enum, unique


@unique
class ParseKeyWords(Enum):
    TYPEDEF = 1
    DEFINE = 2
    FUNCTION = 3


@dataclass
class ParseObject:
    name: str
    line_number: int
    file_name: str
    key_word: ParseKeyWords


@dataclass
class ParseDefine(ParseObject):
    value: str  # can be 15, (1 << 20), uint16_t etc.


@dataclass
class ParceFunc(ParseObject):
    return_type: str
    input_arg: dict  # 'variable' = int
    number_arg: int
    is_variable_arg: bool  # int func(int a, ...); ????
    func_key_words: str  # static, volatile, const, extern


@dataclass
class ParceTypedef(ParseObject):
    target_type: str
    