from tools.binary import Binary
from tools.hamming import HD, HW
import random
import pytest


def test_init():
    Bin1 = Binary()
    assert type(Bin1) is Binary
    assert type(Bin1.bits) is str
    assert Bin1.bits == '0'

    Bin2 = Binary(5)
    assert type(Bin2) is Binary
    assert type(Bin2.bits) is str
    assert Bin2.bits == '101'

    Bin3 = Binary('1100')
    assert type(Bin3) is Binary
    assert type(Bin3.bits) is str
    assert Bin3.bits == '1100'


def test_set_val():
    Bin = Binary()
    assert Bin.bits == '0'
    Bin.set_val(5)
    assert Bin.bits == '101'


def test_gen_random():
    Bin = Binary()
    assert Bin.bits == '0'
    Bin.gen_random(32)
    assert type(Bin.bits) is str
    assert len(Bin.bits) == 32

    zeros = 0
    ones = 0
    for bit in Bin.bits:
        if bit == '0':
            zeros += 1
        else:
            ones += 1
    assert 4 < zeros < 28
    assert 4 < ones < 28



def test_add_padding():
    Bin = Binary(5)
    assert Bin.bits == '101'
    Bin.add_padding(8)
    assert Bin.bits == '00000101'


def test_set_bin():
    Bin = Binary()

    Bin.set_bin(3)
    assert Bin == '11'

    Bin.set_bin(10)
    assert Bin == '1010'

    Bin.set_bin(8)
    assert Bin == '1000'


def test_set_size():
    a = Binary('10101')
    assert a.bits == '10101'
    a.set_size(10)
    assert a.bits == '0000010101'


def test_set_at():
    a = Binary('10101')
    assert a.bits == '10101'
    a.set_at(2, '0')
    assert a.bits == '10001'
    a.set_at(1, '1')
    assert a.bits == '11001'
    a.set_at(0, '1')
    assert a.bits == '11001'


def test_flip_bit_at():
    a = Binary('10101')
    assert a.bits == '10101'
    a.flip_bit_at(2)
    assert a.bits == '10001'
    a.flip_bit_at(1)
    assert a.bits == '11001'
    a.flip_bit_at(0)
    assert a.bits == '01001'


def test_get_dec():
    a = Binary(3)
    b = Binary(10)
    c = Binary(8)
    
    assert a.get_dec() == 3
    assert b.get_dec() == 10
    assert c.get_dec() == 8


def test_get_hex():
    a = Binary(3)
    b = Binary(10)
    c = Binary(8)
    
    assert a.get_hex() == '3'
    assert b.get_hex() == 'a'
    assert c.get_hex() == '8'


def test_get_bin():
    a = Binary(3)
    b = Binary(10)
    c = Binary(8)
    
    # Test empty get.
    assert a.get_bin() == '11'
    assert b.get_bin() == '1010'
    assert c.get_bin() == '1000'

    # Test fixed-size get.
    assert a.get_bin(5) == '00011'
    assert b.get_bin(8) == '00001010'
    assert c.get_bin(3) == '000'


def test_incement():
    a = Binary(30)
    assert a.get_dec() == 30
    assert a.bits == '11110'
    
    a.incr()
    assert a.get_dec() == 31
    assert a.bits == '11111'
    
    a.incr(4)
    assert a.get_dec() == 35
    assert a.bits == '100011'


def test_decrement():
    a = Binary(30)
    assert a.get_dec() == 30
    assert a.bits == '11110'
    
    a.decr()
    assert a.get_dec() == 29
    assert a.bits == '11101'
    
    a.decr(4)
    assert a.get_dec() == 25
    assert a.bits == '11001'


def test_is_binary():
    Bin = Binary()

    assert Bin.is_binary('10101')
    assert Bin.is_binary('0')
    assert not Bin.is_binary('102')
    assert not Bin.is_binary('1af0')
    assert not Bin.is_binary(10)


def test_is_even():
    a = Binary(3)
    b = Binary(10)
    c = Binary(8)
    d = Binary()

    assert not a.is_even()
    assert b.is_even()
    assert c.is_even()
    assert d.is_even()


def test_LSO():
    a = Binary('11110000')
    a.LSO(2)
    assert a.bits == '11000011'


def test_LSO_overload():
    a = Binary('11110000')
    b = a // 2
    assert b.bits == '11000011'


def test_len():
    a = Binary(3)       # 11
    b = Binary(34)      # 100010
    c = Binary(7)       # 111
    d = Binary(13)      # 1101
    e = Binary(1)       # 1
    f = Binary(0)       # 0

    assert len(a) == 2
    assert len(b) == 6
    assert len(c) == 3
    assert len(d) == 4
    assert len(e) == 1
    assert len(f) == 1


