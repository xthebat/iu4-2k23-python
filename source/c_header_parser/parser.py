from json import loads
from sys import stderr

from .dtypes import *


class Analyzer:
    def __init__(self, raw_data_, config_filename_='config.json'):
        self._raw_data = raw_data_
        self._analyzed_data: CHeaderView = CHeaderView([], [], [])
        self._config = {}
        self._load_config(config_filename_)

    def _load_config(self, filename_):
        try:
            with open(file=filename_, mode='r', encoding='utf-8') as fstream:
                self._config = loads(fstream.read())
        except FileNotFoundError:
            print(f'[ERROR] Can\'t open file with name <{filename_}>!', file=stderr)
            exit(1)

    def _parse_line(self, line_: str, row_: int) -> ParserUnit or None:
        result_unit = ParserUnit(row_, 0, None)
        for unit_type in self._config['parsing_units']:
            association_type, association = self._config['keywords'][unit_type]
            if association_type == 'str':
                line_units = line_.split()
                if association in line_units:
                    result_unit.char_offset = line_.index(association)
                    declaration_inner_index = line_units.index(association)
                    result_unit.object = parser_units[unit_type](line_units[declaration_inner_index + 1],
                                                                 line_units[declaration_inner_index + 2])
                    return result_unit

            elif association_type == 'list':
                func_unit = FuncUnit('', '', [])
                associations = self._config[association]
                if not (';' in line_ and '(' in line_ and ')' in line_):
                    continue
                line_ = line_.strip()
                split_point = line_.index('(')
                base_part, args_part = line_[0:split_point], line_[split_point + 1:]
                args_part = args_part.replace(')', ' ')
                args_part = args_part.replace('const', '')
                args_part = args_part.replace('{', ' ')
                args_part = args_part.replace(';', ' ')
                args_pairs = args_part.split(',')

                for c_type in associations:
                    if c_type in base_part.strip():
                        func_unit.type = c_type
                        func_unit.name = base_part[base_part.rindex(' '):].strip()

                for arg_pair in args_pairs:
                    c_var = CVar('', '')
                    arg_pair = arg_pair.strip()
                    split_point = arg_pair.rindex(' ')
                    c_var.name = arg_pair[split_point:].strip()
                    c_var.type = arg_pair[: split_point].strip()
                    if c_var.type not in associations:
                        print(f'[WARNING] Can\'t identify type for argument {c_var.name} in line {row_}, skipped!',
                              file=stderr)
                    func_unit.args.append(c_var)
                result_unit.object = func_unit
                return result_unit

        return None

    def analyze_data(self):
        for line_nu, line in enumerate(self._raw_data):

            parsed_unit = self._parse_line(line[:-1], line_nu)

            if parsed_unit is None:
                continue
            obj_type = type(parsed_unit.object)
            if obj_type == FuncUnit:
                self._analyzed_data.functions.append(parsed_unit)
            elif TypedefUnit:
                self._analyzed_data.typedefs.append(parsed_unit)
            elif DefineUnit:
                self._analyzed_data.defines.append(parsed_unit)

    def data_as_dict(self) -> dict:
        return self._analyzed_data.__dict__()
