from science.format_tools import *
from science.hamming_weight import *


def test_add_padding():
    text1 = '110110110110'
    text2 = '49f1e'
    text3 = 'Hi there'

    assert add_padding(text1, 20) == '00000000110110110110'
    assert add_padding(text2, 8) == '00049f1e'
    assert add_padding(text3, 10, '-') == '--Hi there'


def test_split_string():
    text1 = '1101101101101101'
    text2 = '110110110110110111011011'
    text3 = '110110110110'
    text4 = '110'

    assert split_string(text1, 8) == '11011011 01101101'
    assert split_string(text2, 4) == '1101 1011 0110 1101 1101 1011'
    assert split_string(text3, 8) == '00001101 10110110'
    assert split_string(text4, 8) == '00000110'


################
## Convertion ##
################

def test_to_hex():
    text1 = '00000000'
    text2 = '11111111'
    text3 = '110110110110110111011011'
    num1 = 6
    num2 = 32
    num3 = 128
    num4 = 150000000000

    assert to_hex(text1) == '0'
    assert to_hex(text2) == 'ff'
    assert to_hex(text3) == 'db6ddb'
    assert to_hex(num1)  == '6'
    assert to_hex(num2)  == '20'
    assert to_hex(num3)  == '80'
    assert to_hex(num4)  == '22ecb25c00'


def test_to_bytes():
    text1 = '000'
    text2 = '11111111'
    text3 = '110110110110110111011011'
    num1 = 6
    num2 = 32
    num3 = 128
    num4 = 150000000000

    assert to_bytes(text1) == '00000000'
    assert to_bytes(text2) == '000000ff'
    assert to_bytes(text3) == '00db6ddb'
    assert to_bytes(num1)  == '00000006'
    assert to_bytes(num2)  == '00000020'
    assert to_bytes(num3)  == '00000080'
    assert to_bytes(num4)  == '00000022 ecb25c00'


def test_to_ints():
    a = ['0110', '1001']
    b = ['0101', '1010']
    x = [a, b]
    y = to_ints(x)

    assert len(y) == 2
    assert len(y[0]) == 2
    assert len(y[1]) == 2

    assert y[0][0] == 6
    assert y[0][1] == 9
    assert y[1][0] == 5
    assert y[1][1] == 10


def test_flatten_list():
    X = ['1111', '1100', '1010']
    Y = ['1010', '1100', '1111']
    Z = ('1010', '1111', '0000')
    XYZ = (X, Y, Z)
    ZYX = [X, Y, Z]
    expected = ['1111', '1100', '1010', '1010', '1100', '1111', '1010', '1111', '0000']

    res_XYZ = flatten_list(XYZ)
    res_YZX = flatten_list(ZYX)

    assert type(res_XYZ) is type(res_YZX) is list
    assert len(res_XYZ) == len(res_YZX) == 9
    assert res_XYZ == res_YZX == expected


def test_list_to_str():
    X = ('1111', '1100', '1010')
    Y = ['1111', '1100', '1010']
    Z = '111111001010'
    assert list_to_str(X) == Z
    assert list_to_str(Y) == Z


def test_str_to_list():
    a = '1010'
    b = '1111000011110000'
    assert str_to_list(a) == ('1', '0', '1', '0')
    assert str_to_list(b) == ('1111', '0000', '1111', '0000')


#################
## Type checks ##
#################

def test_is_binary():
    # Binary
    b_1 = '011001'
    b_2 = '1'
    b_3 = '0'
    b_4 = '11111'
    b_5 = '00000'
    b_6 = '100010100100010010100101'

    # Hex
    h_1 = '18ed7dfa'
    h_2 = '1004101'

    # Other string/number
    i_1 = 101001
    i_2 = 12345
    s_1 = 'kake'
    s_2 = '15g4'
    
    assert is_binary(b_1)
    assert is_binary(b_2)
    assert is_binary(b_3)
    assert is_binary(b_4)
    assert is_binary(b_5)
    assert is_binary(b_6)

    assert not is_binary(h_1)
    assert not is_binary(h_2)
    assert not is_binary(i_1)
    assert not is_binary(i_2)
    assert not is_binary(s_1)
    assert not is_binary(s_2)


