import sys
import os


def check_length(filepath: str, length: int) -> bool:
    file = open(filepath, encoding='utf-8')
    text = file.read()
    file.close()
    list_ = list(text.split(" "))
    sorted_list = sorted(list_, key=len)
    #print(f"Word length {len(sorted_list[-1])=}")
    if len(sorted_list[-1]) < length:
        return True
    else:
        return False


def divide_strings(filepath: str, length: int) -> list[str]:
    file = open(filepath, encoding='utf-8')
    text = file.read()
    file.close()
    splinted_text = list(text.split(" "))
    current_substring = ""
    tag = ""
    substrings = []
    flag = 0
    for i in splinted_text:
        if len(current_substring) < length:
            if flag == 0:
                if i[0] == "@":
                    flag = 1
                    tag = i
                    if i[-1] == ":":
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
        print(f"Not enough {len(args)=} required > 2")
        return -1
    elif len(args) % 2 != 1:
        print(f"Missing arguments {len(args)=}")
        return -1
        args.index("-f")
    else:
        if len(args) == 3:
            if args[1] != "-f" or (args[1] == "-f" and not os.path.isfile(args[2])):
                print(f"No path to file sent")
            elif args[1] == "-f" and os.path.isfile(args[2]):
                filepath = sys.argv[2]

        elif len(args) == 5:
            if (args[1] != "-f") and (args[3] != "-f"):
                print(f"No path to file sent {args[1]=} {args[3]=}")
            elif (args[1] == "-f" and not os.path.isfile(args[2])) or (args[3] == "-f" and not os.path.isfile(args[4])):
                print("Incorrect path to file")
            else:
                if args[1] == "-f" and os.path.isfile(args[2]):
                    i = 1
                if args[3] == "-f" and os.path.isfile(args[4]):
                    i = 3
                filepath = sys.argv[i+1]
                if (args[1] == "-n" and not args[2].isdigit) or (args[3] == "-n" and not args[4].isdigit):
                    print(f"String length is not sent {args[2]=}")
                else:
                    if args[1] == "-n" and type(args[2]) != int:
                        i = 2
                    elif args[3] == "-n" and type(args[4]) != int:
                        i = 4
                    if check_length(filepath, int(args[i])):
                        length = int(sys.argv[i])
                    else:
                        print("Length too small , unable divide text")
        substrings = divide_strings(filepath, length)
        print_strings(substrings)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
