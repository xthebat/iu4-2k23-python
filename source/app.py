from argparse import *
from argparse import Namespace

from c_header_parser import CParser
from console_visualizer import DataVisualizer
from data_loader import DataLoader


def parse_args() -> Namespace:
    parser = ArgumentParser(description="Best py prog ever #2!")
    parser.add_argument('-f', '--filename',
                        dest='infile',
                        required=True,
                        nargs=1,
                        metavar='<filename>',
                        help='input File name'
                        )
    parser.add_argument('-j', '--json',
                        dest='outfile',
                        required=False,
                        nargs=1,
                        metavar='<filename>',
                        help='output json file name'
                        )

    parser.add_argument('-of', '--output-functions',
                        dest='out_func',
                        required=False,
                        default=None,
                        action='store_true',
                        help='key to show functions')
    parser.add_argument('-od', '--output-directives',
                        dest='out_dir',
                        required=False,
                        default=None,
                        action='store_true',
                        help='key to show directives'
                        )
    parser.add_argument('-ot', '--output-types',
                        dest='out_types',
                        required=False,
                        default=None,
                        action='store_true',
                        help='key to show types')

    return parser.parse_args()


def main():
    args = parse_args()

    loader = DataLoader(dest_path_=args.outfile[0], source_path_=args.infile[0])
    parser = CParser(loader.read_header_file(), config_filename_='c_header_parser/config.json')

    parser.analyze_data()
    data = parser.data_as_dict()

    loader.dump_data(data)
    visualizer = DataVisualizer(data)

    if args.out_func:
        visualizer.print_units('functions')
    if args.out_dir:
        visualizer.print_units('defines')
    if args.out_types:
        visualizer.print_units('typedefs')


if __name__ == '__main__':
    main()
