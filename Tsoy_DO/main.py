import sys
import os.path


def Fun_out(text_slice, k):
    print("Substring #", k, ":")
    print(f"{text_slice}")


def Check_f(args: list[str]) -> int:
    adr = 0
    if len(args) < 2:
        sys.exit("Not enough")
    if args[1] == "-f":
        adr = args[2]
    else:
        sys.exit("I have not -f parametr")

    if not os.path.exists(adr):
        sys.exit("File is not found!")
    return adr


def Check_n(args: list[str]) -> int:
    kol = 200
    if args[3] == "-n":
        kol = int(args[4])
    else:
        print("I have not -n parametr, I will use 200")
    return kol


def Check_tag(text, i, last):
    sobaka = -1
    for j in range(i, last+1, 1):
        if (text[j] == '@'):
            sobaka = j
    f_colon = -1
    if (sobaka != -1):
        for j in range(sobaka, last+1, 1):
            if (text[j] == ':'):
                f_colon = 1
    if f_colon == -1 and sobaka != -1:
        last = sobaka - 1
        if sobaka == i:
            sys.exit("user-friendly")


def Sub_reduction(text, i, last) -> int:
    while text[last] != ' ' and text[last+1] != ' ' and text[last] != '\n' and text[last+1] != '\n':
        last = last - 1
        if last < i:
            sys.exit("user-friendly")

    return last


def Fun_del(text: list[str], kol):
    count = len(text)
    k = 1
    i = 0
    if count == 0:
        print("File is empty!")

    while i <= count-1:
        if i+kol-1 <= count-1:
            last = i+kol-1
        else:
            last = count-1

        if last != count-1:
            last = Sub_reduction(text, i, last)

        Check_tag(text, i, last)

        text_slice = text[i:last+1]
        Fun_out(text_slice, k);
        k = k + 1
        i = last + 1


def main() -> int:
    adr = Check_f(sys.argv)
    kol = Check_n(sys.argv)

    file = open(adr, "rt", encoding='utf-8')
    text = file.read()
    file.close()

    Fun_del(text, kol)

    return 0


if __name__ == '__main__':
    sys.exit(main())