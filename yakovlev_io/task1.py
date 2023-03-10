import sys
import os.path
import argparse


def parsing():
    parser = argparse.ArgumentParser(description='What the program does',)

    parser.add_argument('-f', type=str, dest='file', help='file path')
    parser.add_argument('-n', type=int, dest='num', help='count')
    parser.add_argument('-l', dest='line', help='str')

    args = parser.parse_args()
    return args


def verify_file(arg):
    if os.path.exists(arg.file) is False:
        print(f"{arg.file} not found")
        exit(404)


def substring(arguments):
    with open(arguments.file, 'r', encoding="utf-8") as file:
        tmp = file.read()
        i = 0
        while i < len(tmp) - 1:
            if tmp[i + arguments.num + 1] == ' ':
                ind = arguments.num
            else:
                ind = tmp[i:i + arguments.num].rfind(' ')

            print(tmp[i:i + ind + 1] + '\n')
            i += ind + 1

            if i + arguments.num >= len(tmp) - 1:
                print(tmp[i:] + '\n')
                break


def main(argv: list[str]):
    arguments = parsing()
    verify_file(arguments)
    substring(arguments)


if __name__ == '__main__':
    main(sys.argv)