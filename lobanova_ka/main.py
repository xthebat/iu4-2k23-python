import sys


def output(substrings: list[str]):  # функция вывода строк
    n = 0
    for n in range(len(substrings)):
        print(f"Substring #{n + 1}:")
        print(substrings[n], end="\n\n")


def slice(text, number):  # функция разбиения на подстроки
    words = text.split()
    start = 0  # начальное значение подстроки
    current_substring_len = 0  # длина подстроки
    substrings = []  # список подстрок
    substrings.append("")
    help = []
    is_tag = False  # флаг на тег
    i, n = 0, 0  # индексы списков
    delta = 0  # длина невошедшего слова
    for word in words:
        if delta == 0:
            current_substring_len += len(word) + 1  # +1, т.к. пробелы и \n
        else:
            current_substring_len += delta + len(word) + 1
            delta = 0
        # Ссылки и даты рассматриваются как слова, так как они пишутся слитно
        # Проверка на тег:
        if word.startswith('@'):
            is_tag = True

        if is_tag and not word.endswith(':'):
            continue

        if is_tag and word.endswith(':'):
            is_tag = False

        help.append("")
        help[i] = text[start: start + current_substring_len - 1]  # -1, т.к. последний добавленный "пробел" лишний

        if len(help[i]) <= number:
            substrings[n] = help[i]
        else:
            n += 1
            delta = len(help[i]) - len(help[i - 1])
            substrings.append("")
            start += current_substring_len - delta
            current_substring_len = 0
        i += 1
    if delta != 0:
        substrings[n] = text[start: start + delta]
        output(substrings)
    else:
        output(substrings)


def check_n(args: list[str]) -> int:
    n = 200
    i = 0
    no_n = False
    no_int_n = False
    for arg in args:
        arg_n = "-n" in args[i]
        if arg_n and i < len(args) - 1:
            if args[i + 1].isdigit():
                n = int(args[i + 1])
            else:
                no_int_n = True
        else:
            i += 1
            if i >= len(args) - 1:
                no_n = True
    if no_n == True:
        print('Не задан -n параметр, по умолчанию n = 200', end='\n\n')
    if no_int_n == True:
        print('Параметр -n задан неверно, по умолчанию n = 200', end='\n\n')
    return n


def check_f(args: list[str]) -> str:
    i = 0
    no_f = False
    no_txt_f = False
    for arg in args:
        arg_f = "-f" in args[i]
        if arg_f and i < len(args) - 1:
            if args[i + 1].endswith('.txt'):
                file = open(args[i + 1], encoding='utf-8')
                text = file.read()
                file.close()
            else:
                no_txt_f = True
        else:
            i += 1
            if i >= len(args) - 1:
                no_f = True
    if no_f == True:
        print('Не задан -f параметр')
        return -1
    if no_txt_f == True:
        print('Параметр -f задан не верно: ожидается .txt формат')
        return -1
    return text


def check_length_n(n: int, text: str):
    words = text.split()
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    if n < max_len:
        print("Задана недостаточная длина подстрок, невозможно разбить текст")
        return -1


def main(args: list[str]) -> int:
    n = check_n(args)
    text = check_f(args)
    check_length_n(n, text)
    slice(text, n)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
