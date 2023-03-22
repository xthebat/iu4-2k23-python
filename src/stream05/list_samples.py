from typing import Any


def list_extend(self: list, other: list):
    self.extend(other)


def push(stack: list, item: Any):
    stack.append(item)


def pop(stack: list) -> Any:
    return stack.pop()
