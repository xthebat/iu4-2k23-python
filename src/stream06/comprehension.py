from typing import Iterable, TypeVar, Callable

T = TypeVar("T")
R = TypeVar("R")


def power_collection_bad(collection: Iterable[int], power: int):
    result = []
    for it in collection:
        result.append(it ** power)
    return result


def power_collection_comp(collection: Iterable[int], power: int):
    return [it ** power for it in collection]


def modify_collection_comp(collection: Iterable[T], function: Callable[[T], R]) -> list[R]:
    return [function(it) for it in collection]


def filter_collection_comp(collection: Iterable[T], predicate: Callable[[T], bool]) -> list[T]:
    return [it for it in collection if predicate(it)]


def first(collection: Iterable[T], predicate: Callable[[T], bool]):
    return next(it for it in collection if predicate(it))


def find(collection: Iterable[T], predicate: Callable[[T], bool]):
    return next((it for it in collection if predicate(it)), None)
