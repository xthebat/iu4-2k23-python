from base_class import BaseParsedObject
from dataclasses import dataclass
from object_print_class import DefineObject


@dataclass
class Define(BaseParsedObject):
    def find_object(self, filename: str) -> list[str]:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.readlines()

        temp_list = [element for element in file_content if '#define' in element]
        return temp_list

    def __get_define_value(self, string: str) -> str:
        return string.split()[2]

    def __get_define_name(self, string: str) -> str:
        return string.split()[1]

    def print_object(self, filename: str) -> list:
        define_list = self.find_object(filename)
        define_object_list = []

        for element_define in define_list:
            define_name = self.__get_define_name(element_define)
            define_value = self.__get_define_value(element_define)
            string_number = self.find_string_number(element_define, filename)

            define_object = DefineObject(define_name, define_value, string_number)
            define_object_list.append(define_object)

        return define_object_list