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
    #     прочитать
    #     записать
    #     define_list ->  define parse (ReadFile.code) -> list
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


def main():
    # define1 = Define()
    # define1.strNum = DefineParse.strnum_return()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))