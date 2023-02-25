import re
import os
import argparse


# Function for working with arguments
def get_arguments():
    usage = '''2K23 Python Task #1'''

    arguments = argparse.ArgumentParser(
        description=usage
    )

    """ The input string is contained in a file,the path to which is passed through
        the command line argument with the -f key """
    arguments.add_argument(
        "-f",
        type=str,
        dest="source",
        help="Source file"
    )

    """ The maximum number of characters in a substring is specified by the command
        line argument with the -n key (the default value of the parameter is 200) """
    arguments.add_argument(
        "-n",
        type=int,
        default=200,
        dest="num",
        help="Max count symbols"
    )

    """ The -l command line parameter, when specified, adds an additional correctness
        to the split into substrings: it is not allowed to split "in the middle" of the string
        indicating the new user's score """
    arguments.add_argument(
        "-l",
        dest="lrz",
        action="store_true",
        help="Separation names"
    )

    """ The -d command line parameter, when specified, saves the output substring
        to different files in the directory specified in this parameter. 
        File names are specified in the format substring_<index>.txt """
    arguments.add_argument(
        "-d",
        type=str,
        dest="dir",
        help="Save directory"
    )

    """ Command-line parameter -r in which the user can specify a line of Python code
        that prohibits breaking the current line from the input file. """
    arguments.add_argument(
        "-r",
        type=str,
        dest="code_row",
        help="Line of code"
    )
    return arguments


def line_separator(line, options):
    tag = False
    idx = 0  # index of a letter in the string
    result = []  # Substring array
    substring = ''
    s_line = line.split()
    if options.lrz and line.find('@') != -1:
        result.append(line)
    else:
        for word in s_line:
            if word.find('@') != -1 or tag:
                if word.find(':') != -1:
                    tag = False
                    idx += 1
                    continue
                else:
                    tag = True
                    substring += f'{word} '
            substring += f'{s_line[idx+1]} ' if tag else f'{word} '
            if len(substring) >= options.num:
                result.append(substring)
                substring = ''
            elif idx == len(s_line) - 1:
                result.append(substring)
            idx += 1
    return result


# Data handling function
def file_handling(options):
    """ The try except construct is needed to handle an error
        in cases of invalid file encoding or an invalid [-n] argument """
    try:
        count = 1
        with open(options.source, 'rt') as source_file:
            if os.stat(options.source).st_size == 0:
                print("File is empty.")
            elif options.num in [0, 1]:
                print(f'Substring #{count}:', end='\n')
                for line in source_file:
                    print(f'\t{line.strip()}', end='\n')
            else:
                for line in source_file:
                    result = line_separator(line, options)
                    if result:
                        for substring in result:
                            """ Checking for the correctness of the -d argument 
                                and for the existence of a directory. If the directory does not exist,
                                the result will be printed to the console. """
                            if options.dir:
                                if os.path.exists(options.dir):
                                    namefile = f"{options.dir}/substring_#{count}.txt"
                                    with open(namefile, 'w+') as wfile:
                                        wfile.write(substring)
                                else:
                                    print(f'Path {options.dir} does not exist', end='\n')
                            else:
                                print(f'Substring #{count}:\n\t{substring.strip()}', end='\n')
                            count += 1
    except Exception as e:
        print(e)


def main():
    arguments = get_arguments()
    options = arguments.parse_args()
    if options.source and os.path.exists(options.source):  # Checking for the existence of a file
        file_handling(options)
    else:
        print(f'File {options.source} not exist!', end='\n')


if __name__ == '__main__':
    main()
