from science.math_tools import *


def test_average():
    values = [1, 5, 9, 13]
    result = average(values)
    assert type(result) is float or type(result) is int
    assert result == 7.0


def test_average_n():
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    result = average_n(values)
    assert type(result) is list
    for res in result:
        assert type(res) is float or type(res) is int
    
    assert len(result) == len(values)/4 == 3
    assert result == [1.5, 5.5, 9.5]
