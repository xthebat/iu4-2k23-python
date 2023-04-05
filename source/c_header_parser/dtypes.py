from dataclasses import dataclass


@dataclass
class define_unit:
    name: str
    value: str

    def __dict__(self):
        pass


@dataclass
class typedef_unit:
    type: str
    annotation: str

    def __dict__(self):
        pass


@dataclass
class c_var:
    type: str
    name: str

    def __dict__(self):
        pass


@dataclass
class func_unit:
    name: str
    type: str
    args: list[c_var]

    def __dict__(self):
        pass


@dataclass
class parser_unit:
    line: int
    char_offset: int
    type: str
    object: dict

    def __dict__(self):
        pass


parser_units = {
    'define': define_unit,
    'typedef': typedef_unit,
    'function': func_unit
}
