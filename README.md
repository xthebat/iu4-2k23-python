# Stream 08

## Как писать документацию к коду

```python
class FilteredBinaryIO(Readable):
    """
    Stream to wrap other stream.
    """

    @classmethod
    def from_bytes(cls, data: bytes, **kwargs) -> Self:
        """
        Method creates specified stream from bytes.
    
        :param data: Data to create stream from.
        :param kwargs: Free argument to create stream from bytes.
        :return: Created stream according to arguments.
        """
        return cls(BytesIO(data), **kwargs)
```

## Переусложнение кода

Инкапсуляция структур

```python
from dataclasses import dataclass


@dataclass
class Define:  # экземпляры: найденные define

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
```

## Плохие имена

Бессмысленные сокращение имен переменных, функций и т.п.

```python
from dataclasses import dataclass


@dataclass
class Function:
    numb_line: int


class ParsFunction:

    # функции, достающие из строки нужные элементы (имя функции, возвращаемый тип и т.д.)
    def ent_line(self, funct_line: str) -> int:
        ...
```

## Некорректная инициализация dataclass + изменяемые сущности

```python
@dataclass
class AllElement:  # общий класс для хранения списков классов
    function_list: list[Function] = None

    def create_list(self):
        self.function_list = []
        self.define_list = []
        self.typedef_list = []

    # функции добавления нового элемента в списки по классам
    def add_function(self, func: Function):
        self.function_list.append(func)
```

## Некорректный нейминг

```python
class List_of_functions:
    ...


class dictionary_to_json:
    ...


# https://github.com/xthebat/iu4-2k23-python/pull/50/files
class c_validator:
    def __init__(self) -> None:
        self.data_types = DATA_TYPES
        self.modifiers = MODIFIERS
```

## Некорректный вызов функций

```python
def print_define(self, filename: str) -> list:
    define_list = Define.__find_element(self, filename)
```

## Приватные методы в интерфейсе + метод не абстрактный

```python
class Base:

    def __find_element(self, filename: str) -> list[str]:
        pass
```

## Использование дефолтного парсера аргументов

```python
    parser.add_argument(
    '-f',
    type=str,
    required=True,
    dest='filepath',
    help='filepath to parse',
)
```

## Некорректная документация + изменяемый объект

```python
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
```

## Использование статических переменных как обычных

```python
class Function:
    name: str
    return_type: int
    args: dict

    def __init__(self, name: str, return_type: str, args: dict) -> None:
        self.name = name
        self.return_type = return_type
        self.args = args
```

## Не используется функциональные паттерн

```python
 for data_type in self.data_types:
    for i in self.modifiers:
        template = i + data_type + space
        if line.startswith(i + data_type + space):
            return template
```

## Рассмотреть подробнее

https://github.com/xthebat/iu4-2k23-python/pull/50/files

## Конвертация в словарь

```python
@dataclass
class typedef_unit:
    type: str
    annotation: str

    def __dict__(self):
        pass
```

## Не будет работать

```python
class Analyzer:
    def __init__(self, filestr_):
        _filestr = filestr_
        _analyzed_data = None


def test():
    pass
```

## Vom...it

```python
FUNC_REGEX = r'^\s*(\w+\s+\**)(\w+)\s*\(([^\)]*)\)\s*;'
TYPE_REGEX = r'^\s*typedef\s+(\w+)\s+(\w+)\s*;'
DEFINE_REGEX = r'^\s*#define\s+(\w+)\s+(.*)$'
VARIABLE_REGEX = r'^\s*(extern\s+)?(\w+\s+\**)(\w+)\s*;'
STRUCT_REGEX = r'^\s*struct\s+(\w+)\s*{([^}]*)}\s*;'
```

```python
    def add_function(self, return_type: str, name: str, args: str, line_num: int) -> None:


    self.functions.append({'return_type': return_type.strip(),
                           'name': name.strip(),
                           'args': args.strip(),
                           'line_num': line_num})
```