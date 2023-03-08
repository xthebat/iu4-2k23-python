import argparse
import sys


def split_string(string: str, max_len: int) -> list[int]:
    last_index = 0
    indexes = []
    tag = False
    result_len = 0
    for index, symbol in enumerate(string):
        if symbol == '@':
            tag = True
        if symbol == ':':
            tag = False
        if not tag and symbol.isspace():
            if index - result_len > max_len:
                if last_index == 0 or last_index in indexes:
                    return []
                indexes.append(last_index)
                result_len = last_index
            else:
                last_index = index

    if len(string) - indexes[-1] > max_len:
        indexes.append(last_index)

    indexes.append(len(string))
    return indexes


def print_result(indexes: list[int], string: str):
    start = 0
    for index, end in enumerate(indexes, 1):
        print(f"Substring: #{index}:")
        print(string[start:end], "\n")
        start = end + 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Путь к файлу", required=True)
    parser.add_argument(
        "-n", "--max-len", help="Максимальная длина строки", type=int, default=200
    )
    parser.add_argument("-d", "--folder", help="Путь к директории", type=str)

    args = parser.parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as file:
            string = file.read()
    except FileNotFoundError:
        print("Нет такого файла")
        sys.exit(-1)

    indexes = split_string(string, args.max_len)
    if len(indexes) == 0:
        print("Не могу разделить файл")
    else:
        if args.folder is not None:
            if not args.folder.endswith('\\'):
                args.folder = args.folder+'\\'
            try:
                bonus(string, indexes, args.folder)
                print_result(indexes, string)
            except FileNotFoundError:
                print(f"Вы указали директорию, которой не существует:{args.folder}")


def bonus(string: str, indexes: list[int], folder: str):
    start = 0
    for index, end in enumerate(indexes, 1):
        test_file = open(f'{folder}substring_{index}.txt', 'w')
        test_file.write(f"Substring: #{index}:\n{string[start:end]}\n")

        start = end + 1


if __name__ == '__main__':
    main()
