class List_of_functions:

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


class List_of_defines:

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


class List_of_typedefs:

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


class dictionary_to_json:
    def __init__(self, functions, defines, typedefs):
        self.list_of_functions = List_of_functions(functions)
        self.list_of_defines = List_of_defines(defines)
        self.list_of_typedefs = List_of_typedefs(typedefs)

    def output_dictionary(self):
        dictionary = {
            'Functions': self.list_of_functions,
            'Defines': self.list_of_defines,
            'Typedefs': self.list_of_typedefs
        }
        return dictionary