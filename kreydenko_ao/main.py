import sys
import os
import re


# считывание параметров и проверка их на корректность
def args_input() -> tuple[str, int]:
    error = False
    max_number = 200
    args = sys.argv
    params = {}
    for i in range(1, len(args), 2):
        params[args[i]] = args[i + 1]
    if '-f' in params:
        if params['-f'] not in os.listdir():
            print("Error: file isn't in directory")
            return None
        elif params['-f'][len(params['-f']) - 3:] != "txt":
            print("Error: wrong file format, not txt")
            return None
    else:
        print("Error: No parameter -f")
        return None

    if '-n' in params:
        try:
            max_number = int(params['-n'])
        except ValueError:
            print("Error: invalid -n argument")
            return None
    return params['-f'], max_number


# функция по разбитию строки на подстроки
def make_substrings(file_path: str, max_n: int) -> list[list[str]]:
    file = open(file_path, encoding='utf-8')
    text = file.read()
    text_split = re.split("( |\n)", text)  # разбиваем на пробелы и \n с их сохранением
    join_user_tag(text_split)
    if check_n_size(text_split, max_n):
        return None
    start_index = 0
    end_index = 0
    substrings = []
    temp_n = 0
    last_appended_index = 0

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
            substrings.append(text_split[start_index:end_index])
            start_index = end_index
            temp_n = 0
        else:
            end_index += 1
    if last_appended_index != end_index:
        substrings.append(text_split[start_index:end_index])
    file.close()
    return substrings


# функция, которая проверяет, можно ли разбить на подстроки с переданным значением -n
def check_n_size(text: list[str], max_n: int) -> bool:
    max_length = len(max(text, key=len))
    if max_n < max_length:
        print("Error: incorrect -n argument, value too small")
        return True
    else:
        return False


# функция, чтобы объединить каждый тег пользователя в один str
def join_user_tag(array: list[str]) -> None:
    found_tag = False
    counter = 0
    for word in array:
        if array[counter][0] == '@':  # нашли начало тега пользователя
            start_index = counter
            found_tag = True
        if found_tag and array[counter][-1] == ':':  # нашли конец тега пользователя
            found_tag = False
            end_index = counter + 1
            array[start_index: end_index] = [''.join(array[start_index: end_index])]
        counter += 1


# функция отображения получившихся подстрок
def print_substrings(substrings: list[list[str]]) -> None:
    len_temp = 0
    for i in range(0, len(substrings)):
        print(f"Substring #{i + 1}")
        for word in substrings[i]:
            print(word, end='')
        print('\n')


def main():
    args = args_input()
    if args:
        substirngs = make_substrings(args[0], args[1])
        if substirngs:
            print_substrings(substirngs)


if __name__ == '__main__':
    main()
