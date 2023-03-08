import os.path
import sys


def print_chunk(text_slice: str, k: int):
    print("Substring #", k, ":")
    print(f"{text_slice}")


def parse_parameter_f(args: list[str]) -> str:
    flag = 0
    if len(args) < 2:
        sys.exit("Not enough")
    for i in range(0, len(args), 1):
        if args[i] == '-f':
            adr = args[i+1]
            flag = 1
    if flag == 0:
        sys.exit("I have not -f parameter")
    if not os.path.exists(adr):
        sys.exit("File is not found!")
    return adr


def parse_parameter_n(args: list[str]) -> int:
    number = 200
    flag = 0
    for i in range(0, len(args), 1):
        if args[i] == '-n':
            number = int(args[i+1])
            flag = 1
    if flag == 0:
        print("I have not -n parameter, I will use 200")
    return number


def check_tag(text, i, last) -> int:
    at_symbol = -1
    for j in range(i, last + 1, 1):
        if text[j] == '@':
            at_symbol = j
    f_colon = -1
    if at_symbol != -1:
        for j in range(at_symbol, last + 1, 1):
            if text[j] == ':':
                f_colon = 1
    if f_colon == -1 and at_symbol != -1:
        last = at_symbol - 1
        if at_symbol == i:
            sys.exit("user-friendly")
    return last


def sub_reduction(text, i, last) -> int:
    while text[last] != ' ' and text[last + 1] != ' ' and text[last] != '\n' and text[last + 1] != '\n':
        last = last - 1
        if last < i:
            sys.exit("user-friendly")
    return last


def fun_del(text: str, kol: int):
    count = len(text)
    k = 1
    i = 0
    if count == 0:
        print("File is empty!")
    while i <= count - 1:
        if i + kol - 1 <= count - 1:
            last = i + kol - 1
        else:
            last = count - 1
        if last != count - 1:
            last = sub_reduction(text, i, last)
        check_tag(text, i, last)
        text_slice = text[i:last + 1]
        print_chunk(text_slice, k)
        k = k + 1
        i = last + 1


def main() -> int:
    adr = parse_parameter_f(sys.argv)
    kol = parse_parameter_n(sys.argv)
    with open(adr, "rt", encoding='utf-8') as file:
        text = file.read()
    fun_del(text, kol)
    return 0


if __name__ == '__main__':
    sys.exit(main())
