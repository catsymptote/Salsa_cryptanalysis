from tools.hamming import *
import pytest
import time


def test_HW():
    a = '10101010' #4
    b = Binary('11110110') #6
    assert HW(a) == 4
    assert HW(b) == 6


def test_HD():
    a = '10101010'
    b = '11111100'
    c = Binary('11110110')
    d = Binary('10010100')

    # HD
    assert HD(a, b) == 4
    assert HD(a, c) == 4
    assert HD(a, d) == 5
    assert HD(b, c) == 2
    assert HD(b, d) == 3
    assert HD(c, d) == 3

    # HD_2
    assert HD_2(a, b) == 4
    assert HD_2(a, c) == 4
    assert HD_2(a, d) == 5
    assert HD_2(b, c) == 2
    assert HD_2(b, d) == 3
    assert HD_2(c, d) == 3


def time_HD(n, alg, word_1, word_2):
    start = time.time()
    for i in range(n):
        a = alg(word_1, word_2)
    finished = time.time()
    total_time = finished - start
    return total_time/n


@pytest.mark.integration_test
def test_HD_algs_speed():
    runs = 10000
    word_1 = '10101010'
    word_2 = '11111001'
    
    test_1 = time_HD(runs, HD, word_1, word_2)
    test_1_bin = time_HD(runs, HD, Binary(word_1), Binary(word_2))
    test_2 = time_HD(runs, HD_2, word_1, word_2)
    test_2_bin = time_HD(runs, HD_2, Binary(word_1), Binary(word_2))

    print('\n#\t str\t\t Binary')
    print('1\t', round(test_1, 12), '\t', round(test_1_bin, 12))
    print('2\t', round(test_2, 12), '\t', round(test_2_bin, 12))

    assert 0 < test_1 < test_1_bin < test_2_bin < test_2 < 1
    #assert 0.000001 < test_1 < test_1_bin < test_2_bin < test_2 < 0.00001


def time_HW(n, alg, word):
    start = time.time()
    for i in range(n):
        a = alg(word)
    finished = time.time()
    total_time = finished - start
    return total_time/n


@pytest.mark.integration_test
def test_HW_algs_speed():
    runs = 10000
    word = '1010101011110010'
    
    test_1 = time_HW(runs, HW, word)
    test_1_bin = time_HW(runs, HW, Binary(word))
    test_2 = time_HW(runs, HW_2, word)
    test_2_bin = time_HW(runs, HW_2, Binary(word))

    print('\n#\t str\t\t Binary')
    print('1\t', round(test_1, 12), '\t', round(test_1_bin, 12))
    print('2\t', round(test_2, 12), '\t', round(test_2_bin, 12))

    assert 0 < test_1 < test_1_bin < test_2 < test_2_bin < 1
    #assert 0.000001 < test_1 < test_1_bin < test_2_bin < test_2 < 0.00001
