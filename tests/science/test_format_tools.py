from science.format_tools import *


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


def test_flip_bits():
    bits    = '1010010'
    flipped = '0101101'
    assert flip_bits(bits) == flipped


def test_flip_bits_in_word():
    bits            = '1010010'

    flipped_last_2  = '1010001'
    flipped_last_3  = '1010101'
    flipped_all     = '0101101'
    
    assert flip_bits_in_word(bits, amount=2) == flipped_last_2
    assert flip_bits_in_word(bits, amount=3) == flipped_last_3
    assert flip_bits_in_word(bits) == flipped_all
