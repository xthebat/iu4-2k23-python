import sys
import os
import re
import glob


# считывание параметров и проверка их на корректность
def args_input(args: list[str]) -> list[str, int, bool, str]:
    max_number = 200
    params = {}
    for cnt, arg in enumerate(args):
        if arg == '-f' or arg == '-n' or arg == '-d':
            params[arg] = args[cnt + 1]
        elif arg == '-l':
            params[arg] = True

    if '-f' in params:
        if params['-f'] not in os.listdir():
            print("Error: file isn't in directory")
            return []
        elif not params['-f'].endswith("txt"):
            print("Error: wrong file format, not txt")
            return []
        file_path = params['-f']
    else:
        print("Error: No parameter -f")
        return []

    if '-n' in params:
        if params['-n'].isdigit():
            max_number = int(params['-n'])
        else:
            print("Error: invalid -n argument")
            return []
    l_param = '-l' in params
    output_path = None
    if '-d' in params:
        if not params['-d'].endswith('/'):
            print("Error: -d argument incorrect")
            return []
        if not os.path.isdir(params['-d']):
            os.makedirs(params['-d'])
        output_path = params['-d']
    return [file_path, max_number, l_param, output_path]


# функция по разбитию строки на подстроки
def make_substrings(file_path: str, max_n: int, l_param: bool) -> list[list[str]]:
    text_split = input_from_file(file_path, max_n, l_param)
    start_index, end_index = 0, 0
    substrings, temp_n, last_appended_index = [], 0, 0

    for part in text_split:
        temp_n += len(part)
        if temp_n > max_n:  # длина подстроки больше максимальной, разделяем по последнему конечному индексу
            substrings.append(text_split[start_index:end_index])
            start_index = end_index
            last_appended_index = end_index
            temp_n = len(part)
            end_index += 1
        elif temp_n == max_n:  # длина подстроки равна максимальной
            end_index += 1
            last_appended_index = end_index
            substrings.append(text_split[start_index:end_index])
            start_index = end_index
            temp_n = 0
        else:
            end_index += 1
    if last_appended_index != end_index:
        substrings.append(text_split[start_index:end_index])
    return substrings


# функция обработки файла с входной строкой
def input_from_file(file_path: str, max_n: int, l_param: bool) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        text = file.read()
        text_split = re.split(r"(\s)", text)  # разбиваем на пробелы и \n с их сохранением
    join_user_tag(text_split)
    if l_param:
        join_user_score(text_split)
    if check_n_size(text_split, max_n):
        return []
    return text_split


# функция, которая проверяет, можно ли разбить на подстроки с переданным значением -n
def check_n_size(text: list[str], max_n: int) -> bool:
    max_length = len(max(text, key=len))
    if max_n < max_length:
        print("Error: incorrect -n argument, value too small")
    return max_n < max_length


# функция, чтобы объединить каждый тег пользователя в один str
def join_user_tag(split_text: list[str]) -> None:
    found_tag = False
    tag_start = 0
    for counter, word in enumerate(split_text):
        if word.startswith('@'):  # нашли начало тега пользователя
            tag_start = counter
            found_tag = True
        if found_tag and word.endswith(':'):  # нашли конец тега пользователя
            found_tag = False
            tag_end = counter + 1
            split_text[tag_start: tag_end] = [''.join(split_text[tag_start: tag_end])]


# функция, чтобы объединить каждый новый score пользователя в str
def join_user_score(split_text: list[str]) -> None:
    for counter, word in enumerate(split_text):
        if word == "-":
            score_start = counter
            score_end = split_text.index('\n', counter) + 1
            split_text[score_start: score_end] = [''.join(split_text[score_start: score_end])]


# функция отображения получившихся подстрок
def print_substrings(substrings: list[list[str]]) -> None:
    for i, sub_s in enumerate(substrings, start=1):
        print(f"Substring #{i}")
        for word in sub_s:
            print(word, end='')
        print()


# функция для записи подстрок в отдельные файлы
def subs_output_files(output_directory: str, substrings: list[list[str]]) -> None:
    # удаление предыдущих файлов из директории, чтобы не было лишних файлов, после запуска, где подстрок было больше
    previous_files = glob.glob(output_directory + "*")
    for file in previous_files:
        os.remove(file)

    for i, sub_s in enumerate(substrings, start=1):
        output_path = output_directory + "substring_" + str(i) + ".txt"
        with open(output_path, mode='w+', encoding='utf-8') as output_file:
            for word in sub_s:
                output_file.write(word)


def main(args: list[str]):
    value_of_args = args_input(args)
    if value_of_args:
        substrings = make_substrings(value_of_args[0], value_of_args[1], value_of_args[2])
        if substrings:
            print_substrings(substrings)
        if value_of_args[3]:
            subs_output_files(value_of_args[3], substrings)


if __name__ == '__main__':
    main(sys.argv)
