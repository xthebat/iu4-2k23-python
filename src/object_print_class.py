from dataclasses import dataclass


@dataclass
class DefineObject:
    define_name: str = None
    define_value: str = None
    string_number: int = None


@dataclass
class FunctionObject:
    returned_type: str = None
    func_name: str = None
    func_arguments: list[str] = None
    string_number: int = None


@dataclass
class TypedefObject:
    declared_type: str = None
    target_type: str = None
    string_number: int = None