from binary.binary import Binary


def test_init():
    Bin1 = Binary()
    assert type(Bin1) is Binary
    assert type(Bin1.bits) is str
    assert Bin1.bits == '0'

    Bin2 = Binary(5)
    assert type(Bin2) is Binary
    assert type(Bin2.bits) is str
    assert Bin2.bits == '101'

    Bin3 = Binary('1100', 8)
    assert type(Bin3) is Binary
    assert type(Bin3.bits) is str
    assert Bin3.bits == '00001100'


def test_set_val():
    Bin = Binary()
    assert Bin.bits == '0'
    Bin.set_val(5)
    assert Bin.bits == '101'


def test_fix_padding():
    Bin = Binary(5, 8)
    assert Bin.bits == '101'
    Bin.add_padding()
    assert Bin.bits == '00000101'


def test_dec_to_bin():
    Bin = Binary()

    assert Bin.dec_to_bin(3) == '11'
    assert Bin.dec_to_bin(10) == '1010'
    assert Bin.dec_to_bin(8) == '1000'


def test_get_dec():
    a = Binary(3)
    b = Binary(10, 8)
    c = Binary(8, 4)
    
    assert a.get_dec() == 3
    assert b.get_dec() == 10
    assert c.get_dec() == 8


def test_get_hex():
    a = Binary(3)
    b = Binary(10, 8)
    c = Binary(8, 4)
    
    assert a.get_hex() == '3'
    assert b.get_hex() == 'a'
    assert c.get_hex() == '8'


def test_get_bin():
    a = Binary(3)
    b = Binary(10, 8)
    c = Binary(8, 4)
    
    assert a.get_dec() == '11'
    assert b.get_dec() == '1010'
    assert c.get_dec() == '1000'


def test_is_binary():
    Bin = Binary()

    assert Bin.is_binary('10101')
    assert Bin.is_binary('0')
    assert not Bin.is_binary('102')
    assert not Bin.is_binary('1af0')
    assert not Bin.is_binary(10)


def test_is_even():
    a = Binary(3)
    b = Binary(10, 8)
    c = Binary(8, 4)

    assert not a.is_even()
    assert b.is_even()
    assert c.is_even()


def test_len():
    a = Binary(3)       # 11
    b = Binary(10, 8)   # 00001010
    c = Binary(7, 4)    # 0111
    d = Binary(13)      # 10101

    assert len(a) == 2
    assert len(b) == 8
    assert len(c) == 4
    assert len(d) == 5
