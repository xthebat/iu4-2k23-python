import sys
import os.path


def main(args: list[str]) -> int:
    adr = 0

    if args[1] == "-f":
        adr = args[2]
    else:
        sys.exit("I have not -f parametr")

    kol = 200
    if args[3] == "-n":
        kol = int(args[4])
    else:
        print("I have not -n parametr")

    if not os.path.exists(adr):
        sys.exit("File is not found!")

    file = open(adr, "rt", encoding='utf-8')
    text = file.read()

    file.close()

    count = len(text)
    print("len = ", count)
    k = 1
    i = 0
    flag = 1

    if count == 0:
        print("File is empty!")
    # print(text[0:3])
    # print(text[1:4])
    while i <= count-1:
        if i+kol-1 <= count-1:
            last = i+kol-1
        else:
            last = count-1

        if last != count-1:
            while text[last] != ' ' and text[last+1] != ' ' and text[last] != '\n' and text[last+1] != '\n':
                last = last - 1
                if last < i:
                    sys.exit("user-friendly")

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

        text_slice = text[i:last+1]
        print("Substring #", k, ":")
        print(f"{text_slice}")
        k = k + 1
        i = last + 1

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))