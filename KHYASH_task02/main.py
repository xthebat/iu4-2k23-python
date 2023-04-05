import argparse 
import code_parser

arg_parser = argparse.ArgumentParser(
        prog = "C parser"
        )

arg_parser.add_argument("filename", type = str, help = "your C code")
arg_parser.add_argument("-o", "--output", help = "you can configure specific name for output file")

args = arg_parser.parse_args()


def main():
    parser = code_parser.Code_parser(input_filename = args.filename, output_filename = args.output)    
    parser.run_parser()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
