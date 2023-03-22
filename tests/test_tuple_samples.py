from stream05.common import benchmark
from stream05.tuple_sample import tuple_filter, list_filter, list_accumulate


def test_tuple_filter():
    print()

    collection = list(range(20_000))

    @benchmark
    def function():
        tuple_filter(collection, lambda it: it > 10_000)

    function()


def test_list_filter():
    print()

    collection: list[int] = list(range(20_000))

    @benchmark
    def function():
        result = list_filter(collection, lambda it: it > 10_000)
        assert result

    function()


def test_list_accumulate():
    collection = range(4)
    result = list_accumulate(collection, lambda it: it * it, 0)
    assert result == 1 + 4 + 9

# 91_453_040
#  1_224_670
