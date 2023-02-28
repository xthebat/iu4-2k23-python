import argparse
import sys


def split_str(string, max_len):
    last_index = 0
    indexes = []
    tag = False
    for index, symbol in enumerate(string):
        if symbol == '@':
            tag = True
        if symbol == ':':
            tag = False
        if not tag and (symbol == " " or symbol == "\n"):
            if index > max_len:
                max_len += last_index
                if last_index == 0:
                    return []
                indexes.append(last_index)
            else:
                last_index = index

    indexes.append(len(string))
    return indexes


def print_result(indexes, string):
    substring = "Substring: #{0}:"

    start = 0
    for index, str_index in enumerate(indexes, 1):
        print(substring.format(index))
        print(string[start:str_index], "\n")
        start = str_index


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Путь к файлу", required=True)
    parser.add_argument(
        "-n", "--max-len", help="Максимальная длина строки", type=int, default=200
        )
    args = parser.parse_args()
    try:
        with open(args.file, "r") as file:
            string = file.read()
    except FileNotFoundError:
        print("Нет такого файла")
        sys.exit()

    indexes = split_str(string, args.max_len)
    if len(indexes) == 0:
        print("Не могу разделить файл")
    else:
        print_result(indexes, string)


if __name__ == '__main__':
    main()
