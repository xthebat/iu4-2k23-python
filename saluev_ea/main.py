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


def line_separator(line, options):
    idx = 0  # index of a letter in the string
    result = []  # Substring array
    substring = ''
    s_line = line.split()

    # Functionality [-r] check
    try:
        func = eval(options.row)
    except Exception as error:
        raise CantEvaluate(options.row) from error

    if func(line):
        result.append(line)
    elif options.lrz and line.find('@') != -1:
        result.append(line)
    else:
        for word in s_line:
            if word.find('@') != -1:
                substring += f'{word} {s_line[idx+1]} '
                idx += 1
                continue
            elif word.find(':') != -1:
                idx += 1
                continue
            substring += f'{word} '
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
            print("File is empty.")
            return
        elif options.num in [0, 1]:
            print(f'Substring #{count}:\n')
            for line in source_file:
                print(f'\t{line.strip()}\n')
            return
        for line in source_file:
            for substring in line_separator(line, options):
                # Checking for the correctness of the -d argument
                # and for the existence of a directory. If the directory does not exist,
                # the result will be printed to the console.
                if not options.dir:
                    print(f'Substring #{count}:\n\t{substring.strip()}\n')
                else:
                    if os.path.exists(options.dir):
                        with open(f"{options.dir}/substring_#{count}.txt", 'w+') as wfile:
                            wfile.write(substring)
                    else:
                        print(f'Path {options.dir} does not exist\n')
                count += 1


def main():
    options = get_arguments().parse_args()
    if not options.source or not os.path.exists(options.source):  # Checking for the existence of a file
        print(f'File {options.source} not exist!\n')
        return
    file_handling(options)


if __name__ == '__main__':
    main()
