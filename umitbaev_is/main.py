import argparse
import os
import pathlib


def main():
    parser = argparse.ArgumentParser(description="Enter arguments")
    parser.add_argument('-n', '--number', type=int, default=200, help="Enter '-n' to set number of symvols i")
    parser.add_argument('-f', '--file', type=str, help="Enter path to file works only with '-f' in front")
    parser.add_argument('-d', '--direct', type=str, help="Enter path to file works only with '-f' in front")

    args = parser.parse_args()

    check_path(args.file)
    text = read_file(args.file)
    divide_index = divide_string(text, args.number)

    create_files(args.direct, divide_index, text)

    print_strings(divide_index, text)


def check_path(path):
    file = pathlib.Path(path)
    if not file.is_file() or not os.stat(path).st_size:
        print("No such file")
        exit(1)
    if not os.stat(path).st_size:
        print("File is empty")
        exit(1)


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def divide_string(text: str, max_number: int) -> list[int]:
    last_index = 0
    divide_index = []
    flag = False
    result_len = 0
    for index in range(len(text)):
        if text[index] == '@':
            flag = True
        if text[index] == ':':
            flag = False
        if not flag and text[index].isspace():
            if index - result_len > max_number:
                if last_index == 0 or last_index in divide_index:
                    return []
                divide_index.append(last_index)
                result_len = last_index
            else:
                last_index = index

    if len(text) - divide_index[-1] > max_number:
        divide_index.append(last_index)

    divide_index.append(len(text))
    return divide_index


def create_files(direct: str, divide_index: list[int], text: str):
    if direct is not None:
        if not direct.endswith('\\'):
            direct = direct + '\\'
        try:
            print_into_file(text, divide_index, direct)
        except FileNotFoundError:
            print(f"Вы указали директорию, которой не существует:{direct}")
            exit(1)


def print_into_file(text: str, divide_index: list[int], direct: str):
    start = 0
    for index, end in enumerate(divide_index, 1):
        test_file = open(f'{direct}substring_{index}.txt', 'w')
        test_file.write(f"Substring: #{index}:\n{text[start:end]}\n")

        start = end + 1


def print_strings(divide_index: list[int], string: str):
    start = 0
    for index, end in enumerate(divide_index, 1):
        print(f"Substring: #{index}:")
        print(string[start:end], "\n")
        start = end + 1


if __name__ == '__main__':
    main()
