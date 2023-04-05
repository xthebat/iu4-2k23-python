# import json
# import os.path
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


class Parsing:
    def __init__(self, code_path: str) -> None:
        # there we'll store the parsing results
        self.function_list = []
        self.define_list = []
        self.typedef_list = []
        self.code_path = code_path

    def read_file(self) -> None:
        with open(self.code_path, encoding = "utf-8") as file:
            code = file.read().splitlines()
        return code

    def show_data(self) -> None:
        print()
        cprint("functions".upper(), "blue")
        for i in self.function_list:
            print(f"NAME - {i.name}")
            print(f"return_type - {i.return_type}")
            print(i.args)
            print()
        print()
        cprint("typedef's".upper(), "blue")
        for i in self.typedef_list:
            print(f"NAME - {i.name}")
            print(f"point_type - {i.point_type}")
            print()
        print()
        cprint("define's".upper(), "blue")
        for i in self.define_list:
            print(f"NAME - {i.name}")
            print(f"definition - {i.definition}")
            print()

    def run(self, show_data: bool = True) -> None:
        self.code = self.read_file()
        self.validator = c_validator()

        self.parse_typedef()
        self.parse_define()
        self.parse_function()

        if show_data:
            self.show_data()

    def parse_function(self) -> bool:
        cprint("* functions", "yellow")

        inside_function = False

        for line in self.code:
            line = line.strip()

            file_type_check = self.validator.check(line, space = " ")

            if not inside_function and file_type_check and "(" in line and ")" in line:
                # print(line)
                function_name, arguments_str = line.split(file_type_check)[1].rstrip(")").split("(")
                arguments = arguments_str.split(',')
                arguments = list(map(lambda a: a.strip().split(), arguments))
                return_type = file_type_check.strip()

                arguments_dict = {}
                for i in arguments:
                    if len(i) == 1:
                        arguments_dict[i[0]] = None
                    else:
                        arguments_dict[i[0]] = i[1]

                function = Function(
                        name = function_name,
                        return_type = return_type,
                        args = arguments_dict
                        )

                self.function_list.append(function)
                inside_function = True

            elif inside_function and line.endswith("}"):
                inside_function = False

        cprint(f" -- done {len(self.function_list)} functions", "green")

    def parse_define(self) -> bool:
        cprint("* define's", "yellow")

        for line in self.code:
            line = line.strip()

            if line.startswith("#define"):
                line = line.split("#define")[1].strip()
                name, definition = line.split(None, 1)
                define = Define(name = name, definition = definition)
                self.define_list.append(define)
        cprint(f" -- done {len(self.define_list)} define's", "green")

    def parse_typedef(self) -> bool:
        cprint("* typedef's", "yellow")

        inside_typedef = False
        waiting_type = ""

        for line in self.code:
            line = line.strip()

            if line.startswith("typedef"):
                line = line.split("typedef ")[1]
                point_type = self.validator.check(line, typedef = True)
                name =  ""
                if line.endswith(";"):
                    name = line.split(point_type)[1].strip().rstrip(";")
                    self.validator.add_typedef(name)
                    typedef = Typedef(name = name, point_type = point_type)
                    self.typedef_list.append(typedef)
                else:
                    waiting_type = point_type
                    inside_typedef = True

            elif line.startswith("} ") and inside_typedef:
                name = line.split("}")[1].strip().rstrip(";")
                self.validator.add_typedef(name)
                typedef = Typedef(name = name, point_type = waiting_type)
                self.typedef_list.append(typedef)
                waiting_type = ""
                inside_typedef = False


        cprint(f" -- done {len(self.typedef_list)} typedef's", "green")