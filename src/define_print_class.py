from dataclasses import dataclass


@dataclass
class DefinePrinting:
    define_name: str
    define_value: str
    string_number: int = None
