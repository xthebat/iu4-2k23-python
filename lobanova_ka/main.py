import sys


def output_substrings(substrings: list[str]):
    for n in range(len(substrings)):
        print(f"Substring #{n + 1}:\n{substrings[n]}", end="\n\n")


def slice_text(text: str, number: int):
    words = text.split()
    start = 0
    current_substring_len = 0
    substrings: list[str] = [""]
    current_string: list[str] = [""]
    flag_tag = False
    i, n = 0, 0  # индексы списков
    delta = 0  # длина невошедшего слова
    for word in words:
        if delta == 0:
            current_substring_len += len(word) + 1  # +1, т.к. пробелы и \n
        else:
            current_substring_len += delta + len(word) + 1
            delta = 0

        if word.startswith('@'):
            flag_tag = True

        if flag_tag and not word.endswith(':'):
            continue

        if flag_tag and word.endswith(':'):
            flag_tag = False

        current_string.append("")
        current_string[i] = text[
                            start: start + current_substring_len - 1]
        # -1, т.к. последний добавленный "пробел" лишний

        if len(current_string[i]) <= number:
            substrings[n] = current_string[i]
        else:
            n += 1
            delta = len(current_string[i]) - len(current_string[i - 1])
            substrings.append("")
            start += current_substring_len - delta
            current_substring_len = 0
        i += 1
    if delta != 0:
        substrings[n] = text[start: start + delta]
        output_substrings(substrings)
    else:
        output_substrings(substrings)


def parsing_n(args: list[str]) -> int:
    n = 200
    i = 0
    flag_no_n = False
    flag_no_int_n = False
    for _ in args:
        arg_n = "-n" in args[i]
        if arg_n and i < len(args) - 1:
            if args[i + 1].isdigit():
                n = int(args[i + 1])
            else:
                flag_no_int_n = True
        else:
            i += 1
            if i >= len(args) - 1:
                flag_no_n = True
    if flag_no_n:
        print('Не задан -n параметр, по умолчанию n = 200', end='\n\n')
    if flag_no_int_n:
        print('Параметр -n задан неверно, по умолчанию n = 200', end='\n\n')
    return n


def parsing_f(args: list[str]) -> str:
    i = 0
    flag_no_f = False
    flag_no_txt_f = False
    for _ in args:
        arg_f = "-f" in args[i]
        if arg_f and i < len(args) - 1:
            if args[i + 1].endswith('.txt'):
                file = open(args[i + 1], encoding='utf-8')
                text = file.read()
                file.close()
            else:
                flag_no_txt_f = True
        else:
            i += 1
            if i >= len(args) - 1:
                flag_no_f = True
    if flag_no_f:
        print('Не задан -f параметр')
        sys.exit(-1)
    if flag_no_txt_f:
        print('Параметр -f задан не верно: ожидается .txt формат')
        sys.exit(-1)
    return text


def check_length_n(n: int, text: str):
    words = text.split()
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    if n < max_len:
        print("Задана недостаточная длина подстрок, невозможно разбить текст")
        sys.exit(-1)


def main(args: list[str]) -> int:
    n = parsing_n(args)
    text = parsing_f(args)
    check_length_n(n, text)
    slice_text(text, n)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
