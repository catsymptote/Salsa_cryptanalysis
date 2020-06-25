import pytest

from salsa.prg import PRG


def make_words(n=1, as_tuple=True):
    byte1 = '10010101100101011001010110010101'
    byte2 = '10100100101001001010010010100100'
    
    if n == 1:
        return byte1

    words = [byte1, byte2]
    
    if n != 2:
        n -= 2
        new_word = byte2
        for i in range(n):
            new_word = new_word[3:] + new_word[:3]
            words.append(new_word)
    
    if as_tuple is True:
        return tuple(words)
    else:
        bits = ''
        for word in words:
            bits += word
        return bits


def test_make_word():
    b1 = '10010101100101011001010110010101'
    b2 = '10100100101001001010010010100100'
    b3 = '00100101001001010010010100100101'
    b4 = '00101001001010010010100100101001'
    b5 = '01001001010010010100100101001001'

    assert make_words() == b1
    assert make_words(n=2) == (b1, b2)

    assert type(make_words()) is str
    assert type(make_words(n=2)) is tuple
    assert type(make_words(n=4)) is tuple
    assert type(make_words(n=4, as_tuple=False)) is str

    words = make_words(n=5)
    assert words[0] == b1
    assert words[1] == b2
    assert words[2] == b3
    assert words[3] == b4
    assert words[4] == b5


def test_init():
    prg1 = PRG()
    assert type(prg1) is PRG

    assert len(prg1.a_vects) == len(prg1.b_vects) == len(PRG.A_VECTOR) == len(PRG.B_VECTOR) == 4
    assert len(prg1.a_vects[0]) == 32

    prg2 = PRG(test_mode=True)
    assert prg2.test_mode == True


@pytest.mark.skip
def test_to_ascii():
    prg = PRG()
    output = prg.to_ascii('A')
    assert output == 65


@pytest.mark.skip
def test_from_ascii():
    prg = PRG()
    output = prg.from_ascii(65)
    assert output == 'A'


@pytest.mark.skip
def test_to_binary():
    prg = PRG()
    output = prg.to_binary(65)
    assert output == '01000001'


@pytest.mark.skip
def test_from_binary():
    prg = PRG()
    output = prg.from_binary(bin(65))
    assert output == 65


#@pytest.mark.skip
def test_to_bytes():
    prg = PRG()
    words1 = make_words(n=8)
    words2 = make_words(n=8, as_tuple=False)
    output1 = prg.to_bytes(words1)
    output2 = prg.to_bytes(words2)
    assert type(output1) is type(output2) is tuple
    assert len(output1) == len(output2) == len(words1)*4 == len(words2)/8
    for byte in output1:
        assert len(byte) == 8
    for byte in output2:
        assert len(byte) == 8
    
    assert output1 == output2


#@pytest.mark.skip
def test_to_words():
    prg = PRG()
    bits = make_words(n=8, as_tuple=False)
    output = prg.to_words(bits)
    assert type(output) is tuple
    assert len(output) == len(bits)/32 == 8
    for word in output:
        assert len(word) == 32


#@pytest.mark.skip
def test_to_bits():
    prg = PRG()
    words = make_words(n=8)
    output = prg.to_bits(words)
    assert type(output) is str
    assert len(output) == len(words)*32 == 256


@pytest.mark.skip
def test_sum_words():
    prg = PRG()
    w1, w2 = make_words(n=2)
    output1 = prg.sum_words(w1, w2)
    assert output1 == '00111010001110100011101000111001'

    w3 = '01001001'
    w4 = '10010010'
    output2 = prg.sum_words(w3, w4)
    assert output2 == '11011011'

    w5 = '11111111'
    w6 = '11111111'
    output3 = prg.sum_words(w5, w6)
    assert output3 == '11111110'


@pytest.mark.skip
def test_xor():
    # 10010101100101011001010110010101 <-- w1
    # 10100100101001001010010010100100 <-- w2
    # 00110001001100010011000100110001 <-- w1 xor w2
    prg = PRG()
    w1, w2 = make_words(n=2)
    output1 = prg.xor(w1, w2)
    assert output1 == '00110001001100010011000100110001' # '00110001'*4

    # 10010101 <-- w3
    # 11011110 <-- w4
    # 01001011 <-- w3 xor w4
    w3 = '10010101'
    w4 = '11011110'
    output2 = prg.xor(w3, w4)
    assert output2 == '01001011'

    output3 = prg.xor(w1, w4)
    assert output3 == '10010101100101011001010101001011'


