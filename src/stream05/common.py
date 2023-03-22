import time
from typing import Callable


def benchmark(function: Callable):
    def wrapped(*args):
        start = time.perf_counter_ns()
        for k in range(10):
            result = function(*args)
        end = time.perf_counter_ns()
        print(f"function = {function} mean = {(end - start) / 10} ns")
        # noinspection PyUnboundLocalVariable
        return result

    return wrapped
