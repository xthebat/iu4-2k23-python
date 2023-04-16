import argparse
import json
import os.path
from dataclasses import dataclass

@dataclass
class Function:
    """
    Экземпляры: найденные функции
    """

    name: str
    """Имя функции"""

    return_type: str
    """Возвращаемый тип"""

    arguments: list
    """Аргументы функции"""

@dataclass
class Variable:
    """
    Экземпляры: найденные глобальные переменные
    """

    name: str
    """Имя переменной"""

    data_type: str
    """Тип данных"""

    value: str
    """Значение переменной"""

@dataclass
class Ifdef:
    """
    Экземпляры: найденные ifdef
    """

    expression: str
    """Выражение условия"""

@dataclass
class Include:
    """
    Экземпляры: найденные include
    """

    filename: str
    """Имя вкладываемого файла"""

    contents: str
    """Содержание вкладываемого файла"""

@dataclass
class SyntaxError:
    """
    Экземпляры: синтаксические ошибки
    """

    message: int
    """Содержание ошибки"""

class CHeaderParser:
    """
    Интерфейс, описывающий классы, необходимые для парсинга
    """

    def __init__(self):
        self.functions = []
        self.variables = []
        self.ifdefs = []
        self.includes = []
        self.errors = []
        self.line_number = 0
        """Номер строки, где найдена структура"""

    def get_json(self, input_str):
        """
        Метод, получающий данные из JSON
        """

        data = json.loads(input_str)
        self.functions = [Function(**f) for f in data.get('functions', [])]
        self.variables = [Variable(**v) for v in data.get('variables', [])]
        self.ifdefs = [Ifdef(**i) for i in data.get('ifdefs', [])]
        self.includes = [Include(**i) for i in data.get('includes', [])]
        self.errors = [SyntaxError(**e) for e in data.get('errors', [])]
        self.line_number = data.get('line_number', 0)

    def set_json(self):
        """
        Метод, создающий JSON
        """

        data = {
            'functions': [f.__dict__ for f in self.functions],
            'variables': [v.__dict__ for v in self.variables],
            'ifdefs': [i.__dict__ for i in self.ifdefs],
            'includes': [inc.__dict__ for inc in self.includes],
            'errors': [err.__dict__ for err in self.errors],
            'line_number': self.line_number
        }
        return json.dumps(data, indent=4)

    def parse(self, str input):
    ...

    def print(self):
    ...


def main(args: list[str]) -> int:
    parser = argparse.ArgumentParser(description="C Header Parser")

    parser.add_argument("-of", "--output-functions", action="store_true", help="output list of all functions")
    parser.add_argument("-od", "--output-directives", action="store_true", help="output list of all compiler directives")
    parser.add_argument("-ot", "--output-types", action="store_true", help="output list of all type declarations")
    parser.add_argument("-f", "--input-file", type=str, help="input file for parsing or saved file")
    parser.add_argument("-j", "--json", type=str, help="output file in JSON format")

    args = parser.parse_args()

    if args.input_file:
        # Check the file extension to determine the type of input file
        if args.input_file.endswith(".c"):
            # Parse the C header file
            # ...
            pass
        elif args.input_file.endswith(".json"):
            # Load the saved state from a JSON file
            # ...
            pass
        else:
            print("Error: unsupported file type")
            parser.print_usage()
            return 1

    if args.output_functions:
        # Output list of all functions
        # ...
        pass

    if args.output_directives:
        # Output list of all compiler directives
        # ...
        pass

    if args.output_types:
        # Output list of all type declarations
        # ...
        pass

    if args.json:
        # Save the output in JSON format to a file
        # ...
        pass
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))