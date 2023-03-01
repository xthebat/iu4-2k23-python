from argparse import ArgumentParser, ArgumentError
import os
import re
from typing import List
import random
import string
from pathlib import Path

os.chdir(Path(__file__).parent)


def parse_args():
    parser = ArgumentParser(description='Преобразование строк в подстроки', exit_on_error=False)
    parser.add_argument('-f', '--filepath', type=str)
    parser.add_argument('-n', '--limit', type=int, default=200)
    parser.add_argument('-l', '--allow-splitting', action='store_true', default=False)
    parser.add_argument('-d', '--directory', type=str)
    parser.add_argument('-r', '--rule', type=str)

    return parser.parse_args()


def stop_script():
    os.system('pause')
    exit(1)


try:
    parse_args()
except ArgumentError:
    print("Указан неверный тип аргумента для одного из ключей. Перепроверьте их при запуске.")
    stop_script()

args = parse_args()


def check_args():
    if args.filepath is None:
        print("Не указан путь до файла. Измените параметр -f.")
        stop_script()

    if not os.path.isfile(args.filepath):
        print(f'Указанного файла не существует по заданному пути ({args.filepath}). Поменяйте параметр -f.')
        stop_script()

    if args.directory is not None and \
            not os.path.isdir(args.directory):
        print(f'Указанной папки не существует по заданному пути ({args.directory}). Пытаемся создать новую.')
        try:
            os.mkdir(args.directory)
        except OSError:
            print("Не удалось создать папку по заданному пути. Поменяйте путь или название папки в параметре -d")
            stop_script()

    if args.limit <= 0:
        print(f'Лимит слишком мал. Исправьте параметр -n.')
        stop_script()


def file_read() -> str:
    with open(args.filepath, 'rb') as f:
        current_string = f.read()
        current_string = current_string.decode('utf-8', 'ignore')
        return current_string


def split_string_list_to_words(
        input_strings: List[str], max_chars=args.limit, restrict_middle_splitting=args.allow_splitting) -> List[str]:
    result_list = []
    current_substring = ''

    for word in input_strings:
        if len(current_substring) + len(word) <= max_chars:
            current_substring += word + ("\n" if restrict_middle_splitting is True else " ")
        else:
            result_list.append(current_substring[:-1])
            current_substring = word + ("\n" if restrict_middle_splitting is True else " ")
            continue
    result_list.append(current_substring[:-1])
    return result_list


def check_string_limiter_args(lines: List[str], limit=args.limit):
    for current_string in lines:
        if len(current_string) > limit:
            print("Невозможно разбить строку на подстроки. Лимит слишком мал. Исправьте параметр -n.")
            stop_script()


def divide_strings(
        file_string: str, restrict_middle_splitting=args.allow_splitting) -> List[str]:
    lines = file_string.splitlines()
    keyword = "".join(random.choice(string.printable) for _ in range(10))

    for idx, current_line in enumerate(lines):
        if args.rule is None:
            break
        try:
            if eval(args.rule)(current_line):
                lines[idx] = keyword + lines[idx]
        except Exception as exc:
            print(f"Вы неверно указали строку кода. Измените параметр -r."
                  f"\nВведённый код: {args.rule}."
                  f"\nОшибка, связанная с ним: {exc}")
            stop_script()

    if restrict_middle_splitting is False:
        substrings = []
        for x in lines:
            substrings.append(x.strip(keyword) if keyword in x else x.split())

        lines = substrings

    for idx, current_substring_part in enumerate(lines):
        if re.search('^@', lines[idx]) and re.search(':$', lines[idx + 1]):
            lines[idx] += f" {lines[idx + 1]}"
            lines[idx + 1] = ""

    result_list = [specific_substring for specific_substring in lines if specific_substring != ""]

    check_string_limiter_args(lines=result_list)

    result_list = split_string_list_to_words(input_strings=result_list)

    return result_list


def print_substrings(redacted_string_list: List[str]):
    for idx, substring in enumerate(redacted_string_list):
        print(f'Substring №{idx + 1}:\n{substring}')


def save_output_file(substrings: List[str], output_directory=args.directory):
    for idx, current_substring in enumerate(substrings):
        with open(f"{output_directory}/substring_{idx + 1}", "w", encoding='utf-8') as f:
            f.write(current_substring)
            f.close()


def main():
    check_args()
    cur_string = file_read()
    divided_strings = divide_strings(file_string=cur_string)
    print_substrings(divided_strings)
    if args.directory is not None:
        save_output_file(divided_strings)


if __name__ == '__main__':
    main()
