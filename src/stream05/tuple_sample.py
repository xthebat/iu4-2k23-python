from typing import Iterable, Callable, Any, TypeVar

T = TypeVar("T")


def tuple_filter(collection: Iterable, predicate: Callable) -> tuple:
    result = ()
    for it in collection:
        if predicate(it):
            result += (it,)
    return result


def list_filter(iterable: Iterable[T], predicate: Callable[[T], bool]) -> tuple[T]:
    result = []
    for it in iterable:
        if predicate(it):
            result.append(it)
    return tuple(result)


def list_accumulate(collection: Iterable, key: Callable, initial: Any) -> Any:
    result = initial
    for it in collection:
        result += key(it)
    return result
