from dataclasses import dataclass


@dataclass
class TypedefPrinting:
    declared_type: str
    target_type: str
    string_number: int = None
