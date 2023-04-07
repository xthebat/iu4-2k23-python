import argparse
import json
import re
import os

#Команда Невзорова Юлиана ИУ4-83Б, Ильин Андрей ИУ4-82Б
#Со всеми бонусами

#Определяем регулярные выражения для синтаксического анализа заголовочных файлов C:
FUNC_REGEX = r'^\s*(\w+\s+\**)(\w+)\s*\(([^\)]*)\)\s*;'
TYPE_REGEX = r'^\s*typedef\s+(\w+)\s+(\w+)\s*;'
DEFINE_REGEX = r'^\s*#define\s+(\w+)\s+(.*)$'
VARIABLE_REGEX = r'^\s*(extern\s+)?(\w+\s+\**)(\w+)\s*;'
STRUCT_REGEX = r'^\s*struct\s+(\w+)\s*{([^}]*)}\s*;'

# Make by Nevzorova
class CHeaderView:
    def __init__(self) -> None:
        self.functions = []
        self.types = []
        self.defines = []
        self.variables = []
        self.structures = []

    def add_function(self, return_type: str, name: str, args: str, line_num: int) -> None:
        self.functions.append({'return_type': return_type.strip(),
                               'name': name.strip(),
                               'args': args.strip(),
                               'line_num': line_num})

    def add_type(self, target_type: str, name: str, line_num: int) -> None:
        self.types.append({'target_type': target_type.strip(),
                           'name': name.strip(),
                           'line_num': line_num})

    def add_define(self, name: str, value: str, line_num: int) -> None:
        self.defines.append({'name': name.strip(),
                             'value': value.strip(),
                             'line_num': line_num})

    def add_variable(self, var_type: str, name: str, line_num: int) -> None:
        self.variables.append({'var_type': var_type.strip(),
                               'name': name.strip(),
                               'line_num': line_num})

    def add_structure(self, name: str, fields: str, line_num: int) -> None:
        self.structures.append({'name': name.strip(),
                                'fields': fields,
                                'line_num': line_num})

    def to_dict(self) -> dict:
        return {'functions': self.functions,
                'types': self.types,
                'defines': self.defines,
                'variables': self.variables,
                'structures': self.structures}

    def to_json(self, filename: str) -> None:
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def from_dict(cls, data: dict) -> 'CHeaderView':
        header_view = cls()
        for func in data['functions']:
            header_view.add_function(func['return_type'], func['name'], func['args'], func['line_num'])
        for type_decl in data['types']:
            header_view.add_type(type_decl['target_type'], type_decl['name'], type_decl['line_num'])
        for define in data['defines']:
            header_view.add_define(define['name'], define['value'], define['line_num'])
        for var in data['variables']:
            header_view.add_variable(var['var_type'], var['name'], var['line_num'])
        for struct in data['structures']:
            header_view.add_structure(struct['name'], struct['fields'], struct['line_num'])
        return header_view

# Make by Ilyin
    @classmethod
    def from_json(cls, filename: str) -> 'CHeaderView':
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)

    def output_functions(self):
        for func in self.functions:
            print(f"{func['return_type']} {func['name']}({func['args']})")

    def output_types(self):
        for type_decl in self.types:
            print(f"typedef {type_decl['target_type']} {type_decl['name']};")

    def output_defines(self):
        for define in self.defines:
            print(f"#define {define['name']} {define['value']}")

    def output_variables(self):
        for var in self.variables:
            print(f"{var['var_type']} {var['name']}")

    def output_structures(self):
        for struct in self.structures:
            print(f"struct {struct['name']} {{")
            fields = struct['fields'].split(';')
            for field in fields:
                if field.strip() != '':
                    print(f"    {field.strip()};")
            print("}")

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            # Remove comments
            line = re.sub(r'//.*$', '', line)
            line = re.sub(r'/\*.*?\*/', '', line, flags=re.DOTALL)
            # Parse function declarations
            match = re.match(FUNC_REGEX, line)
            if match:
                self.add_function(match.group(1), match.group(2), match.group(3), i + 1)
                continue
            # Parse typedefs
            match = re.match(TYPE_REGEX, line)
            if match:
                self.add_type(match.group(1), match.group(2), i + 1)
                continue
            # Parse defines
            match = re.match(DEFINE_REGEX, line)
            if match:
                self.add_define(match.group(1), match.group(2), i + 1)
                continue
            # Parse variables
            match = re.match(VARIABLE_REGEX, line)
            if match:
                self.add_variable(match.group(2), match.group(3), i + 1)
                continue
            # Parse structures
            match = re.match(STRUCT_REGEX, line)
            if match:
                self.add_structure(match.group(1), match.group(2), i + 1)
                continue

# Make by Nevzorova
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парссинг файла C')
    parser.add_argument('input_file', help='Файл, который парсим.')
    parser.add_argument('-o', '--output-file', help='Файл JSON, который выводим.')
    args = parser.parse_args()

    header_view = CHeaderView()
    header_view.parse_file(args.input_file)

    if args.output_file:
        header_view.to_json(args.output_file)
    else:
        header_view.output_functions()
        header_view.output_types()
        header_view.output_defines()
        header_view.output_variables()
        header_view.output_structures()
