import os.path
import re
import sys
import click

from typing import Iterator, Optional


@click.command()
@click.option("-f", "file_path", required=True, help="Path to file")
@click.option("-n", "max_len", default=200, help="Max simbols in line")
@click.option("-l", "skip_score", is_flag=True, help="Split score")
@click.option("-d", "target_directory", help="Directory to save substrings")
@click.option(
    "-r", "deprecating_expression",
    help="Expression to protect line from breaking"
)
def main(
    file_path: str,
    max_len: int,
    skip_score: bool,
    target_directory: str,
    deprecating_expression: str,
):
    """Main program entrypoint."""

    try:
        with open(file_path, "r") as file:
            file_text = file.read()
    except OSError:
        print(f"Can't read input file '{file_path}'")
        sys.exit(os.EX_NOINPUT)

    deprecation_checker = None
    if deprecating_expression:
        try:
            deprecation_checker = eval(deprecating_expression)
        except Exception as error:
            print(f"Can't interpret '{deprecating_expression}':  {error}")
            sys.exit(os.EX_DATAERR)

    breakpoints_iterator = iterate_breakpoint_indexes(
        file_text, skip_score, deprecation_checker
    )

    breakpoint_indexes = collect_breakpoint_indexes(max_len, breakpoints_iterator)

    if len(file_text) not in breakpoint_indexes:
        breakpoint_indexes.append(len(file_text))

    substrings = create_substrings(file_text, breakpoint_indexes)
    if target_directory:
        if not os.path.isdir(target_directory):
            print(f"Directory '{target_directory}' doesn't exists")
            sys.exit(os.EX_DATAERR)
    print_substrings(substrings, target_directory)


def print_substrings(substrings: list[str], directory: str):
    """Print substrings in appropriate format."""

    for idx, substring in enumerate(substrings, 1):
        substring_name = f"Substring #:{idx}"
        if directory:
            with open(os.path.join(directory, substring_name), "w") as file:
                file.write(substring)
        else:
            print(substring_name, substring, "\n")


def create_substrings(
    text: str,
    breakpoint_indexes: list[int],
) -> list[str]:
    """Break text into substrings."""

    substrings = []
    start = 0
    for idx in breakpoint_indexes:
        substrings.append(text[start:idx])
        start = idx + 1
    return substrings


def is_deprecated(line, deprecation_checker: Optional[callable] = None) -> bool:
    """Check if line is deprecated."""

    if deprecation_checker:
        try:
            return deprecation_checker(line)
        except Exception as error:
            print(f"Error in deprecating expression: {error}")
            sys.exit(os.EX_DATAERR)

    return False


def iterate_breakpoint_indexes(
    text: str,
    split_scores: bool = False,
    deprecation_checker: Optional[callable] = None,
) -> Iterator[int]:
    """Iterator on text breakpoint indexes."""

    score_template = "- Новый score пользователя @"
    current_index = -1

    for line in text.splitlines():
        if split_scores and re.match(score_template, line) or is_deprecated(line, deprecation_checker):
            current_index += len(line)
        else:
            is_tag = False
            for symbol in line:
                current_index += 1
                if symbol.isspace() and not is_tag:
                    yield current_index
                elif symbol == "@":
                    is_tag = True
                elif is_tag and symbol == ":":
                    is_tag = False
        current_index += 1
        if current_index < len(text):
            yield current_index


def collect_breakpoint_indexes(
    max_len: int,
    break_points_iterator: Iterator[int],
) -> list[int]:
    """Collect appropriate indexes to make a line break."""

    breakpoint_indexes = []
    prev_breakpoint_idx = 0
    current_len = 0
    for idx in break_points_iterator:
        if idx - current_len > max_len:
            if prev_breakpoint_idx in breakpoint_indexes or prev_breakpoint_idx == 0:
                print("Can't break text into lines with your restrictions")
                sys.exit(os.EX_DATAERR)
            breakpoint_indexes.append(prev_breakpoint_idx)
            current_len = prev_breakpoint_idx
        else:
            prev_breakpoint_idx = idx

    return breakpoint_indexes


if __name__ == '__main__':
    main()
