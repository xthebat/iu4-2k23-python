from parsed_types import *


@dataclass
class CHeaderView:
    parsed_functions: list[ParsedFunction] = []
    parsed_type_defs: list[ParsedTypeDef] = []
    parsed_defines: list[ParsedDefine] = []
    parsed_inline_vars: list[ParsedInlineVariable] = []
    parsed_structs: list[ParsedStruct] = []

    def __dict__(self):
        pass

    def save_to_json(self, filepath: str):
        pass

    def recover_from_json(self, filepath: str):
        pass

