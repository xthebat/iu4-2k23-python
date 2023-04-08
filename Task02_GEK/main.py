from dataclasses import dataclass

class CHeaderParser:
    def set_json(self, str input):
        ...
    def get_json(self, str output):
        ...
    def parse(self, str input):
        ...
    def print(self):
        ...
    Function: dict
    Variable: dict
    Ifdef: dict
    Include: dict
    SyntaxError: dict
    line_number: int


@dataclass
class Function(CHeaderParser):
    name: str
    return_type: str
    arguments: list

@dataclass
class Variable(CHeaderParser):
    name: str
    data_type: str
    value: str

@dataclass
class Ifdef(CHeaderParser):
    expression: str

@dataclass
class Include(CHeaderParser):
    filename: str
    contents: str

@dataclass
class SyntaxError(CHeaderParser):
    message: int