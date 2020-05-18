from science.hamming_weight import *


def get_bytes():
    a = '10010101'
    b = '11010011'
    return a, b


def test_xor():
    a, b = get_bytes()
    c = '01000110'
    
    assert type(xor(a, b)) is str
    
    assert xor(a, b) == c


def test_hamming_weight():
    a, b = get_bytes()
    weight_a = 4
    weight_b = 5

    assert type(hamming_weight(a)) is int
    
    assert hamming_weight(a) == weight_a
    assert hamming_weight(b) == weight_b


def test_hamming_distance():
    a, b = get_bytes()
    distance = 3
    
    assert type(hamming_distance(a, b)) is int
    assert type(hamming_distance_2(a, b)) is int

    assert hamming_distance(a, b) == 3
    assert hamming_distance_2(a, b) == 3
