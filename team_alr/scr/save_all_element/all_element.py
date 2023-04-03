from dataclasses import dataclass
from function_pars.func_parsing import Function
from typedef_pars.typedef_pars import Typedef
from define_parse.define_parse import Define


@dataclass
class AllElement:  # общий класс для хранения списков классов
    function_list: list[Function] = None
    #define_list: list[Define] = None
    #typedef_list: list[Typedef] = None

    def create_list(self):
        self.function_list = []
        self.define_list = []
        self.typedef_list = []

    # функции добавления нового элемента в списки по классам
    def add_function(self, func: Function):
        self.function_list.append(func)

    def add_define(self, define: Define):
        self.define_list.append(define)

    def add_typedef(self, typ: Typedef):
        self.typedef_list.append(typ)

    # функции возвращения списков элементов

    def out_funct(self):
        return self.function_list

    def out_define(self):
        return self.define_list

    def out_typedef(self):
        return self.typedef_list

    # функции вывода из спсиков по индексу

    def index_funct(self, index_fun: int) -> Function:
        ...
        return self.function_list[index_fun]

    def index_def(self, index_def: int) -> Define:
        ...
        return self.define_list[index_def]

    def index_typedef(self, index_typ: int) -> Typedef:
        ...
        return self.typedef_list[index_typ]