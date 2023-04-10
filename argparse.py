import argparse

def arg_parser(args: list[]):
    parser_files = argparse.ArgumentParser()

    parser_files.add_argument('-ofu', '--output-functions', help='return functions')
    parser_files.add_argument('-odir', '--output-dirs', help='return dirs')
    parser_files.add_argument('-otyp', '--output-types', help='return types')
    parser_files.add_argument('-if', '--input-file', help='return input file')
    parser_files.add_argument('-j', '--json', help='return json')

    return parser_files