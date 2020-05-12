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
