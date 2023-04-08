import os

from dataclasses import dataclass


class Ifdef:
    def __init__(self, condition):
        self.condition = condition

class SimpleParser:
    def __init__(self):
        self.line_number = 0
        self.errors = []
        self.ifdefs = []
        self.declarations = []

class CHeaderParser:
    def set_json(self, str input):
        ...
    def get_json(self, str output):
        ...
    def parse(self, input_filename):
        if not os.path.exists(input_filename):
            raise ValueError(f"Input file '{input_filename}' not found")

        with open(input_filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            self.line_number += 1

            # remove whitespace at beginning and end of line
            line = line.strip()

            # check for preprocessor directives
            if line.startswith('#'):
                self._parse_preprocessor_directive(line)
                continue

            # check for function or variable declaration
            if '(' in line and ')' in line and ';' in line:
                self._parse_declaration(line)
                continue

            # check for syntax errors
            if line:
                self.errors.append(SyntaxError(f"Syntax error on line {self.line_number}: {line}"))


    def _parse_preprocessor_directive(self, line):
        directive = line.strip("#").strip()
        self.directives.append(directive)

    def _parse_declaration(self, line):
        declaration = line[:line.find(';')].strip()
        self.declarations.append(declaration)

    def print(self):
        results = {
            "Function": {},
            "Variable": {},
            "Ifdef": {},
            "Include": {},
            "SyntaxError": {},
            "line_number": self.line_number
        }

        for directive in self.directives:
            if directive.startswith("include"):
                results["Include"][directive] = None
            elif directive.startswith("ifdef") or directive.startswith("ifndef"):
                results["Ifdef"][directive] = None

        for declaration in self.declarations:
            if "(" in declaration and ")" in declaration:
                results["Function"][declaration] = None
            else:
                results["Variable"][declaration] = None

        for error in self.errors:
            results["SyntaxError"][str(error)] = None

        for category, items in results.items():
            if isinstance(items, dict):
                print(f"{category}:")
                for item in items:
                    print(f"    {item}")
            else:
                print(f"{category}: {items}")

if __name__ == "__main__":
    parser = CHeaderParser()
    parser.parse("example_file.txt")
    parser.print()

@dataclass
class Function(CHeaderParser):
    name: str
    return_type: str
    arguments: list

@dataclass
class Variable(CHeaderParser):
    name: str
    data_type: str
    value: str

@dataclass
class Ifdef(CHeaderParser):
    expression: str

@dataclass
class Include(CHeaderParser):
    filename: str
    contents: str

@dataclass
class SyntaxError(CHeaderParser):
    message: int