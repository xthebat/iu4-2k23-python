from dataclasses import dataclass


@dataclass
class ParsedObject:
    line: int


@dataclass
class ParsedFunction(ParsedObject):
    return_type: str
    name: str
    args: list[str]


@dataclass
class ParsedTypeDef(ParsedObject):
    type_existing: str
    type_alis: str


@dataclass
class ParsedDefine(ParsedObject):
    name: str
    value: str


@dataclass
class ParsedInlineVariable(ParsedObject):
    name: str
    type: str
    expression: str


@dataclass
class ParsedStruct(ParsedObject):
    name: str
    variables: dict
