from salsa.QR_function import *
from tools.bit_generator import *
import time
import pytest



def test_QR():
    X = ('000000', '011001', '111100', '101010')
    Y = QR(X)
    assert type(Y) is tuple
    assert len(Y) == 4

    for bits in Y:
        assert type(bits) is str
        assert len(bits) == 6


def test_QR_chacha():
    X = ('000000', '011001', '111100', '101010')
    Y = QR_chacha(X)
    assert type(Y) is tuple
    assert len(Y) == 4

    for bits in Y:
        assert type(bits) is str
        assert len(bits) == 6


def time_QR(function, X, runs=1000):
    start = time.time()
    for i in range(runs):
        a = function(X)
    total_time = time.time() - start
    return total_time/runs


@pytest.mark.integration_test
def test_speed():
    functions = (QR, QR_chacha)
    Xs = (
        ('00000000', '00000000', '00000000', '00000000'),
        ('11111111', '11111111', '11111111', '11111111'),
        ('01010101', '01010101', '01010101', '01010101'),
        gen_random_words(4, 8),
        gen_random_words(4, 4),
        gen_random_words(4, 32),
        gen_random_words(4, 128),
        #gen_random_words(4, 256)
    )

    print()
    print("Name \t Bits \t Time per run \t Run per second")
    for f_index in range(len(functions)):
        for X_idx in range(len(Xs)):
            func = functions[f_index]
            X = Xs[X_idx]
            time_per_run = round(time_QR(func, X), 12)
            runs_per_second = round(1 / time_per_run, 5)
            print(func.__name__[:6], '\t', len(X[0]), '\t', time_per_run, '\t', runs_per_second)
    
    # assert False to run this test with output.
    #assert False
