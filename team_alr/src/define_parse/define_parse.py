from dataclasses import dataclass

@dataclass
class Define: #экземпляры: найденные define
    number: int # номер строки, в которой обнаружен define
    name: str   # имя макроса
    value: str  # значение макроса
    def instance_define(self, number: int, name: str, value: str):
        self.number = number
        self.name = name
        self.value = value
    #функция, назначающая атрибуты из ParseDefine
    def check_value(self) -> bool:
        ...
    #проверка, не является ли значение макроса выражением
    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

class ParseDefine: #экземпряр: строка из файла
    def number_of_string(self) -> int:
        ...
    #метод, возращающий номер строки
    def name_of_define(self) -> str:
        ...
    #метод, возвращающий имя макроса
    def value_of_define(self) -> str:
        ...
    #метод, возвращающий значение макроса

#класс class AllElement(Function, Define, Typedef) - общий класс
#методы - создание списков экзепляров классов с их атрибутами

#создаем генератор строк текста
#каждая новая строка - экземпляр класса parse_define