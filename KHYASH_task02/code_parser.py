import json
import os.path
from termcolor import cprint

DATA_TYPES = ["int", "string", "double", "char", "long"]
MODIFIERS = ["signed ", "unsigned ", ""]

class Function:
    name: str
    return_type: int
    args: dict

    def __init__(self, name: str, return_type: str, args: dict) -> None:
        self.name = name
        self.return_type = return_type
        self.args = args


class Typedef:
    name: str
    point_type: str

    def __init__(self, name: str, point_type: str) -> None:
        self.name = name
        self.point_type = point_type


class Define:
    name: str
    definition: str

    def __init__(self, name: str, definition: str) -> None:
        self.name = name
        self.definition = definition

# that class validates filetypes
class c_validator:
    def __init__(self) -> None:
        self.data_types = DATA_TYPES
        self.modifiers = MODIFIERS

    def check(self, line: str, space: str = "", typedef: bool = False) -> None:
        # special typedef option because whe should to catch struct
        if typedef and line.startswith("struct"):
            return line.split("{")[0].strip()

        # other cases
        for data_type in self.data_types:
            for i in self.modifiers:
                template = i + data_type + space
                if line.startswith(i + data_type + space):
                    return template

        return False

    def add_typedef(self, name: str) -> None:
        self.data_types.append(name)
