from dataclasses import dataclass


@dataclass
class DefineUnit:
    name: str
    value: str

    def __dict__(self):
        return {'name': self.name, 'value': self.value}


@dataclass
class TypedefUnit:
    type: str
    name: str

    def __dict__(self):
        return {'name':self.name, 'type': self.type}


@dataclass
class CVar:
    type: str
    name: str

    def __dict__(self):
        return {'name': self.name, 'type': self.type}


@dataclass
class FuncUnit:
    name: str
    type: str
    args: list[CVar]

    def __dict__(self):
        return {'name': self.name, 'type': self.type, 'args': [arg.__dict__() for arg in self.args]}


@dataclass
class ParserUnit:
    line: int
    char_offset: int
    object: FuncUnit or DefineUnit or TypedefUnit

    def __dict__(self):
        return {'line': self.line, 'object': self.object.__dict__(), 'offset': self.char_offset}


@dataclass
class CHeaderView:
    functions: list[ParserUnit]
    defines: list[ParserUnit]
    typedefs: list[ParserUnit]

    def __dict__(self):
        return {'functions': [element.__dict__() for element in self.functions],
                'defines': [element.__dict__() for element in self.defines],
                'typedefs': [element.__dict__() for element in self.typedefs]}


parser_units = {
    'define': DefineUnit,
    'typedef': TypedefUnit,
    'function': FuncUnit
}
