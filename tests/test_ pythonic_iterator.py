import pytest

from pythonisms.pythonic_iterator import LL

def test_for_in():

    foods = LL(("apple","banana","cucumber"))

    foods_list = []

    for food in foods:
        foods_list.append(food)

    assert foods_list == ["apple","banana","cucumber"]


def test_list_comprehension():

    foods = LL(("apple","banana","cucumber"))

    cap_foods = [food.upper() for food in foods]

    assert cap_foods == ["APPLE","BANANA","CUCUMBER"]

def test_list_cast():

    food_list = ["apple","banana","cucumber"]

    foods = LL(food_list)

    assert list(foods) == food_list

def test_range():

    num_range = range(1,20+1)

    nums = LL(num_range)

    assert len(nums) == 20


def test_filter():

    nums = LL(range(1,21))

    odds = [num for num in nums if num % 2]

    assert odds == [1,3,5,7,9,11,13,15,17,19]

def test_next():

    foods = LL(["apple","banana","cucumber"])

    iterator = iter(foods)

    assert next(iterator) == "apple"
    assert next(iterator) == "banana"
    assert next(iterator) == "cucumber"

def test_stop_iteration():

    foods = LL(["apple","banana","cucumber"])

    iterator = iter(foods)

    with pytest.raises(StopIteration):
        while True:
            food = next(iterator)


def test_str():
    foods = LL(["apple","banana","cucumber"])
    assert str(foods) == "[ apple ] -> [ banana ] -> [ cucumber ] -> None"

# dunder method tests

def test_equals():

    lla = LL(["apple","banana","cucumber"])
    llb = LL(["apple","banana","cucumber"])

    assert lla == llb

def test_get_item():

    foods = LL(["apple","banana","cucumber"])

    assert foods[0] == "apple"

    assert foods[-3] == "apple"



def test_get_item_out_of_range():

    foods = LL(["apple","banana","cucumber"])

    with pytest.raises(IndexError):
        test = foods[3]
        test2 = foods[-4]
