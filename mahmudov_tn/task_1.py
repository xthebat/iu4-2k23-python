import os
import sys

INDEX = 1


def output_substring(arguments, substrings):
    global INDEX
    for substring in substrings:
        if arguments['dir'] and os.path.exists(arguments['path']):
            with open(f"{arguments['dir']}\\substring_#{INDEX}.txt", 'w+') as file:
                file.write(substring.strip())
                INDEX += 1
                continue
        print(f'Substring #{INDEX}:\n{substring.strip()}')
        INDEX += 1


def work_string(arguments, string):
    substrings = []
    string_buff = ''
    words = string.split()
    for word in words:
        if 'score' in string and '@' in word:
            string_buff += f'{word} '
        elif 'score' in string and ':' in word:
            string_buff += f'{word} '
        elif len(string_buff) <= arguments['num']:
            string_buff += f'{word} '
            if len(string_buff) >= arguments['num']:
                substrings.append(string_buff)
                string_buff = ''
            elif word == words[len(words) - 1]:
                substrings.append(string_buff)
                string_buff = ''
        else:
            substrings.append(string_buff)
            string_buff = ''
    output_substring(arguments, substrings)


def work_file(arguments):
    with open(arguments['path'], 'r') as file:
        for string in file.read().split('\n'):
            if string:
                if arguments['row'] and 'score' in string:
                    output_substring(arguments, [string])
                    continue
                work_string(arguments, string)


def main():
    arguments = {
        'path': sys.argv[2],
        'num': int(sys.argv[4]) if '-n' in sys.argv else int(200),
        'row': True if '-l' in sys.argv else False,
        'dir': sys.argv[7] if '-d' in sys.argv else None
    }
    work_file(arguments)


if __name__ == '__main__':
    main()
