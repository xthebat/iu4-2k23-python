from dataclasses import dataclass
from base_class import BaseParsedObject
from object_print_class import TypedefObject


@dataclass
class Typedef(BaseParsedObject):
    typedef = 'typedef'

    def find_object(self, filename: str) -> list[str]:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.readlines()

        temp_list = [element for element in file_content if self.typedef in element]
        return temp_list

    def __find_typedef_declared(self, string: str) -> str:
        temp_list = string.split()
        declared_list = [element for element in temp_list if self.typedef != element or ';' not in element]
        return ' '.join(declared_list)

    def __find_typedef_target(self, string: str) -> str:
        temp_list = string.split()
        return ''.join(element[:element.index(';')] for element in temp_list if ';' in element)

    def print_object(self, filename: str) -> list:
        typedef_list = self.find_object(filename)
        typedef_object_list = []

        for element_typedef in typedef_list:
            declared_type = self.__find_typedef_declared(element_typedef)
            target_type = self.__find_typedef_declared(element_typedef)
            string_number = self.find_string_number(element_typedef, filename)

            typedef_object = TypedefObject(declared_type, target_type, string_number)
            typedef_object_list.append(typedef_object)

        return typedef_object_list
