from statistical_analysis import *


def test_split_str():
    a = '11111111'
    b = '11110000'
    c = '11001100'
    d = '10101010'
    pieces = 4

    res_a = split_str(a, pieces=pieces)
    res_b = split_str(b, pieces=pieces)
    res_c = split_str(c, pieces=pieces)
    res_d = split_str(d, pieces=pieces)

    assert res_a == [3, 3, 3, 3]
    assert res_b == [3, 3, 0, 0]
    assert res_c == [3, 0, 3, 0]
    assert res_d == [2, 2, 2, 2]
