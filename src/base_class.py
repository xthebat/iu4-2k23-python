from dataclasses import dataclass


@dataclass
    class BaseParsedObject:

    def __find_object(self, filename: str) -> list[str]:
        raise NotImplementedErrors

    def print_object(self, filename: str) -> list:
        raise NotImplementedError

    def find_string_number(self) -> int:
        raise NotImplementedError
