from dataclasses import dataclass

@dataclass
class Function(Compiler):
    name: str
    return_type: str
    arguments: list
    line_number: int

@dataclass
class Variable(Compiler):
    name: str
    data_type: str
    value: str
    line_number: int

@dataclass
class Ifdef(Compiler):
    expression: str
    line_number: int

@dataclass
class Include(Compiler):
    filename: str
    contents: str
    line_number: int

@dataclass
class SyntaxError(Compiler):
    message: int
    line_number: int