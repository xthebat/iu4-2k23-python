from base_class import Base
from dataclasses import dataclass
from function_print_class import FunctionPrinting


@dataclass
class Function(Base):

    def __find_element(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.readlines()

        temp_list = [element for element in file_content if element.find('(')]
        return temp_list

    def __find_func_type(self, string: str) -> str:
        temp_list_words = string.split()
        temp_list_type = []

        for element in temp_list_words:
            if '(' not in element:
                temp_list_type.append(element)
            else:
                break
        return ' '.join(temp_list_type)

    def __find_func_name(self, string: str) -> str:
        temp_list_words = string.split()

        func_name = ''
        for element in temp_list_words:
            if '(' in element:
                func_name = element[:element.index('(')]
        return func_name

    def __find_func_args(self, string: str) -> list[str]:
        return (string[string.index('(') + 1:string.index(')')]).split()

    def print_function(self, filename: str) -> list:
        function_list = Function.__find_element(self, filename)
        function_object_list = []

        for element_func in function_list:
            returned_type = Function.__find_func_type(self, element_func)
            func_name = Function.__find_func_name(self, element_func)
            func_arguments = Function.__find_func_args(self, element_func)

            function_object = FunctionPrinting(returned_type, func_name, func_arguments)
            function_object_list.append(function_object)
        return function_object_list