@pytest.mark.skip
def test_binary_left_rotation():
    prg = PRG()
    w1 = make_words(n=1)
    output = prg.binary_left_rotation(w1, 6)
    assert output == '01100101011001010110010101100101'

    w2 = '11011011'
    output = prg.binary_left_rotation(w2, 3)
    assert output == '11011110'


@pytest.mark.skip
def test_quarter():
    """
    xor_a = 10010101
    add_a = 01001001
    add_b = 10010010

    add   = add_a + add_b
      01001001
    + 10010010
    = 11011011

    shift <<< 3
    11011011... <<< 3
    ...11011110

    xor
    11011110
    10010101
    01001011
    """
    prg = PRG()
    xor_a = '10010101'
    add_a = '01001001'
    add_b = '10010010'
    shift = 3
    output = prg.quarter(xor_a=xor_a, add_a=add_a, add_b=add_b, shift=shift)
    assert output == '01001011' # inverse shift --> '01111011'


def test_quarterround_function():
    prg = PRG()
    x = make_words(n=4)
    output = prg.quarterround_function(x)
    # Values not tested.
    assert type(output) is tuple
    assert output == ('10100000001010000010100100101001', '11111011111110111111101111111011', '00000110000001100000010000000110', '01101001001010010000100101101001')



### All tests below here are wrong/incomplete!!


def test_rowround_function():
    prg = PRG()

    # Create test variables.
    x = make_words(n=16)
    y0 = prg.quarterround_function(x[0:4])
    y1 = prg.quarterround_function(x[4:8])
    y2 = prg.quarterround_function(x[8:12])
    y3 = prg.quarterround_function(x[12:16])
    y = (y0, y1, y2, y3)
    assert type(y) is type(y0) is type(y1) is type(y2) is type(y3) is tuple
    
    # Unpack y.
    y_unpacked = []
    for words in y:
        for word in words:
            y_unpacked.append(word)
    assert type(y_unpacked) is list
    y_unpacked = tuple(y_unpacked)
    assert type(y_unpacked) is tuple
    assert len(y_unpacked) == 16
    
    # Run function tests.
    output = prg.rowround_function(x)
    assert type(output) is tuple
    assert len(output) == 16
    for element in output:
        assert type(element) is str
    
    # Compare output.
    assert output == y_unpacked


def test_columnround_function():
    prg = PRG()
    x = make_words(n=16)
    y0 = prg.quarterround_function( (x[0], x[4], x[8], x[12]) )
    y1 = prg.quarterround_function( (x[5], x[9], x[13], x[1]) )
    y2 = prg.quarterround_function( (x[10], x[14], x[2], x[6]) )
    y3 = prg.quarterround_function( (x[15], x[3], x[7], x[11]) )
    y = (y0, y1, y2, y3)
    assert type(y) is type(y0) is type(y1) is type(y2) is type(y3) is tuple
    
    # Unpack y.
    y_unpacked = []
    for words in y:
        for word in words:
            y_unpacked.append(word)
    assert len(y_unpacked) == 16
    y_unpacked = tuple(y_unpacked)

    # Run function tests.
    output = prg.columnround_function(x)
    assert type(output) is tuple
    assert len(output) == 16
    for element in output:
        assert type(element) is str
    
    # Compare output.
    assert output == y_unpacked


def test_doubleround_function():
    prg = PRG()
    x = make_words(n=16)
    verification = prg.columnround_function(x)
    verification = prg.rowround_function(verification)
    output = prg.doubleround_function(x)
    print(type(x))
    print(type(output))
    print(type(verification))
    assert type(output) is type(verification) is type(x) is tuple
    assert len(output) == len(verification) == len(x) == 16
    assert output == verification


def test_littleendian_function():
    prg = PRG()
    b  = '00000100000010000001000000100000'
    b_ = '00100000000100000000100000000100'
    output = prg.littleendian_function(b)
    assert output == b_


def test_hash_function():
    prg = PRG()
    words = make_words(n=16)
    output = prg.hash_function(words)
    assert type(output) is str
    assert len(words)*32 == len(output) == 512 # == 64 bytes * 8 bites/byte


def test_expansion_function():
    prg = PRG()
    
    key_16 = make_words(n=4, as_tuple=False)

    key_32 = make_words(n=8, as_tuple=False)
    key0_32 = key_32[0:128]
    key1_32 = key_32[128:256]
    
    n = make_words(n=4, as_tuple=False)

    output_16 = prg.expansion_function(key_16, key_16, n, False)
    output_32 = prg.expansion_function(key0_32, key1_32, n, True)
    
    assert len(output_16) == 512
    assert len(output_32) == 512
