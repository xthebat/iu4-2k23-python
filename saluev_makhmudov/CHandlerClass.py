class CHandlerClass:
    def __init__(self):
        self.functions = []
        self.directives = []
        self.types = []

    def functions_handler(self, idx, line):  # ToDo: args
        self.functions.append(
            {
                'line': idx,
                'function': line.split()[1].split('(')[0],
                'arguments': None
            }
        )

    def directives_handler(self, idx, line):  # ToDo: ??
        self.directives.append(
            {
                'line': idx,
                'directive': line.split()[1].split('(')[0]
            }
        )

    def types_handler(self, idx, line):  # ToDo: types
        for count, ntype in enumerate(line.split('(')[1].split(')')[0].split(), 1):
            if count % 2:
                self.types.append(
                    {
                        'line': idx,
                        'types': ntype
                    }
                )

    def reader_file(self, filename):
        with open(filename, 'r') as header:
            for idx, line in enumerate(header.readlines(), 1):
                # functions
                if line.find('void') != -1:
                    self.functions_handler(idx, line)

                # directives
                if line.find('define') != -1:  # ToDo: ifdef; ifndef; include
                    self.directives_handler(idx, line)

                # types
                if line.find('uint32_t') != -1:  # ToDo: types
                    self.types_handler(idx, line)
        return self.functions, self.directives, self.types
