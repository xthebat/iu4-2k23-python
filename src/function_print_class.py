from dataclasses import dataclass


@dataclass
class FunctionPrinting:
    returned_type: str
    func_name: str
    func_arguments: list[str]
    number_string: int = None
