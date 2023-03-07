import os
import sys
from itertools import groupby


# функция проверяет размер файла
def file_size(filename: str) -> bool:
    file_size_content = os.path.getsize(filename)
    return 0 == file_size_content


# функция чтения файла
def read_file(file_name: str) -> list[str]:
    try:
        file = open(file_name, 'r', encoding='utf-8')
    except FileNotFoundError:
        print("This file is not exist:(")
    else:
        file_size_status = file_size(file_name)
        if file_size_status:
            file_content = file.readlines()
            return file_content
        else:
            print("This file is empty")


# функция печати подстрок
def print_substrings(file: str, split_number: int, status: bool) -> None:
    list_string = split_string(file, split_number, status)
    i = 0
    for string in list_string:
        print(f"Substring #{i + 1}:\n" + string)
        i += 1


# функция удаляет перенос строки и записывает получившиеся элементы в список
def delete_symbols(list_strings: list[str]) -> list[str]:
    temp_list = []
    for read_string in list_strings:
        if -1 != read_string.find('\n'):
            read_string = read_string.replace('\n', '')

        temp_list.append(read_string)
    return temp_list


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


# функция считает количество символов в элементах списка
def count_sum_symbols(input_list: list[str]) -> list[int]:
    list_sum_symbols = []

    for list_element in input_list:
        list_sum_symbols.append(len(list_element))

    return list_sum_symbols


# Функция удаляет спец. символы которые были добавлены в пробел тега
def delete_special_symbols(input_list: list[str]) -> list[str]:
    input_list = [element.replace("&", " ") for element in input_list]
    return input_list


# Функция, которая создает файлы
def create_files(directory: str, input_list: list[str]) -> None:
    if os.path.isdir(directory):

        i = 0
        for string in input_list:
            filepath = os.path.join(directory, f"substring_{i}.txt")
            temp_file = open(filepath, "w+")
            temp_file.write(string)
            temp_file.close()
            i += 1
    else:
        print("This -d param is not directory or so directory is not exist")


# функция для разделения строк
def split_string(file: str, split_number: int, status: bool) -> list[str]:
    list_strings = read_file(file)

    if not status:
        new_list = delete_symbols(list_strings)
    else:
        new_list = list_strings

    read_string = ' '.join(new_list)
    read_string_new = find_tags(read_string)

    new_list = read_string_new.split()
    list_sum_symbols = count_sum_symbols(new_list)
    temp_list_string = []

    if max(list_sum_symbols) > split_number:
        print("Impossible to divide into substrings")
        print("Your word is too big\nTry to choose bigger split number")

    else:
        i = 0
        j = 0
        current_index = 0

        while i < split_number:
            i += 1
            max_element_pos = split_number * i + (i - 1)

            try:
                if ' ' == read_string_new[max_element_pos]:

                    if not status:

                        temp_list_string.append(read_string_new[split_number * j + j:max_element_pos])
                    else:
                        if -1 != read_string_new.find("score", split_number * j + j, max_element_pos):
                            index_symbol_end = read_string_new.find("\n", split_number * j + j)
                            temp_list_string.append(read_string_new[split_number * j + j:index_symbol_end])
                        else:
                            temp_list_string.append(read_string_new[split_number * j + j:max_element_pos])

                current_index = read_string_new.find(" ", split_number * j + j)

            except IndexError:
                temp_list_string.append(read_string_new[current_index:len(read_string_new)])

            else:
                index_begin_space = read_string_new.rfind(' ', split_number * j + j,
                                                          max_element_pos + 1)
                index_end_space = read_string_new.find(' ',
                                                       max_element_pos)

                if ' ' == read_string_new[split_number * j + j] or 0 == j:
                    if not status:
                        temp_list_string.append(read_string_new[split_number * j + j:index_begin_space + 1])
                        temp_list_string.append(read_string_new[index_begin_space + 1:index_end_space + 1])

                    else:
                        if -1 != read_string_new.find("score", split_number * j + j, index_end_space + 1):
                            index_symbol_end = read_string_new.find("\n", split_number * j + j)
                            temp_list_string.append(read_string_new[split_number * j + j:index_symbol_end + 1])

                            index_symbol_end2 = read_string_new.find("\n", index_symbol_end + 1)

                            if index_symbol_end2 > index_end_space:
                                temp_list_string.append(read_string_new[index_symbol_end + 1:index_symbol_end2 + 1])
                            else:
                                temp_list_string.append(read_string_new[index_symbol_end + 1:index_end_space + 1])
                        else:
                            temp_list_string.append(read_string_new[split_number * j + j:index_begin_space + 1])
                            temp_list_string.append(read_string_new[index_begin_space + 1:index_end_space + 1])

                else:
                    if not status:
                        temp_list_string.append(read_string_new[current_index + 1:index_end_space + 1])
                    else:
                        if -1 != read_string_new.find("score", current_index + 1, index_end_space + 1):
                            index_symbol_end = read_string_new.find("\n", current_index + 1)
                            temp_list_string.append(read_string_new[current_index + 1:index_symbol_end + 1])
                        else:
                            temp_list_string.append(read_string_new[current_index + 1:index_end_space + 1])

            j += 1

    temp_list_string = [element for element, _ in groupby(temp_list_string)]

    try:
        temp_list_string.remove('')
    except ValueError:
        pass

    temp_list_string = delete_special_symbols(temp_list_string)
    return temp_list_string


# Про пользовательский код на питоне
# Тут что-то не очень понятно, в примере - типа "lambda line: 'score' not in line" -
# убрать все строки (в смысле разделенный по \n) в которых есть слово score,
# но по сути эта лямбда функция как бы осуществляет только проверку: есть ли 'score' в заданной строке
# если есть - вернет False, нет - True,
# но так как мы получаем вот физическую строку с кодом, то мы никакого значения и не получим, а просто сможем выполнить
# код, который задал пользователь в качестве аргумента
# И вот на этом моменте непонятно, как введенный в примере код уберет все строки?
# Или мой код должен сам это сделать, а введеный код как в примере - просто проверяет условие?
# Если так - то как я пойму, что мне вернется из кода пользователя, если мы можем выполнить пользовательский код
# только при помощи `eval` или `exec` - но никакого возврата мы в таком случае не получим
# Возможно, есть и другие варианты кроме этих?

# Поэтому оставлю это пока так до дальнейшего ответа с ревью:)

# Хотя сначала хотелось сделать что-то типа такого:

# i=0
# for element in list_string:
# code_string=lambda line: 'score' not in line (ну тут бы был польз. код)
# status=(code_string(element))
# if False==status:
# list_string.pop(i)
# i+=1


# Пока считаю, что пользователь сам знает, чего он хочет и вводит код в качестве параметра,
# а мой код его исполняет

def begin_code(input_list: list[str], input_code: str) -> bool:
    for element in input_list:
        code_string = eval(input_code)
        status = (code_string(element))
        return status


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

    if -1 != argv_f:
        status = False

        if -1 != argv_l:
            status = True
        else:
            status = False

        if -1 != argv_n:
            split_number = int(sys.argv[argv_n + 1])
            print_substrings(sys.argv[argv_f + 1], split_number, status)
        else:
            split_number = 200
            print_substrings(sys.argv[argv_f + 1], split_number, status)

        list_strings = split_string(sys.argv[argv_f + 1], split_number, status)

        if -1 != argv_r:
            status_code = begin_code(list_strings, sys.argv[argv_r + 1])
        else:
            pass

        if -1 != argv_d:
            create_files(sys.argv[argv_d + 1], list_strings)
        else:
            pass
    else:
        print("Param -f is required")


if __name__ == '__main__':
    main()
