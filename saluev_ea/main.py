import os
import argparse


class CantEvaluate(Exception):
    pass


# Function for working with arguments
def get_arguments():
    usage = '''2K23 Python Task #1'''

    arguments = argparse.ArgumentParser(
        description=usage
    )

    # The input string is contained in a file,the path to which is passed through
    # the command line argument with the -f key
    arguments.add_argument(
        "-f",
        type=str,
        dest="source",
        help="Source file"
    )

    # The maximum number of characters in a substring is specified by the command
    # line argument with the -n key (the default value of the parameter is 200)
    arguments.add_argument(
        "-n",
        type=int,
        default=200,
        dest="num",
        help="Max count symbols"
    )

    # The -l command line parameter, when specified, adds a correctness
    # to the split into substrings: it is not allowed to split "in the middle" of the string
    # indicating the new user's score
    arguments.add_argument(
        "-l",
        dest="lrz",
        action="store_true",
        help="Separation names"
    )

    # The -d command line parameter, when specified, saves the output substring
    # to different files in the directory specified in this parameter.
    # File names are specified in the format substring_<index>.txt
    arguments.add_argument(
        "-d",
        type=str,
        dest="dir",
        help="Save directory"
    )

    # Command-line parameter -r in which the user can specify a line of Python code
    # that prohibits breaking the current line from the input file.
    arguments.add_argument(
        "-r",
        type=str,
        dest="row",
        help="Line of code"
    )
    return arguments


def write_file(options, substring, count):
    with open(f"{options.dir}/substring_#{count}.txt", 'w+') as wfile:
        wfile.write(substring)
    count += 1
    return count


def separation_ban(options, line):
    # Functionality [-r] check
    try:
        func = eval(options.row)
    except Exception as error:
        raise CantEvaluate(options.row) from error

    if func(line):
        return line.strip()


def line_separator(line, options):
    idx = 0  # index of a letter in the string
    result = []  # Substring array
    substring = ''
    s_line = line.split()

    if options.row:
        line_ban = separation_ban(options, line)
        if line_ban:
            result.append(line_ban)
        return
    elif options.lrz and line.find('@') != -1:
        result.append(line.strip())
    else:
        for word in s_line:
            if word.find('@') != -1 or word.find(':') != -1 and line.find('@') != -1:
                substring = ' '.join([substring, word])
                idx += 1
                # Checks for the total length of the user tag.
                # If the length is longer than specified (e.g.: 1),
                # the substring will be added to the substring list and then reset to zero.
                if substring.find(':') != -1 and len(substring) >= options.num:
                    result.append(substring)
                    substring = ''
                continue
            substring = ' '.join([substring, word])
            if len(substring) >= options.num:
                result.append(substring)
                substring = ''
            elif idx == len(s_line) - 1:
                result.append(substring)
            idx += 1
    return result


# Data handling function
def file_handling(options):
    count = 1
    with open(options.source, 'rt') as source_file:
        if os.stat(options.source).st_size == 0:
            exit('File is empty.')
        if options.num == 0:
            if options.dir:
                write_file(options, source_file.read().strip(), count)
                return
            print(f'Substring #{count}:')
            for line in source_file:
                print(f'\t{line.strip()}')
            return
        for line in source_file:
            if not line.strip():
                continue
            for substring in line_separator(line, options):
                if not options.dir:
                    print(f'Substring #{count}:\n\t{substring.strip()}')
                    count += 1
                    continue
                count = write_file(options, substring, count)


def main():
    options = get_arguments().parse_args()
    if not options.source or not os.path.exists(options.source):
        exit(f'File {options.source} not exist!\n')
    if options.dir is not None and not os.path.exists(options.dir):
        exit(f'Path {options.dir} does not exist\n')
    file_handling(options)


if __name__ == '__main__':
    main()
