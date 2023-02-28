import argparse
import os
import re
from typing import List, Any
import random
import string


class RuleInputError(Exception):
    Exception: Any


def parse_args():
    parser = argparse.ArgumentParser(description='Преобразование строк в подстроки')
    parser.add_argument('-f', '--filepath', type=str, required=True)
    parser.add_argument('-n', '--limit', type=int, default=200)
    parser.add_argument('-l', '--allow-splitting', action='store_true', default=False)
    parser.add_argument('-d', '--directory', type=str)
    parser.add_argument('-r', '--rule', type=str)
    return parser.parse_args()


args = parse_args()


def check_args():
    if not os.path.isfile(args.filepath):
        print(f'Указанного файла не существует по заданному пути ({args.filepath}). Поменяйте параметр -f.')
        exit(1)

    if args.directory is not None and \
            not os.path.isdir(args.directory):
        print(f'Указанной папки не существует по заданному пути ({args.directory}). Пытаемся создать новую.')
        try:
            os.mkdir(args.directory)
        except OSError:
            print("Не удалось создать папку по заданному пути. Поменяйте путь или название папки в параметре -d")
            exit(1)

    if args.limit <= 0:
        print(f'Лимит слишком мал. Исправьте параметр -n.')
        exit(1)


def file_read() -> str:
    with open(args.filepath, 'rb') as f:
        current_string = f.read()
        current_string = current_string.decode('utf-8', 'ignore')
        return current_string


def split_string_list_to_words(
        input_string: List[str], max_chars=args.limit, restrict_middle_splitting=args.allow_splitting) -> List[str]:
    substrings = []
    current_substring = ''

    for word in input_string:
        if len(current_substring) + len(word) <= max_chars:
            if restrict_middle_splitting is True:
                current_substring += word + '\n'
            if restrict_middle_splitting is False:
                current_substring += word + " "
        else:
            substrings.append(current_substring)
            if restrict_middle_splitting is True:
                current_substring = word + "\n"
            if restrict_middle_splitting is False:
                current_substring = word + " "
            continue
    substrings.append(current_substring)
    return substrings


def check_string_limiter_args(lines: List[str], limit=args.limit):
    for current_string in lines:
        if len(current_string) > limit:
            print("Невозможно разбить строку на подстроки. Лимит слишком мал. Исправьте параметр -n.")
            exit(1)


def divide_strings(
        file_string: str, restrict_middle_splitting=args.allow_splitting) -> List[str]:
    lines = file_string.splitlines()
    keyword = "".join(random.choice(string.printable) for x in range(10))

    for idx, current_line in enumerate(lines):
        if args.rule is None:
            break
        try:
            if eval(args.rule)(current_line):
                lines[idx] = keyword + lines[idx]
        except Exception as exc:
            print(f"Вы неверно указали строку кода. Измените параметр -r. "
                  f"Введённый код: {args.rule}. Ошибка, связанная с ним: {exc}")
            exit(1)

    if restrict_middle_splitting is False:
        substrings = []
        for x in lines:
            if keyword not in x:
                substrings.extend(x.split())
            else:
                substrings.append(x.strip(keyword))
        lines = substrings

    for idx, current_substring_part in enumerate(lines):
        if re.search('^@', lines[idx]) and re.search(':$', lines[idx + 1]):
            lines[idx] += f" {lines[idx + 1]}"
            lines[idx + 1] = ""

    substrings = [specific_substring for specific_substring in lines if specific_substring != ""]

    check_string_limiter_args(lines=substrings)

    substrings = split_string_list_to_words(input_string=substrings)

    return substrings


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

# -f file.txt -n 60 -d new_folder
# -f file.txt -n 60 -d new_folder
# -f file.txt -n 200 -l -r "lambda line: len(line) == 45"
# -f file.txt -n 10
# -f file.txt -n 200 -r "lambda line: line.startswith('-')"
