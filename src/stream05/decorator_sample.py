from typing import Callable


def loggable(callee: Callable):
    def wrapped(*args):
        result = callee(*args)
        print(f"args={args} result={result}")
        return result

    return wrapped
