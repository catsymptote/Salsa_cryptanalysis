from tools.bit_generator import *
from tools.binary import Binary


def test_gen_random_bits():
    random_bits = gen_random_bits(6)
    assert type(random_bits) is Binary
    assert len(random_bits) == 6


def test_gen_random_words():
    # tuple
    random_words_tuple = gen_random_words(4, 16)
    assert type(random_words_tuple) is tuple
    assert len(random_words_tuple) == 4
    for word in random_words_tuple:
        assert type(word) is Binary
        assert len(word) == 16
    
    # list
    random_words_tuple = gen_random_words(4, 16, as_tuple=False)
    assert type(random_words_tuple) is list
    assert len(random_words_tuple) == 4
    for word in random_words_tuple:
        assert type(word) is Binary
        assert len(word) == 16


def test_while_bits():
    a = '0100101'
    b = Binary('01010111')
    c = ('010', '101', '110', '100')
    d = [Binary('1010'), Binary('001'), '100010101010']

    A = whipe_bits(a)
    B = whipe_bits(b, default='1')
    C = whipe_bits(c)
    D = whipe_bits(d)

    assert type(A) is str
    assert len(A) == len(a)
    assert A == '0000000'

    assert type(B) is Binary
    assert len(B) == len(b)
    assert B == Binary('11111111')

    assert type(C) is tuple
    assert len(C) == len(c)
    assert C == ('000', '000', '000', '000')
    assert type(C[0]) == type(C[1]) == type(C[2]) == type(C[3]) == str

    assert type(d) is list
    assert len(D) == len(d)
    assert D == [Binary('0000'), Binary('000'), '000000000000']
    assert type(D[0]) == type(D[1]) == Binary
    assert type(D[2]) == str
