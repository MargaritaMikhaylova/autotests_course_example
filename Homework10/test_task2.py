import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

def test_type_1():
    assert TypeError

@pytest.mark.parametrize('arg1, result', [(2, 2),(4, 4)])
def test_type_2(arg1, result):
    assert all_division(arg1) == result

def test_type_3():
    assert all_division(1, 1) == 1

@pytest.mark.smoke
def test_zero():
    assert ZeroDivisionError('Нельзя делить на ноль')

@pytest.mark.skip
def test_broken():
    assert False

