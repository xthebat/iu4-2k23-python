import os
import argparse


def write_file(filename, substring, index):
    with open(filename, 'w+', encoding='UTF8') as file:
        file.write(substring.strip())
        index += 1
    return index


def work_string(num, string):
    substrings = []
    string_buff = ''
    words = string.split()
    for word in words:
        if 'score' in string and '@' in word and ':' in word:
            string_buff += f'{word} '
        elif len(string_buff) <= num:
            string_buff += f'{word} '
            if len(string_buff) >= num:
                substrings.append(string_buff)
                string_buff = ''
            elif word == words[len(words) - 1]:
                substrings.append(string_buff)
                string_buff = ''
        else:
            substrings.append(string_buff)
            string_buff = ''
    return substrings


def parse_line(arguments):
    index = 1
    if not os.path.exists(arguments.path):
        print(f"File{arguments.path} not found!")
        exit()
    with open(arguments.path, 'r', encoding='UTF8') as file:
        for string in file.read().split('\n'):
            if not string:
                continue
            if arguments.row and 'score' in string:
                if arguments.dir and os.path.exists(arguments.path):
                    index = write_file(f"{arguments.dir}\\substring_#{index}.txt", substring, index)
                    continue
                print(f'Substring #{index}:\n{string.strip()}')
                index += 1
                continue
            substrings = work_string(arguments.num, string)
            for substring in substrings:
                if arguments.dir and os.path.exists(arguments.path):
                    index = write_file(f"{arguments.dir}\\substring_#{index}.txt", substring, index)
                    continue
                print(f'Substring #{index}:\n{substring.strip()}')
                index += 1


def main():
    arguments = argparse.ArgumentParser()
    arguments.add_argument("-f", type=str, dest="path")
    arguments.add_argument("-n", type=int, default=200, dest="num")
    arguments.add_argument("-l", action="store_true", dest="row")
    arguments.add_argument("-d", type=str, dest="dir")
    parse_line(arguments.parse_args())


if __name__ == '__main__':
    main()
