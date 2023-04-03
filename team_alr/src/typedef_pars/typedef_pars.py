from dataclasses import dataclass


@dataclass
class Typedef:
    line_number: int  # номер строки в которой был найден typedef
    typedef_type: str  # существующий тип данных которому присваиваем новое имя
    typedef_new_name: str  # новое имя для существующего типа данных

    def get_line_number(self):
        return self.line_number

    def get_typedef_type(self):
        return self.typedef_type

    def get_typedef_new_name(self):
        return self.typedef_new_name


@dataclass
class ParsTypedef:
    def find_typedef_line(self) -> str:
        ...
        return typedef_line

    def find_typedef_type(self, typedef_line: str) -> str:
        ...
        return typedef_type

    def find_typedef_new_name(self, typedef_line: str) -> str:
        ...
        return typedef_new_name

    def set_typedef(self):
        typedef = Typedef(self.find_typedef_line(),
                          self.find_typedef_type(),
                          self.find_typedef_new_name())
        return typedef
