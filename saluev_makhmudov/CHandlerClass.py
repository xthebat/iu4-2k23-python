def tryexcept(line):
    try:
        args = line.split('(')[1].split(')')[0]
    except IndexError:
        args = None
    return args


class CHandlerClass:
    def __init__(self):
        self.functions = []
        self.directives = []
        self.types = []

    def functions_handler(self, idx, line):
        args = tryexcept(line)
        self.functions.append(
            {
                'line': idx,
                'function': line.split()[1].split('(')[0],
                'arguments': args
            }
        )

    def directives_handler(self, idx, line):
        self.directives.append(
            {
                'line': idx,
                'directive': line.split()[0],
                'directive_value': line.split()[1].split('(')[0]
            }
        )

    def types_handler(self, idx, line):
        for count, ntype in enumerate(line.split('(')[1].split(')')[0].split(), 1):
            if count % 2:
                self.types.append(
                    {
                        'line': idx,
                        'type': ntype
                    }
                )

    def reader_file(self, filename):
        with open(filename, 'r') as header:
            for idx, line in enumerate(header.readlines(), 1):
                # functions
                if line.find('void') != -1:
                    self.functions_handler(idx, line)

                # directives
                if '#' in line and line.split()[0] in ['#define', '#ifdef', '#ifndef', '#include']:
                    self.directives_handler(idx, line)

                # types
                types = ['char', 'int', 'float', 'double', 'void']
                if line.find('(') != -1:
                    line = line.split(' ', 1)[1]
                for n_type in types:
                    if n_type in line:
                        self.types_handler(idx, line)
        return self.functions, self.directives, self.types
