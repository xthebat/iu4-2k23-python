import os.path
import sys


def find_d(args: list[str]):
    if len(args) >= 2:
        for index, it in enumerate(args):
            if (it == '-d') & (len(args) > index):
                return args[index + 1]
    return 0


def find_l(args: list[str]):
    if len(args) >= 2:
        for index, it in enumerate(args):
            if (it == '-l') & (len(args) > index):
                return args[index + 1]
    return 0


def find_n(args: list[str]):
    if len(args) >= 2:
        for index, it in enumerate(args):
            if (it == '-n') & (len(args) > index):
                return int(args[index + 1])
    else:
        print('Вы не указали параметр -l')
    return 200


def find_file(args: list[str]):
    if len(args) >= 2:
        for index, it in enumerate(args):
            if (it == '-f') & (len(args) > index):
                return args[index + 1]
    else:
        print('Вы не указали параметр -f')
    return 0


def read_file(filename: str, n: int):
    if os.path.getsize(filename) > 0:
        file = open(filename, 'r')
        string = file.read(n)
        inc = 1
        while len(string) > 0:
            print('Substring ', inc)
            inc = inc + 1
            print(string)
            string = file.read(n)
        file.close()
    else:
        print('file is empty(')


def main():
    print('dz_bat_1')
    n = find_n(sys.argv)
    filename = find_file(sys.argv)

    print('chosen file:', filename)
    print('string\'s length:', n)

    read_file(filename, n)

    pass


if __name__ == '__main__':
    main()
