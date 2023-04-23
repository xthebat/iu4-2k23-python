from dataclasses import dataclass


@dataclass
class BaseParsedObject:

    def find_object(self, filename: str) -> list[str]:
        raise NotImplementedError

    def print_object(self, filename: str) -> list:
        raise NotImplementedError

    def find_string_number(self, object_element: str, filename: str) -> int:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.readlines()

        return file_content.index(object_element)
