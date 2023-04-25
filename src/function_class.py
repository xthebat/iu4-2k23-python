from base_class import BaseParsedObject
from dataclasses import dataclass
from object_print_class import FunctionObject
from itertools import takewhile

@dataclass
class Function(BaseParsedObject):

    def find_object(self, filename: str) -> list[str]:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.readlines()

        return [element for element in file_content if '(' in element]

    def __find_func_type(self, string: str) -> str:
        temp_list_words = string.split()
        return ' '.join([element for element in takewhile(lambda element: '(' not in element, temp_list_words)])

    def __find_func_name(self, string: str) -> str:
        temp_list_words = string.split()
        return ''.join(element[:element.index('(')] for element in temp_list_words if '(' in element)

    def __find_func_args(self, string: str) -> list[str]:
        return (string[string.index('(') + 1:string.index(')')]).split()

    def print_object(self, filename: str) -> list:
        function_list = self.find_object(filename)
        function_object_list = []

        for element_func in function_list:
            returned_type = self.__find_func_type(element_func)
            func_name = self.__find_func_name(element_func)
            func_arguments = self.__find_func_args(element_func)
            string_number = self.find_string_number(element_func, filename)

            function_object = FunctionObject(returned_type, func_name, func_arguments, string_number)
            function_object_list.append(function_object)
        return function_object_list
