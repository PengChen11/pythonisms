import pytest

from pythonisms.pythonic_decorator import *


def test_destination():
    arg = 'China'
    test = vacation_suggestion(arg)
    assert test == f'Sure, I\'d love to go "{arg.upper()}" !!!!!'

