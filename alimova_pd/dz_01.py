import sys


def arg_file(args: list[str]) -> str:
    try:
        index_f = args.index('-f')
    except ValueError:
        print('Вы не ввели параметр файла -f')
        return 'ValueError'
    try:
        args[index_f + 1].index('.txt')
    except ValueError:
        print('Некорректное название файла')
        return 'ValueError'
    return args[index_f + 1]


def symbol_file(args: list[str]) -> int:
    try:
        index_sy = args.index('-n')
    except ValueError:
        print('Вы не ввели параметр количества символов. Принято значение по умолчанию\n')
        return 200
    if args[index_sy + 1].isdigit() and int(args[index_sy + 1]) > 0:
        return int(args[index_sy + 1])
    else:
        print('Некорректное значение длины')
        return -1


def all_string(args: list[str]) -> bool:
    try:
        args.index('-l')
    except ValueError:
        return False
    return True


def direct_file(args: list[str]) -> str:
    try:
        args.index('-d')
    except ValueError:
        print('Не задан путь директории')
        return 'Error'
    return args[args.index('-d') + 1]


def line_from_file(args: list[str]):
    name_file = arg_file(args)
    if name_file == 'ValueError':
        return 'ValueError'
    with open(name_file, "rt", encoding="utf-8") as file:
        str_1 = file.read()
        # print(str_1)

        return str_1


def str_to_line(in_str: str) -> list[str]:
    if in_str == 'ValueError':
        return []
    spisok = []
    limit = symbol_file(sys.argv)
    if limit < 1:
        return []
    probel = 0  # индекс последнего пробела
    counter = 0  # счетчик новой строки
    flag = False
    last_final = 0
    all_lines = all_string(sys.argv)
    for i in range(len(in_str)):
        counter += 1

        if all_lines:
            if in_str[i] == '-':
                flag = True
            if in_str[i] == '\n' and flag:
                flag = False
        else:
            if in_str[i] == '@':
                flag = True

            if in_str[i] == ':' and flag:
                flag = False

        if in_str[i] in (' ', '\n') and not flag:
            probel = i

        # if counter >= limit and (i - probel) < limit:
        if (i - probel) < limit <= counter:
            spisok.append(in_str[last_final:probel])
            last_final = probel + 1
            counter = 0 + i - probel  # добавляем то, что уже успели пройти в поисках пробела

    spisok.append(in_str[last_final:])
    return spisok


def check_spisok(spisok: list[str]):
    limit = symbol_file(sys.argv)
    if limit < 1:
        return []
    flag = False
    for i in spisok:
        if len(i) > limit:
            flag = True

    if flag:
        print('Строку невозможно разбить, возьмите значение ограничения больше')
        return []
    return spisok


def print_list(spisok: list[str]):
    if len(spisok) == 0:
        return 'ValueError'
    for i in range(len(spisok)):
        print(f"Substring #{i}")
        print(spisok[i])
        print()


def print_list_in_file(spisok: list[str]) -> str:
    if len(spisok) == 0:
        return 'ValueError'
    direct = direct_file(sys.argv)
    for i in range(len(spisok)):
        name_file = direct + '\\substring_' + str(i) + '.txt'
        with open(name_file, 'wt') as out_file:
            out_file.write(spisok[i] + '\n')


def main():
    str_input = line_from_file(sys.argv)
    list_out = str_to_line(str_input)

    if direct_file(sys.argv) == 'Error':
        print_list(check_spisok(list_out))
    else:
        print_list_in_file(list_out)


if __name__ == '__main__':
    main()
