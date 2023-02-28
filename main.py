import sys


def main(args: list[str]) -> int:
    if len(args) < 2:
        print(f"Not enough {len(args)} required > 2")
        return -1
    file_name = args[2] if args[1] == "-f" else sys.exit(-1)
    check_txt(file_name)
    flag_num = args[-1]
    flag = args[-2]
    n = int(check_flag_n(flag, flag_num))
    words = read_file(file_name)
    work_file(words, n)


# read file
def read_file(file_name) -> str:
    with open(file_name, 'r', encoding='utf-8') as r:
        u = r.read()
        return u


# make some shiiiii..sh) flex, not cringe, cool code, yeap i've got
def work_file(str, n):
    j = int(1)
    delete_list = []
    new_str = str.split(' ')

    for i in range(len(new_str)):
        if ("@" in new_str[i]):
            new_str[i] = new_str[i] + " " + new_str[i + 1]
            delete_list.append(new_str[i + 1])

    for i in range(len(delete_list)):
        new_str.remove(delete_list[i])

    for i in range(len(new_str)):
        if (len(new_str[i]) > n):
            print("Невозможно разделить строки")
            sys.exit(1)

    pr_str = new_str[0]

    for i in range(len(new_str) - 1):
        if (len(pr_str) + len(new_str[i + 1]) < n - 1):
            pr_str = pr_str + ' ' + new_str[i + 1]
        else:
            print_str(pr_str, j)
            pr_str = new_str[i + 1]
            j += 1

    print_str(pr_str, j)


def print_str(str, i):
    print(f"Substring #{i}:")
    print(str)


# check .txt in argc
def check_txt(args):
    if ".txt" not in args:
        print("Недопустимое разрешение файла, ожидалось txt")
        sys.exit(-1)


# check -n NUMBER in argc
def check_flag_n(args, num) -> int:
    if "-n" not in args:
        return 200
    else:
        return num


if __name__ == '__main__':
    sys.exit(main(sys.argv))
