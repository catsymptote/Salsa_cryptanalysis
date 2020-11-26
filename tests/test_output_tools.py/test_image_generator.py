from output.image_generator import *


def roughly_equal(values:list, error:float = 0.9):
    """Values is a list of numbers.
    error is a float, which tells how close the
        values has to be to be accepted.
        0.9 means a 90% similarity."""
    for v1 in values:
        for v2 in values:
            if v1 < v2 * error:
                return False
    return True


def test_load_values():
    num, PTs, CTs = load_values(fil='tests\\assets\\test_csv.csv', max_count=3)
    assert type(num) == type(PTs) == type(CTs) == list
    assert len(num) == len(PTs) == len(CTs) == 3
    for i in range(len(num)):
        assert type(num[i]) is type(PTs[i]) is type(PTs[i]) is str
        assert len(num[i]) == 2
        assert len(PTs[i]) == len(PTs[i]) == 4


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


def create_bits():
    bits = ['1011' * 256] * 8
    assert type(bits) is list
    assert len(bits) == 8
    assert type(bits[0]) is str
    assert len(bits[0]) == 1024

    bits = create_bits(bits)
    assert type(bits) is str
    assert len(bits) == 8*256*4


def test_create_QR_rgb_bitmaps():
    """Same as test_create_rgb_bitmaps, but with
    different sizes."""
    bits = ['1011' * 32] * 8   # 8 full QRs.
    assert type(bits) is list
    assert len(bits) == 8
    assert type(bits[0]) is str
    assert len(bits[0]) == 128

    bitmaps = create_rgb_bitmaps(bits)
    assert type(bitmaps) is list
    assert len(bitmaps) == 1

    image = bitmaps[0]
    assert type(image) is list
    assert len(image) == 256

    row = bitmaps[0][0]
    assert type(row) is list
    assert len(image) == 256

    pixel = bitmaps[0][0][0]
    assert type(pixel) is list
    assert len(pixel) == 3

    bit = pixel[0]
    assert type(bit) is str
    assert len(bit) == 1
    assert bit == '0' or bit == '1'


def test_create_rgb_bitmaps():
    bits = ['1011' * 256] * 8   # 8 full PTs/CTs.
    assert type(bits) is list
    assert len(bits) == 8
    assert type(bits[0]) is str
    assert len(bits[0]) == 1024

    bitmaps = create_rgb_bitmaps(bits)
    assert type(bitmaps) is list
    assert len(bitmaps) == 1

    image = bitmaps[0]
    assert type(image) is list
    assert len(image) == 256

    row = bitmaps[0][0]
    assert type(row) is list
    assert len(image) == 256

    pixel = bitmaps[0][0][0]
    assert type(pixel) is list
    assert len(pixel) == 3

    bit = pixel[0]
    assert type(bit) is str
    assert len(bit) == 1
    assert bit == '0' or bit == '1'

    r = 0
    g = 0
    b = 0
    for img in bitmaps:
        for bit_row in img:
            for pix in bit_row:
                assert type(pix) is list
                assert len(pix) == 3
                #print(pix)
                if pix[0] == '1':
                    r += 1
                if pix[1] == '1':
                    g += 1
                if pix[2] == '1':
                    b += 1
    
    # Assert the values are roughly equal.
    assert roughly_equal([r, g, b])


def create_rgb_image_file():
    bits = ['1011' * 256] * 16
    bitmap = create_bitmaps(bits)[0]
    img = create_image_file(bitmap)
    
    assert type(img) is list
    assert len(img) == 256
    assert type(img[0]) is tuple
    assert len(img[0]) == 768
    assert type(img[0][0]) is int
    assert img[0][0] == 255
    assert img[0][96] == 0


def test_create_QR_bitmaps():
    bits = ['1011' * 32] * 8
    assert type(bits) is list
    assert len(bits) == 8
    assert type(bits[0]) is str
    assert len(bits[0]) == 128

    bitmaps = create_QR_bitmaps(bits)
    assert type(bitmaps) is list
    assert len(bitmaps) == 1
    assert type(bitmaps[0]) is list
    assert len(bitmaps[0]) == 256
    assert type(bitmaps[0][0]) is list
    assert len(bitmaps[0][0]) == 256
    assert type(bitmaps[0][0][0]) is str
    assert len(bitmaps[0][0][0]) == 1
    assert bitmaps[0][0][0] == '0' or bitmaps[0][0][0] == '1'


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
    assert name_formatter('tests', 'assets', 13) == 'output_folder/PT/13.png'
