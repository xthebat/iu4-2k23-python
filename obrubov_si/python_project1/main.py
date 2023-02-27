import sys
import os.path
import re


def main(args: list[str]):
    # проверка наилчия арументов
    if len(args) < 2:
        print(f" not enough {len(args)=}: required > 2")
        return -1

    # проверка  аргумента -n
    if len(args) > 3 and args[3] == "-n":
        substr_length = int(args[4])
    else:
        substr_length = 200

    # проверка -f пути до файла
    if args[1] == "-f" and len(args) > 2:
        if os.path.isfile(args[2]):
            file_path = args[2]
            file = open(file_path, encoding='utf-8')
            text = file.read()
            file.close()
            listed_text = re.findall(r'\S+|\n', text)
        else:
            print("incorrect file path")
    else:
        print(f"Incorrect input data")

    list_to_print = string_divider(login_detector(listed_text), substr_length)


def login_detector(listed_text: list[str]) -> list[str]:
    newlist = []
    for i in range(len(listed_text)):
        if listed_text[i].startswith('@') and listed_text[i + 1].endswith(':'):
            listed_text[i + 1] = listed_text[i] + ' ' + listed_text[i + 1]
        else:
            newlist.append(listed_text[i])
    return newlist


def string_divider(listed_string: list[str], max_length: int) -> list[str]:
    string_length = 0
    string = []
    sorted_text = []
    for i in range(len(listed_string)):

        if listed_string[i] == '\n':
            element_length = 0
        else:
            element_length = len(listed_string[i])

        if string_length + element_length + len(string) - string.count('\n') <= max_length:
            string_length += element_length
            if len(string) > 0:
                string_length += 1
            string.append(listed_string[i])
        else:
            if string_length > 0:
                list_to_string = ' '.join(string)
                sorted_text.append(list_to_string)
            string_length = 0
            string = [listed_string[i]]
            string_length += element_length

    if string:
        list_to_string = ' '.join(string)
        sorted_text.append(list_to_string)

    return sorted_text


def output(sorted_text: list[str], d: bool, path: str):
    for i in range(len(sorted_text)):
        print(f"\nSubstring #{i + 1}:\n{sorted_text[i]}")


if __name__ == '__main__':
    main(sys.argv)
