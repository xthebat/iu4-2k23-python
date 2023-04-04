from dataclasses import dataclass


@dataclass
class Base:

    def __find_element(self, filename: str) -> list[str]:
        pass

    def print_function(self, filename: str) -> list:
        pass

    def print_typedef(self, filename: str) -> list:
        pass

    def print_define(self, filename: str) -> list:
        pass

    def find_string_number(self) -> int:
        pass
