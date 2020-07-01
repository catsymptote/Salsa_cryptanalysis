from analysis.bad_crypto import *


###########
## Tools ##
###########

def get_0():
    a = Binary('00000000')
    X = (a, a, a, a)
    return X


def get_1():
    a = Binary('11111111')
    X = (a, a, a, a)
    return X


def get_ordered():
    a = Binary('11001100')
    b = Binary('11110000')
    X = (a, b, a, b)
    return X


def get_X():
    a = Binary('10011010')
    b = Binary('11100100')
    X = (a, b, a, b)
    return X


def test_tools():
    Xs = [
        get_0(), get_1(),
        get_ordered(), get_X()
    ]

    X = get_0()
    assert type(X) is tuple
    assert len(X) == 4
    for word in X:
        assert type(word) is Binary
        assert len(word) == 8
    
    X = get_1()
    assert type(X) is tuple
    assert len(X) == 4
    for word in X:
        assert type(word) is Binary
        assert len(word) == 8
    
    X = get_ordered()
    assert type(X) is tuple
    assert len(X) == 4
    for word in X:
        assert type(word) is Binary
        assert len(word) == 8
    
    X = get_X()
    assert type(X) is tuple
    assert len(X) == 4
    for word in X:
        assert type(word) is Binary
        assert len(word) == 8


###################
## General tests ##
###################

def test_get_algs():
    algs = get_algs()
    assert type(algs) is tuple
    assert len(algs) == 7


def test_types():
    algs = get_algs()
    X = get_X()
    for alg in algs:
        print(alg.__name__)
        print(alg)
        Y = alg(X)
        assert type(Y) is tuple
        assert len(Y) == 4
        for word in Y:
            assert type(word) is Binary
            assert len(word) == 8



####################
## Specific tests ##
####################

def test_nothing():
    a = get_0()
    b = get_1()
    c = get_ordered()
    d = get_X()

    assert nothing(a) == a
    assert nothing(b) == b
    assert nothing(c) == c
    assert nothing(d) == d


def test_random_bits():
    X = get_0()
    Y = random_bits(X)
    assert len(Y) == len(X)
    assert type(Y) is type(X) is tuple
    assert Y[0].bits != X[0].bits
    assert Y != X


def test_reverse_tuple():
    X = get_ordered()
    Y = reverse_tuple(X)
    assert X[0].bits == X[2].bits == '11001100'
    assert Y[1].bits == Y[3].bits == '11001100'


def test_reverse_bits():
    X = get_ordered()
    Y = reverse_bits(X)
    print(X)
    print(Y)
    assert X[0].bits == '11001100'
    assert Y[0].bits == '00110011'


def test_reverse_full():
    X = get_X()
    Y = reverse_full(X)

    assert X[3] == '11100100'
    assert Y[0] == '00100111'
    assert Y[3] == '01011001'


def test_xor_0():
    X = get_0()
    assert xor_0(X) == X


def test_xor_1():
    X = get_1()
    assert xor_1(X) == get_0()
