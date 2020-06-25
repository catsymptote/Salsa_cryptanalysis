from tools.binary import Binary


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
    a.LSO(2)
    assert a.bits == '11000011'


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


def test_mod_add():
    a = Binary(234)
    b = Binary(345)
    c = Binary(500)
    d = Binary(579)
    
    #print(type(a%b))
    #print(type(c))
    assert a % b != c
    assert a % b != d
    d.set_size(len(b))
    assert a % b == d


def test_mod_int():
    a = Binary(46)
    assert a == '101110'
    assert type(a % 3) is Binary
    assert a % 3 == '110'
    assert a % 5 == '01110'


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
