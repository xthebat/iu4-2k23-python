from base_class import Base
from dataclasses import dataclass
from define_print_class import DefinePrinting


@dataclass
class Define(Base):
    def __find_element(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.readlines()

        temp_list = [element for element in file_content if '#define' in element]
        return temp_list

    def __find_define_value(self, string: str) -> str:
        return string.split()[2]

    def __find_define_name(self, string: str) -> str:
        return string.split()[1]

    def print_define(self, filename: str) -> list:
        define_list = Define.__find_element(self, filename)
        define_object_list = []

        for element_define in define_list:
            define_name = Define.__find_define_name(self, element_define)
            define_value = Define.__find_define_value(self, element_define)

            define_object = DefinePrinting(define_name, define_value)
            define_object_list.append(define_object)

        return define_object_list
