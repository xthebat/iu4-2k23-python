import pytest

from stream05.list_samples import list_extend, push, pop


@pytest.mark.parametrize(
    "initial,other,expected",
    [
        ([1, 2, 3], [10, 15, 20], [1, 2, 3, 10, 15, 20]),
        (["a", "aboba"], [1, 2, 3], ["a", "aboba", 1, 2, 3]),
    ]
)
def test_list_extend(initial: list, other: list, expected: list):
    list_extend(initial, other)
    assert initial == expected


def test_stack():
    stack = []
    push(stack, 1)
    push(stack, 2)
    push(stack, 3)

    assert stack == [1, 2, 3]
    assert pop(stack) == 3
    assert pop(stack) == 2
    assert pop(stack) == 1
