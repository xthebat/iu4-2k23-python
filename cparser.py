import json
import os.path
import argparse
import sys
from dataclasses import dataclass


@dataclass
class Typedef:
    strNum: int
    name: str
    userType: str


@dataclass
class Function:
    strNum: int
    type_return: str
    name: str
    args: dict


@dataclass
class Define:
    strNum: int
    name: str
    value: str


class Parse:
    def __init__(self, CFileName: str, JSONFileName: str):
        self.define = []
        self.typedef = []
        self.function = []
        self.cfilename = CFileName
        self.jsonfilename = JSONFileName

    def readcfile(self) -> list[str]:
        with open(self.cfilename, encoding='utf-8') as cfile:
            file_strings = cfile.read().splitlines()
        return file_strings

    def do_parse(self):
        file_strings = self.readcfile()
        self.define = DefineParse.parse(file_strings)
        self.function = FunctionParse.parse(file_strings)
        self.typedef = TypedefParse.parse(file_strings)
class Boot:
    def run(self, c_file_name: str, json_file_name: str, print_res: bool) -> Parse:
        parse = Parse(c_file_name, json_file_name)
        parse.do_parse()
        if print_res:
            self.print_res()
        return parse

    def print_res(self):
        pass

    def json_generate(self, parse: Parse):
        pass
class DefineParse:
    def __init__(self, input_name: str, code: list):
        self.defines_all = []

    def parse(self, code : list):
        pass
    pass

class TypedefParse:
    pass

class FunctionParse:
    pass


def main(ags: list):
    parse_structure = Boot.run()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))