def test_is_hex():
    pass


############
## Prints ##
############

def test_print_list_of_lists():
    x0 = ['1001', '0110']
    x1 = ['1010', '0101']
    X = [x0, x1]
    results = print_list_of_lists(X)
    assert type(results) is type(None)


def test_tab_print():
    X = ['1001', '0110', '1010', '0101']
    results = print_list_of_lists(X)
    assert type(results) is type(None)


################
## Generators ##
################

def test_get_random_binary():
    binary = get_random_binary(128)
    assert type(binary) is str
    assert len(binary) == 128
    for bit in binary:
        assert bit == '0' or bit == '1'


def test_flip_n_bits():
    a = '00000000'
    b = '1001010101001010'
    c = '0000000000000000'

    a_ = flip_n_bits(a, 1)
    b_ = flip_n_bits(b, 1)
    a__ = flip_n_bits(a, 5)
    b__ = flip_n_bits(b, 7)
    c_ = flip_n_bits(c, 15)

    assert hamming_distance(a, a_) == 1
    assert hamming_distance(a, a__) == 5
    assert hamming_distance(b, b_) == 1
    assert hamming_distance(b, b__) == 7
    assert hamming_distance(c, c_) == 15


def test_flip_random_bit():
    X_0 = '10101010'
    X_1 = ('1010', '0101', '1001', '0100')

    flipped_0 = flip_random_bit(X_0)
    flipped_1 = flip_random_bit(X_1)
    
    HD_0 = hamming_distance(X_0, flipped_0)
    
    HD_1 = 0
    for i in range(len(X_1)):
        HD_1 += hamming_distance(X_1[i], flipped_1[i])

    assert HD_0 == -1 or HD_0 == 1
    assert HD_1 == -1 or HD_1 == 1

    for i in range(10):
        flipped_0_multi = flip_random_bit(X_0, amount=4)
        HD_0_multi = hamming_distance(X_0, flipped_0_multi)
        assert HD_0_multi in [-4, -2, 0, 2, 4]


def test_flip_bits():
    bits    = '1010010'
    flipped = '0101101'
    assert flip_bits(bits) == flipped


def test_flip_bit_at():
    bits_0 = '00000000'
    assert flip_bit_at(bits_0, 0) == '10000000'
    assert flip_bit_at(bits_0, 1) == '01000000'
    assert flip_bit_at(bits_0, 2) == '00100000'
    assert flip_bit_at(bits_0, 3) == '00010000'
    assert flip_bit_at(bits_0, 7) == '00000001'

    bits_1 = ('0000', '0000')
    assert flip_bit_at(bits_1, 0) == ('1000', '0000')
    assert flip_bit_at(bits_1, 1) == ('0100', '0000')
    assert flip_bit_at(bits_1, 6) == ('0000', '0010')
    assert flip_bit_at(bits_1, 7) == ('0000', '0001')


def test_flip_bits_in_word():
    bits            = '1010010'

    flipped_last_2  = '1010001'
    flipped_last_3  = '1010101'
    flipped_all     = '0101101'
    
    assert flip_bits_in_word(bits, amount=2) == flipped_last_2
    assert flip_bits_in_word(bits, amount=3) == flipped_last_3
    assert flip_bits_in_word(bits) == flipped_all


def test_increment_bits():
    a   = '00001101'
    A   =     '1101'
    a_  = '00001110'
    A_   =    '1110'
    a__ = '00001111'
    A__ =     '1111'
    a___= '00010000'
    A___=    '10000'
    assert increment_bits(a) == A_
    assert increment_bits(a_) == A__
    assert increment_bits(a__) == A___


def test_increment_QR_X():
    X = ('0000', '0000', '0000', '0000')
    X_ = ('0000', '0000', '0000', '0001')
    X__= ('0000', '0000', '0000', '0010')
    X_64 = ('0000', '0000', '0100', '0000')

    assert increment_QR_X(X) == X_
    assert increment_QR_X(X_) == X__
    assert increment_QR_X(X, step=2) == X__
    assert increment_QR_X(X, step=64) == X_64
