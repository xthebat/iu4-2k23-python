from dataclasses import dataclass


@dataclass
class DefineObject:
    define_name: str
    define_value: str
    string_number: int = None


@dataclass
class FunctionObject:
    returned_type: str
    func_name: str
    func_arguments: list[str]
    number_string: int = None


@dataclass
class TypedefObject:
    declared_type: str
    target_type: str
    string_number: int = None