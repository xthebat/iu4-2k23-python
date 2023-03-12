import os
import sys


# функция чтения файла
def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()
            return file_content

    except FileNotFoundError:
        print("This file is not exist:(")
        exit(-1)


# функция печати подстрок
def print_temp_strings(file: str, split_number: int, status: bool) -> None:
    list_string = split_string(file, split_number, status)
    i = 0
    for string in list_string:
        print(f"Substring #{i + 1}:\n" + string)
        i += 1


# функция поиска тегов и замены пробелов в них
def find_tags(input_string: str) -> str:
    index_element = 0

    while index_element < len(input_string):
        index_begin_tag = input_string.find('@', index_element)
        index_end_tag = input_string.find(':', index_begin_tag)

        if -1 != index_begin_tag and -1 != index_end_tag:
            index_space = input_string.find(' ', index_begin_tag, index_end_tag + 1)
            if -1 != index_space:
                temp_list = list(input_string)
                temp_list[index_space] = '&'
                input_string = "".join(temp_list)

        index_element += 1
    return input_string


# Функция, которая создает файлы
def create_files(directory: str, input_list: list[str]) -> None:
    if os.path.isdir(directory):

        i = 0
        for string in input_list:
            filepath = os.path.join(directory, f"temp_string_{i}.txt")
            with open(filepath, "w+", encoding="utf-8") as file:
                file.write(string)
            i += 1
    else:
        print("This -d param is not directory or so directory is not exist")


def split_string(file: str, split_number: int, status: bool) -> list[str]:
    temp_read_strings = read_file(file)
    read_strings = find_tags(temp_read_strings)

    list_strings = read_strings.strip().split('\n')

    temp_list_strings = []
    for string in list_strings:
        if "score" in string and status:

            if len(string) > split_number:
                print("Impossible to divide into temp_strings")
                print("Your temp_string is too big\nTry to choose bigger split number")
                exit(-1)

            else:
                temp_list_strings.append(string + "\n")
                continue

        temp_string = string.split(" ")
        for symbols in temp_string:
            if len(symbols) > split_number:
                print("Impossible to divide into temp_strings")
                print("Your temp_string is too big\nTry to choose bigger split number")
                exit(-1)

            else:
                temp_list_strings.append(symbols)
        temp_list_strings.append("\n")

    temp_string = ""
    collect_list = []
    temp_list = []

    for string in temp_list_strings:
        if len(string) + len(temp_string) <= split_number:
            temp_list.append(string + " ")
            temp_string = " ".join(temp_list)
            continue
        elif string == '\n':
            temp_list.append(string)
            temp_string = " ".join(temp_list)
            continue

        collect_list.append(temp_string)
        temp_string = string
        temp_list.clear()
        
    if temp_string != '':
        collect_list.append(temp_string)

    collect_list = [element.replace("&", " ") for element in collect_list]
    return collect_list


def begin_lambda_code(input_list: list[str], condition: str) -> list[str]:
    user_code = eval(condition)
    list_cond = list(filter(user_code, input_list))
    return list_cond


def main() -> None:
    argv_f = -1
    argv_n = -1
    argv_d = -1
    argv_r = -1
    argv_l = -1
    try:
        argv_f = sys.argv.index('-f')
    except ValueError:
        pass

    try:
        argv_d = sys.argv.index('-d')
    except ValueError:
        pass

    try:
        argv_n = sys.argv.index('-n')
    except ValueError:
        pass

    try:
        argv_r = sys.argv.index('-r')
    except ValueError:
        pass

    try:
        argv_l = sys.argv.index('-l')
    except ValueError:
        pass

    if -1 == argv_f:
        print("Param -f is required")
        exit(-1)

    status = -1 != argv_l
    split_number = int(sys.argv[argv_n + 1]) if -1 != argv_n else 200
    list_strings = split_string(sys.argv[argv_f + 1], split_number, status)

    if -1 != argv_r:
        list_strings = begin_lambda_code(list_strings, sys.argv[argv_r + 1])
    else:
        pass

    if -1 != argv_d:
        create_files(sys.argv[argv_d + 1], list_strings)
    else:
        pass

    print_temp_strings(sys.argv[argv_f + 1], split_number, status)


if __name__ == '__main__':
    main()
