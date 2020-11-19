from output.image_generator import *


def test_load_values():
    num, PTs, CTs = load_values(fil='output/random_compiled_list.csv', max_count=3)
    assert type(num) == type(PTs) == type(CTs) == list
    assert len(num) == len(PTs) == len(CTs) == 3


def test_padder():
    bits1 = '1001'
    bits2 = '10100101' * 200
    bits3 = '1001' * 256
    assert len(bits1) == 4
    assert len(bits2) == 1600
    assert len(bits3) == 1024
    assert len(padder(bits1)) == 1024
    assert len(padder(bits2)) == 1024
    assert len(padder(bits3)) == 1024

    assert padder(bits1) == '0' * 1020 + '1001'
    assert padder(bits2) == '10100101' * 128
    assert padder(bits3) == '1001' * 256


def test_create_bitmaps():
    bits = ['101' * 256] * 8
    assert type(bits) is list
    assert len(bits) == 8
    assert type(bits[0]) is str
    assert len(bits[0]) == 768

    bitmaps = create_bitmaps(bits)
    assert type(bitmaps) is list
    assert len(bitmaps) == 1
    assert type(bitmaps[0]) is list
    assert len(bitmaps[0]) == 256
    assert type(bitmaps[0][0]) is list
    assert len(bitmaps[0][0]) == 256
    assert type(bitmaps[0][0][0]) is str
    assert len(bitmaps[0][0][0]) == 1
    assert bitmaps[0][0][0] == '0' or bitmaps[0][0][0] == '1'


def test_create_image_file():
    bits = ['1011' * 256] * 8
    bitmap = create_bitmaps(bits)[0]
    img = create_image_file(bitmap)
    
    assert type(img) is list
    assert len(img) == 256
    assert type(img[0]) is tuple
    assert len(img[0]) == 768
    assert type(img[0][0]) is int
    assert img[0][0] == 255
    assert img[0][96] == 0


def test_name_formatter():
    assert name_formatter('PT', 13) == 'random_images/PT/13.png'
