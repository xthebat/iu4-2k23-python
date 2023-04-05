from stream06.comprehension import power_collection_comp, power_collection_bad, modify_collection_comp, \
    filter_collection_comp, first, find


def test_power_collection_comp():
    assert power_collection_bad([1, 2, 3], 20) == \
           power_collection_comp([1, 2, 3], 20)


def power_20(it):
    return it ** 20


def test_modify_collection_comp():
    assert power_collection_bad([1, 2, 3], 20) == \
           modify_collection_comp([1, 2, 3], lambda it: it ** 20)


def test_filter_collection_comp():
    assert filter_collection_comp([1, 2, 3, "a", "b", "c"], lambda it: isinstance(it, str)) == \
           ["a", "b", "c"]


def test_complex_list_comp():
    input_list = [1, 2, 3, "a", "b", "c"]
    modified_list = [it ** 2 for it in input_list if isinstance(it, int)]
    assert modified_list == [1, 4, 9]


def test_complex_dict_comp():
    input_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 3
    }

    modified_dict = {v: k for k, v in input_dict.items() if k != "b"}

    assert modified_dict == {
        1: "a",
        3: "d"
    }


def test_complex_set_comp():
    input_list = [1, 2, 3, 1, 2, 3]
    modified_set = {it for it in input_list}
    assert modified_set == {1, 2, 3}


def print_what(item):
    print(f"I got {item=}")
    return item ** 2


def test_complex_generator_comp():
    input_list = [1, 2, 3, 1, 2, 3]
    modified_generator = (print_what(it) for it in input_list)

    for it in modified_generator:
        print(f"I am in for {it=}")

    # assert modified_generator == (1, 2, 3, 1, 2, 3)


def test_first():
    input_list = [1, 2, 3, "a", "b", "c"]
    found = first(input_list, lambda it: isinstance(it, str))
    assert found == "a"


def test_first_not_found():
    input_list = [1, 2, 3, "a", "b", "c"]
    try:
        # next(it for it in input_list if isinstance(it, float))
        first(input_list, lambda it: isinstance(it, float))
    except StopIteration:
        assert True
    else:
        assert False


def test_find():
    input_list = [1, 2, 3, "a", "b", "c"]
    found = find(input_list, lambda it: isinstance(it, str))
    assert found == "a"


def test_find_not_found():
    input_list = [1, 2, 3, "a", "b", "c"]
    found = find(input_list, lambda it: isinstance(it, float))
    assert found is None
