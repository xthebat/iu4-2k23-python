class FunctionsList:

    def __init__(self, list_of_fuctions_as_classes):
        self.list_to_parse = list_of_fuctions_as_classes

    def processed_list(self):
        newlist = []
        for element in self.list_to_parse:
            newlist.append(
                {
                    'func name': element.func_name,
                    'func type': element.returned_type,
                    'arguments': element.func_arguments
                }
            )
        return newlist


class DefinesList:

    def __init__(self, list_of_defines_as_classes):
        self.list_to_parse = list_of_defines_as_classes

    def processed_list(self):
        newlist = []
        for element in self.list_to_parse:
            newlist.append(
                {
                    'define name': element.define_name,
                    'define value': element.define_value
                }
            )
        return newlist


class TypedefsList:

    def __init__(self, list_of_typedefs_as_classes):
        self.list_to_parse = list_of_typedefs_as_classes

    def processed_list(self):
        newlist = []
        for element in self.list_to_parse:
            newlist.append(
                {
                    'declared type': element.declared_type,
                    'target type': element.target_type
                }
            )
        return newlist


class DictionaryForJSON:
    def __init__(self, functions, defines, typedefs):
        self.list_of_functions = FunctionsList(functions)
        self.list_of_defines = DefinesList(defines)
        self.list_of_typedefs = TypedefsList(typedefs)

    def output_dictionary(self):
        dictionary = {
            'Functions': self.list_of_functions,
            'Defines': self.list_of_defines,
            'Typedefs': self.list_of_typedefs
        }
        return dictionary