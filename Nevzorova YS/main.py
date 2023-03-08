import sys

MIN_LEN_ARG = 3
MAX_LEN_ARG = 5

def main(args: list[str]) -> int:
    control_arg_len(args)
    tuple_flag = find_flags(args)
    control_type_file_txt(tuple_flag[0])
    all_words = reader(tuple_flag[0])
    changed_list = word_breaking(all_words, tuple_flag[1])
    make_and_print_words(changed_list, tuple_flag[1])
    return 1


# функция считывающая файл
def reader(path_file: str) -> str:
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            return file.read()
    except:
        print("Искомый файл не обнаружен")
        sys.exit(-1)


# обработка строки из файла
def word_breaking(args: str, n: int) -> list[str]:
    changed_list = glue_nicks(args)
    word_output_control(changed_list, n)
    return changed_list


# Проверка длины параметра
def control_arg_len(args: list[str]):
    if len(args) < MIN_LEN_ARG:
        print(f"Не достаточно аргументов параметра = {len(args) - 1}, необходимо > {MIN_LEN_ARG - 2}")
        sys.exit(-1)
    elif len(args) > MAX_LEN_ARG:
        print(f"Слишком большая длина параметра = {len(args) - 1}, необходимо < {MAX_LEN_ARG}")
        sys.exit(-1)


# ищем флаги -f -n
def find_flags(args: str) -> tuple:
    n = 200
    for i, val in enumerate(args):
        if val == '-f':
            path_file = args[i + 1]
        elif val == '-n':
            n = int(args[i + 1])
    return (path_file, n)


# проверка разрешения файла на .txt
def control_type_file_txt(args: str):
    if len(args) >= 5:
        if not args.endswith('.txt'):
            print("Неверное разрешение файла, введите .txt")
            sys.exit(-1)
    else:
        print("Некорректное имя файла")
        sys.exit(-1)


# склейка никнеймов
def glue_nicks(args: str) -> list:
    changed_list = args.split(" ")
    list_delete_words = []
    for i, val in enumerate(changed_list):
        if "@" in val and ":" not in val:
            nickname = val
            a = i
            while True:
                list_delete_words.append(changed_list[a + 1])
                if ":" not in changed_list[a + 1]:
                    nickname += " " + changed_list[a + 1]
                    a += 1
                else:
                    nickname += " " + changed_list[a + 1]
                    changed_list[a] = nickname
                    break

    for i, word in enumerate(list_delete_words):
        changed_list.remove(word)

    return changed_list


# проверка на делимость строки
def word_output_control(my_list: tuple, n: int):
    for i, val in enumerate(my_list):
        if len(val) > n:
            print(f"Невозможно разделить на подстроки")
            sys.exit(-1)


# склейка слов для вывода подстроки
def make_and_print_words(my_list: list[str], n: int):
    a = 1
    glued_string = my_list[0]
    for i in range(len(my_list) - 1):
        if len(glued_string) + len(my_list[i + 1]) < n - 1:
            glued_string += ' ' + my_list[i + 1]
        else:
            printing_string(a, glued_string)
            glued_string = my_list[i + 1]
            a += 1
    printing_string(a, glued_string)


# вывод полученной подстроки
def printing_string(i: int, args: str):
    print(f"Substring #{i}:\n{args}")


if __name__ == '__main__':
    sys.exit(main(sys.argv))