def test_xor():
    # Setup.
    a_ = Binary('10101010')
    b_ = Binary('11110000')
    c_ = Binary('11010001')
    ab = Binary('01011010')
    ac = Binary('01111011')
    bc = Binary('00100001')

    # Type test.
    assert type(a_ ^ b_) is Binary

    # Invertible test.
    assert a_ ^ b_ == b_ ^ a_

    # Check if accurate.
    assert a_ ^ b_ == ab
    assert a_ ^ c_ == ac
    assert b_ ^ c_ == bc    


def test_add():
    a = Binary(123)
    b = Binary(345)
    c = Binary(468)
    assert a + b == c
    assert a.is_binary(a)
    assert a.is_binary(a+b)


def test_mod_add():
    a = Binary(234)
    b = Binary(345)
    c = Binary(500)
    d = Binary(579)
    
    assert a % b != c
    assert a % b != d
    d.set_size(len(b))
    assert a % b == d

    assert a.is_binary(a)
    assert b.is_binary(b)
    assert c.is_binary(c)
    assert d.is_binary(d)


def test_mod_int():
    a = Binary(46)
    assert a == '101110'
    assert type(a % 3) is Binary
    assert a % 3 == '110'
    assert a % 5 == '01110'


def test_rotate():
    # Rotate, LSO, floordiv, //
    a = Binary('1111100000')
    b = a // 3


def test_str_print(capsys):
    # "print(instance)"" should print the binary number. 
    a = Binary('1001')
    print('a:', a)
    captured = capsys.readouterr()
    assert captured.out == 'a: 1001\n'


def test_hamming_weight():
    a = Binary('11111111')
    b = Binary('11110000')
    c = Binary('11010011')
    d = Binary('10000001')

    # Test.
    assert a.hamming_weight() == 8
    assert b.hamming_weight() == 4
    assert c.hamming_weight() == 5
    assert d.hamming_weight() == 2


def test_hamming_distance():
    a = Binary('11111111')
    b = Binary('11110000')
    c = Binary('11010011')
    d = Binary('10000001')

    # Test.
    

    assert a.hamming_distance(b) == 4
    assert a.hamming_distance(c) == 3
    assert a.hamming_distance(d) == 6

    assert b.hamming_distance(c) == 3
    assert b.hamming_distance(d) == 4

    assert c.hamming_distance(d) == 3


def test_hamming_distance_hw_xor():
    a = Binary('11111111')
    b = Binary('11110000')
    c = Binary('11010011')
    d = Binary('10000001')

    # Test.
    assert a.hamming_distance_hw_xor(b) == 4
    assert a.hamming_distance_hw_xor(c) == 3
    assert a.hamming_distance_hw_xor(d) == 6

    assert b.hamming_distance_hw_xor(c) == 3
    assert b.hamming_distance_hw_xor(d) == 4

    assert c.hamming_distance_hw_xor(d) == 3


def test_split_string():
    a = '1111000011110000'
    b = Binary(a)

    A = b.split_string(a)
    B = b.split_string(b)
    C = b.split_string()
    D = b.split_string(a, 8)
    with pytest.raises(AssertionError):
        E = b.split_string(a, 3)
    
    expected_result_1 = (
        Binary('1111'),
        Binary('0000'),
        Binary('1111'),
        Binary('0000')
    )

    expected_result_2 = (
        Binary('11'),
        Binary('11'),
        Binary('00'),
        Binary('00'),
        Binary('11'),
        Binary('11'),
        Binary('00'),
        Binary('00')
    )

    assert A == expected_result_1
    assert B == expected_result_1
    assert C == expected_result_1
    assert D == expected_result_2


def test_combine_string():
    a = (
        Binary('1111'),
        Binary('0000'),
        Binary('1111'),
        Binary('0000')
    )
    A = Binary('1111000011110000')
    assert A.combine_string(a) == A


def test_flip_random_bit():
    a = Binary('00000000')
    b = Binary('11111111')
    c = Binary('11001010')

    a.flip_random_bit()
    b.flip_random_bit()
    c.flip_random_bit()
    
    assert HD(a, '00000000') == 1
    assert HD(b, '11111111') == 1
    assert HD(c, '11001010') == 1


def test_random_index():
    a = Binary('1001101010')
    indexes = [0] * len(a)
    runs = 100
    for i in range(runs):
        index = random.randint(0, len(a.bits) - 1)
        indexes[index] += 1
    for index in indexes:
        assert index > 0
