from typing import Callable, Iterator

from bonus.types import T


def get(iterator: Iterator[T]) -> T | None:
    """
    Get next item from iterator or None if iterator is empty.

    :param iterator: Iterator to get element from.
    :return: Got Item from iterator.
    """
    return next(iterator, None)


def safe_issubclass(what, cls: type):
    """
    Function safely checks that `what` is specified subclass of `cls`.
    Default issubclass crashes if `what` is not class.

    :param what: Object to check.
    :param cls: Checking subclass of.
    :return: True if `what` is subclass of `cls` otherwise None.
    """
    return isinstance(what, type) and issubclass(what, cls)


def getitem2args(target: Callable):
    """
    Function decorator unpacks item to __getitem__ function arguments.
    By defaults arguments of __getitem__ can be tuple or single variable.

    :param target: Target __getitem__ function to wrap
    :return: Wrapped __getitem__ function
    """

    def __getitem__(cls, item):
        args = item if isinstance(item, tuple) else (item,)
        return target(cls, *args)

    return __getitem__
