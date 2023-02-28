import sys


def read_file(input_file):
    try:
        with open(input_file, 'r', encoding="utf-8") as f:
            input_str = f.read()
        return input_str
    except FileNotFoundError:
        print("ERROR: Input file not found.")
        sys.exit()


def split_strings(input_str, max_length=200):
    substring_list = []
    current_substring = ""
    for symbol in input_str:
        current_substring += symbol
        if len(current_substring) == max_length:
            substring_list.append(current_substring)
            current_substring = ""
    if current_substring != "":
        substring_list.append(current_substring)
    return substring_list


def output_result(substring_list):
    for i, substring in enumerate(substring_list):
        print(f"Substring {i+1}: {substring}")


def main():
    input_file = None
    max_length = 200
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == '-f':
            input_file = sys.argv[i+1]
        elif sys.argv[i] == '-n':
            max_length = int(sys.argv[i+1])

    if input_file is None:
        print("ERROR: Input file path not specified.")
        sys.exit()

    input_str = read_file(input_file)
    substring_list = split_strings(input_str, max_length)
    output_result(substring_list)


if __name__ == "__main__":
    main()
