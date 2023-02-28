import sys


def main(args: list[str]) -> int:
    control_len(args)
    list_flag = find_flags(args)
    control_txt(list_flag[0])
    all_words = reader(list_flag[0])
    changed_list = word_breaking(all_words, list_flag[1])
    make_and_print_words(changed_list, list_flag[1])


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
def control_len(args: str):
    if len(args) < 2:
        print(f"Не достаточно аргументов параметра = {len(args)}, необходимо > 2")
        return -1
    elif len(args) > 5:
        print(f"Слишком большая длина параматра = {len(args) - 1}, необходимо < 5")
        return -1


# ищем флаги -f -n
def find_flags(args: str):
    n = 200
    for i in range(len(args)):
        if args[i] == '-f':
            path_file = args[i + 1]
        elif args[i] == '-n':
            n = int(args[i + 1])
    return [path_file, n]


# проверка разрешения файла на .txt
def control_txt(args: str):
    if len(args) >= 5:
        if args[-1] != "t" or args[-2] != "x" or args[-3] != "t" or args[-4] != ".":
            print("Неверное разрешение файла, введите .txt")
            return -1
    else:
        print("Некорректное имя файла")
        return -1


# склейка никнеймов
def glue_nicks(args: str) -> list:
    changed_list = args.split(" ")
    list_delete_words = []
    for i in range(len(changed_list)):
        if "@" in changed_list[i] and ":" not in changed_list[i]:
            nickname = changed_list[i]
            a = i
            while True:
                if ":" not in changed_list[a + 1]:
                    nickname = nickname + " " + changed_list[a + 1]
                    list_delete_words.append(changed_list[a + 1])
                    a += 1
                else:
                    nickname = nickname + " " + changed_list[a + 1]
                    changed_list[i] = nickname
                    list_delete_words.append(changed_list[a + 1])
                    break

    for i, word in enumerate(list_delete_words):
        changed_list.remove(word)

    return changed_list


# проверка на делимость строки
def word_output_control(my_list: list[str], n: int):
    for i in range(len(my_list)):
        if len(my_list[i]) > n:
            print(f"Невозможно разделить на подстроки")
            sys.exit(-1)


# склейка слов для вывода подстроки
def make_and_print_words(my_list: list[str], n: int):
    a = 1
    glued_string = my_list[0]
    for i in range(len(my_list) - 1):
        if len(glued_string) + len(my_list[i + 1]) < n - 1:
            glued_string = glued_string + ' ' + my_list[i + 1]
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
