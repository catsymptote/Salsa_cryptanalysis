from pair_generator import *


def test_gen_random_string():
    string = gen_random_string(24)
    assert type(string) is str
    assert len(string) == 24


def test_gen_random_QR():
    X = gen_random_QR()
    assert type(X) is tuple
    assert len(X) == 4
    assert type(X[0]) is str
    assert len(X[0]) == 32

    bits = 0
    non_bit = 0
    for word in X:
        for bit in word:
            if bit == '0' or bit == '1':
                bits += 1
            else:
                non_bit += 1
    assert bits == 128
    assert non_bit == 0


def test_to_binary():
    assert to_binary('abc') == '011000010110001001100011'


def test_get_plaintext():
    assert get_plaintext(0) == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    assert get_plaintext(1) == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'
    assert get_plaintext(3) == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011'
    assert get_plaintext(1000) == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111101000'
