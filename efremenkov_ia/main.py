from argparse import ArgumentParser, ArgumentError
import os
import re
import sys


class PredicateError(Exception):
    pass


class InputArgumentError(Exception):
    pass


def parse_args(argv):
    parser = ArgumentParser(description='Преобразование строк в подстроки', exit_on_error=False)
    parser.add_argument('-f', '--filepath', type=str)
    parser.add_argument('-n', '--max-chars', type=int, default=200)
    parser.add_argument('-l', '--allow-splitting', action='store_true', default=False)
    parser.add_argument('-d', '--directory', type=str)
    parser.add_argument('-r', '--rule', type=str)

    return parser.parse_args(argv[1:])


def check_args(filepath: str, directory: str, max_chars: int):
    if filepath is None:
        raise FileNotFoundError("Не указан путь до файла. Измените параметр -f.")

    if max_chars <= 0:
        raise ValueError(f'Лимит слишком мал. Измените параметр -n.')

    if not os.path.isfile(filepath):
        raise FileNotFoundError(
            f'Указанного файла не существует по заданному пути ({filepath}). Измените параметр -f.')

    if directory is not None and \
            not os.path.isdir(directory):
        try:
            os.mkdir(directory)
        except OSError as e:
            raise e


def split_string_list_to_words(
        input_strings: list[str], max_chars: int, allow_splitting: bool) -> list[str]:
    result_list = []
    current_substring = ''

    for word in input_strings:
        if len(current_substring) + len(word) <= max_chars:
            current_substring += word + ("\n" if allow_splitting is True else " ")
        else:
            result_list.append(current_substring[:-1])
            current_substring = word + ("\n" if allow_splitting is True else " ")
            continue
    result_list.append(current_substring[:-1])
    return result_list


def check_string_limiter_args(lines: list[str], max_chars):
    for current_string in lines:
        if len(current_string) > max_chars:
            raise ValueError("Невозможно разбить строку на подстроки. Лимит слишком мал. Измените параметр -n.")


def read_file(filepath: str) -> list[str]:
    result_list = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            result_list.append(line.replace("\n", ""))
    return result_list


def divide_strings_from_file(allow_splitting: bool, filepath: str, rule: str, max_chars: int) -> list[str]:
    substring_list = read_file(filepath)
    keyword = "[this_is_a_keyword]"

    for idx, current_line in enumerate(substring_list):
        if rule is None:
            break
        try:
            predicate = eval(rule)
            condition = predicate(current_line)
        except Exception as e:
            raise PredicateError(f"Вы неверно указали строку кода. Измените параметр -r."
                                 f"\nВведённый код: {rule}.\nОшибка, связанная с ним: {e}")

        if condition and allow_splitting is False:
            substring_list[idx] = keyword + substring_list[idx]

    if allow_splitting is False:
        substring_list = [(x.strip(keyword) if keyword in x else x.split()) for x in substring_list]
        substring_list = [item for sublist in substring_list for item in sublist]

    for idx, current_substring_part in enumerate(substring_list):
        if current_substring_part is not None and idx < len(substring_list) - 1 \
                and re.search('^@', current_substring_part) and re.search(':$', substring_list[idx + 1]):
            substring_list[idx] += f" {substring_list[idx + 1]}"
            # noinspection PyTypeChecker
            substring_list[idx + 1] = None

    result_list = [specific_substring for specific_substring in substring_list if specific_substring is not None]

    check_string_limiter_args(result_list, max_chars)

    result_list = split_string_list_to_words(result_list, max_chars, allow_splitting)

    return result_list


def print_substrings(redacted_string_list: list[str]):
    for idx, substring in enumerate(redacted_string_list):
        print(f'Substring №{idx + 1}:\n{substring}')


def save_output_file(substrings: list[str], directory: str):
    for idx, current_substring in enumerate(substrings):
        with open(f"{directory}/substring_{idx + 1}", "w", encoding='utf-8') as f:
            f.write(current_substring)


def get_args(argv):
    try:
        args = parse_args(argv)
    except ArgumentError as e:
        raise InputArgumentError(f"\nНеверно указан параметр."
                                 f"\nНеправильный параметр: {e.argument_name} "
                                 f"\nОшибка, связанная с ним: {e}")
    return args


def main(args):
    check_args(args.filepath, args.directory, args.max_chars)

    result_substrings = divide_strings_from_file(args.allow_splitting, args.filepath, args.rule, args.max_chars)
    print_substrings(result_substrings)
    if args.directory is not None:
        save_output_file(result_substrings, args.directory)


if __name__ == '__main__':
    input_arguments = get_args(sys.argv)
    main(input_arguments)

'''
-f file.txt -n 60
-f file.txt -n 200 -l -r "lambda line: len(line) == 45"
-f file.txt -n 10
-f file.txt -n 200 -r "lambda line: line.startswith('-')"
'''
