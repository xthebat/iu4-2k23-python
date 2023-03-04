import os.path
import sys


def arg_file(args: list[str]) -> str | None:
    try:
        index_f = args.index('-f')
    except ValueError:
        print('Вы не ввели параметр файла -f', end='\n\n')
        return None

    if index_f == len(args) - 1:
        print('Не указано название файла', end='\n\n')
        return None

    if os.path.splitext(args[index_f + 1])[1] == '.txt':
        return args[index_f + 1]
    else:
        print('Некорректное название файла', end='\n\n')
        return None


def symbol_file(args: list[str]) -> int | None:
    try:
        index_sy = args.index('-n')
    except ValueError:
        print('Вы не ввели параметр количества символов. Принято значение по умолчанию', end='\n\n')
        return 200

    if index_sy == len(args) - 1:
        print('Вы не ввели параметр количества символов. Принято значение по умолчанию', end='\n\n')
        return 200

    if args[index_sy + 1].isdigit() and int(args[index_sy + 1]) > 0:
        return int(args[index_sy + 1])
    else:
        print('Некорректное значение длины', end='\n\n')
        return None


def all_string(args: list[str]) -> bool:
    try:
        args.index('-l')
    except ValueError:
        return False
    return True


def direct_file(args: list[str]) -> str | None:
    try:
        direct_index = args.index('-d')
    except ValueError:
        print('Не задан путь директории', end='\n\n')
        return None
    
    if direct_index == len(args) - 1:
        print('Не задан путь директории', end='\n\n')
        return None

    return args[args.index('-d') + 1]


def line_from_file(args: list[str]) -> str | None:
    name_file = arg_file(args)
    if name_file is None:
        return None
    with open(name_file, "rt", encoding="utf-8") as file:
        return file.read()


def str_to_line(in_str: str, limit: int) -> list[str]:
    if in_str is None:
        return []
    list_string = []
    if limit is None:
        return []
    space_index = 0
    counter = 0
    tags_on = False
    last_final = 0
    all_lines = all_string(sys.argv)
    for i in range(len(in_str)):
        counter += 1

        if all_lines:
            if in_str[i] == '-':
                tags_on = True
            if in_str[i] == '\n' and tags_on:
                tags_on = False
        else:
            if in_str[i] == '@':
                tags_on = True

            if in_str[i] == ':' and tags_on:
                tags_on = False

        if in_str[i] in (' ', '\n') and not tags_on:
            space_index = i

        # if counter >= limit and (i - space_index) < limit:
        if (i - space_index) < limit <= counter:
            list_string.append(in_str[last_final:space_index])
            last_final = space_index + 1
            counter = 0 + i - space_index  # добавляем то, что уже успели пройти в поисках пробела

    list_string.append(in_str[last_final:])
    return list_string


def check_list(list_string: list[str], limit: int) -> list[str] | None:
    if limit is None:
        return None

    for i in list_string:
        if len(i) > limit:
            print('Строку невозможно разбить, возьмите значение ограничения больше', end='\n\n')
            return None

    return list_string


def print_list(list_string: list[str]):
    if list_string is None:
        return None
    for i, val in enumerate(list_string):
        print(f"Substring #{i}")
        print(val, end='\n\n')


def print_list_in_file(list_string: list[str]) -> None:
    if list_string is None:
        return None
    direct = direct_file(sys.argv)
    for i, val in enumerate(list_string):
        name_file = os.path.join(direct, f'substring_{str(i)}.txt')
        with open(name_file, 'wt') as out_file:
            out_file.write(val + '\n')


def main():
    str_input = line_from_file(sys.argv)
    limit = symbol_file(sys.argv)
    list_out = str_to_line(str_input, limit)

    if direct_file(sys.argv) is None:
        print_list(check_list(list_out, limit))
    else:
        print_list_in_file(check_list(list_out, limit))


if __name__ == '__main__':
    main()
