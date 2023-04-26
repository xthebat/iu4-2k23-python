import os
import json
import argparse

from saluev_makhmudov.CHandlerClass import CHandlerClass


def get_arguments():
    usage = '2K23 Python Task #2'

    arguments = argparse.ArgumentParser(description=usage)
    # Data output formats
    arguments.add_argument('-of', '--output-functions', dest='out_func',
                           action='store_true', help="List functions")
    arguments.add_argument('-od', '--output-directives', dest='out_dir',
                           action='store_true', help="List directives")
    arguments.add_argument('-ot', '--output-types', dest='out_types',
                           action='store_true', help="List types")

    # Input and output files
    arguments.add_argument('-f', '--input-file', dest='in_file',
                           type=str, help="Input file for parsing")
    arguments.add_argument('-o', '--output-file', dest='o_file',
                           type=str, help="Save to file "
                                          "[Specify file name without an extension]")

    # Format for saving the output file
    arguments.add_argument('-j', '--json', dest='f_json',
                           action='store_true', help="Save in json format "
                                                     "[Specify if you want to save the file in json format]")
    return arguments


def checks(arguments):
    # Checking for the existence of a file
    if not arguments.in_file or not os.path.exists(arguments.in_file):
        exit(f'File {arguments.in_file} not exist!\n')

    # Checking that the input file format is correct
    if arguments.in_file.split('/')[-1].find('.') == -1:
        exit(f'File {arguments.in_file} has the wrong format!\n')

    # Checking whether the output file is specified
    if not arguments.o_file:
        exit(f'Output file not specified!\n')


def data_assembly(arguments, functions, directives, types):
    summary_data = []
    if arguments.out_func:
        summary_data += functions
    if arguments.out_dir:
        summary_data += directives
    if arguments.out_types:
        summary_data += types
    return summary_data


def saving_to_file(arguments, summary_data):
    if arguments.f_json:
        with open(f'{arguments.o_file}.json', 'w+') as json_file:
            json.dump(summary_data, json_file, sort_keys=True, indent=4)
            exit()

    with open(f'{arguments.o_file}.txt', 'w+') as txt_file:
        for line in summary_data:
            write_file = str(line).replace('{', '').replace('}', '').replace("'", '')
            txt_file.write(f'{write_file}\n')


def main():
    # Pull arguments
    arguments = get_arguments().parse_args()
    # Functionality check with given arguments
    checks(arguments)
    # Data processing
    functions, directives, types = CHandlerClass().reader_file(arguments.in_file)

    # Check if there are active arguments concerning the type of output
    # data and collect them all into a single array
    summary_data = data_assembly(arguments, functions, directives, types)

    # Saving to a file
    if not summary_data:
        exit(f'Nothing was found as a result of the search\n')
    saving_to_file(arguments, summary_data)


if __name__ == '__main__':
    main()
