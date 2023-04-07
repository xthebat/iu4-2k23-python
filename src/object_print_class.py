from dataclasses import dataclass


@dataclass
class DefinePrinting:
    define_name: str
    define_value: str
    string_number: int = None


@dataclass
class FunctionPrinting:
    returned_type: str
    func_name: str
    func_arguments: list[str]
    number_string: int = None


@dataclass
class TypedefPrinting:
    declared_type: str
    target_type: str
    string_number: int = None