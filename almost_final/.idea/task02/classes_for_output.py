import json

from function_class import Function
from define_class import Define
from typedef_class import Typedef
from dataclasses import dataclass


class FunctionsList:

    def processed_list(self, filename:str):
        list_of_fuctions_as_classes = Function()
        list_to_parse = list_of_fuctions_as_classes.print_object(filename)
        newlist = []
        for element in list_to_parse:
            newlist.append(
                {
                    'func name': element.func_name,
                    'func type': element.returned_type,
                    'arguments': element.func_arguments,
                    'string number': element.string_number
                }
            )
        return newlist

class DefinesList:

    def processed_list(self, filename: str):
        list_of_defines_as_classes = Define()
        list_to_parse = list_of_defines_as_classes.print_object(filename)
        newlist = []
        for element in list_to_parse:
            newlist.append(
                {
                    'define name': element.define_name,
                    'define value': element.define_value,
                    'string number': element.string_number
                }
            )
        return newlist

class TypedefsList:

    def processed_list(self, filename: str):
        list_of_typedefs_as_classes = Typedef()
        list_to_parse = list_of_typedefs_as_classes.print_object(filename)
        newlist = []
        for element in list_to_parse:
            newlist.append(
                {
                    'declared type': element.declared_type,
                    'target type': element.target_type
                }
            )
        return newlist

@dataclass
class JsonDictionary:

    def output_dictionary(self, filename:str) -> dict:
        typedef = TypedefsList()
        function = FunctionsList()
        define = DefinesList()

        define_list = define.processed_list(filename)
        function_list = function.processed_list(filename)
        typedef_list = typedef.processed_list(filename)

        final_dictionary = {
            'Functions': function_list,
            'Defines': define_list,
            'Typedefs': typedef_list
        }

        return final_dictionary

    def print_to_json(self, filename: str, destination_file:str):
        temp_dictionary = self.output_dictionary(filename)
        with open(destination_file, "w") as output_file:
            json.dump(temp_dictionary, output_file)