from dataclasses import dataclass
from base_class import Base
from typedef_print_class import TypedefPrinting


@dataclass
class Typedef(Base):
    def __find_element(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.readlines()

        temp_list = [element for element in file_content if 'typedef' in element]
        return temp_list

    def __find_typedef_declared(self, string: str) -> str:
        temp_list = string.split()
        declared_list = [element for element in temp_list if 'typedef' != element or ';' not in element]
        return ' '.join(declared_list)

    def __find_typedef_target(self, string: str) -> str:
        temp_list = string.split()
        typedef_target = ''

        for element in temp_list:
            if element.find(';'):
                typedef_target = element[:element.index(';')]
        return typedef_target

    def print_typedef(self, filename: str) -> list:
        typedef_list = Typedef.__find_element(self, filename)
        typedef_object_list = []

        for element_typedef in typedef_list:
            declared_type = Typedef.__find_typedef_declared(self, element_typedef)
            target_type = Typedef.__find_typedef_declared(self, element_typedef)

            typedef_object = TypedefPrinting(declared_type, target_type)
            typedef_object_list.append(typedef_object)

        return typedef_object_list
