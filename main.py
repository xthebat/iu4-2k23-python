import sys
import os


def check_length(text: str, length: int) -> bool:
    list_ = text.split(" ")
    sorted_list = sorted(list_, key=len)
    return len(sorted_list[-1]) < length


def divide_strings(text: str, length: int) -> list[str]:
    splinted_text = list(text.split(" "))
    current_substring = ""
    tag = ""
    substrings = []
    flag = 0
    for i in splinted_text:
        if len(current_substring) < length:
            if flag == 0:
                if i.startswith("@"):
                    flag = 1
                    tag = i
                    if i.startswith(":"):
                        flag = 0
                        if len(current_substring) + len(tag) <= length:
                            current_substring += " " + tag
                        else:
                            substrings.append(current_substring)
                            current_substring = tag
                else:
                    if len(current_substring) + len(i) <= length:
                        current_substring += " " + i
                    else:
                        substrings.append(current_substring)
                        current_substring = i
            else:
                tag += " " + i
                if i[-1] == ":":
                    flag = 0

                    if len(current_substring) + len(tag) <= length:
                        current_substring += " " + tag
                    else:
                        substrings.append(current_substring)
                        current_substring = tag

    if len(current_substring) != 0:
        substrings.append(current_substring)

    return substrings


def print_strings(strings: list[str]):
    for i in range(len(strings)):
        print(f"Substring #{i+1}:\n{strings[i]}")


def main(args: list[str]) -> int:
    length = 200
    if len(args) < 3:
        print(f"Not enough {len(args)=} required at least filepath")
        return -1
    else:
        f_index = args.index("-f")
        if f_index == -1:
            print("No filepath found")
            return -1
        elif not os.path.isfile(args[f_index+1]):
            print("Incorrect path to file")
            return -1
        else:
            with open(sys.argv[f_index+1], encoding='utf-8') as file:
                text = file.read()
        n_index = args.index("-n")
        if n_index != -1 and args[n_index+1].isdigit:
            if check_length(text, int(args[n_index+1])):
                length = int(sys.argv[n_index+1])
            else:
                print("Length too small , unable divide text")
                return -1
        elif not args[n_index+1].isdigit:
            print("Incorrect length value")
            return -1
        substrings = divide_strings(text, length)
        print_strings(substrings)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
