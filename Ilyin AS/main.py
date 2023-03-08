import sys


def main(args: list[str]) -> int:
    num_n = 200
    if len(args) < 2:
        print(f"Not enough {len(args)} required > 2")
        return -1
    elif len(args) > 5:
        print(f"To much {len(args) - 1} required < 5")
        return -1
    for i in range(len(args)):
        if args[i] == '-f':
            file_name = args[i + 1]
        elif args[i] == '-n':
            num_n = int(args[i + 1])
    check_txt(file_name)
    words = read_file(file_name)
    divide_string(words, num_n)


# read file
def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding='utf-8') as r:
            return r.read()
    except:
        print(f"Файл не найден")
        sys.exit(-1)


# divide string
def divide_string(string: str, n: int):
    j = 1
    delete_list = []
    new_list = string.split(" ")

    for i in range(len(new_list)):
        if ("@" in new_list[i]) and (":" not in new_list[i]):
            nick = new_list[i]
            x = i
            while True:
                if ":" in new_list[x + 1]:
                    nick = nick + " " + new_list[x + 1]
                    new_list[i] = nick
                    delete_list.append(new_list[x + 1])
                    break
                else:
                    nick = nick + " " + new_list[x + 1]
                    delete_list.append(new_list[x + 1])
                    x += 1

    for i, word in enumerate(delete_list):
        new_list.remove(word)

    for i in range(len(new_list)):
        if len(new_list[i]) > n:
            print(f"Невозможно разделить строки")
            return -1

    pr_str = new_list[0]

    for i in range(len(new_list) - 1):
        if len(pr_str) + len(new_list[i + 1]) < n - 1:
            pr_str = pr_str + ' ' + new_list[i + 1]
        else:
            print_str(pr_str, j)
            pr_str = new_list[i + 1]
            j += 1

    print_str(pr_str, j)


# print devided strings
def print_str(string: str, i: int):
    print(f"Substring #{i}:")
    print(string)


# check .txt in argc
def check_txt(args: str):
    if len(args) > 4:
        if (args[-4] != ".") or (args[-3] != "t") or (args[-2] != "x") or (args[-1] != "t"):
            print(f"Недопустимое разрешение файла, ожидалось .txt")
            sys.exit(-1)
    else:
        print(f"Имя файла введено некорректно")
        sys.exit(-1)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
