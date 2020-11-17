from output.image_generator import *


def test_create_image_structure():
    bits = '00001111000011110101'
    assert create_image_structure(bits) == ['00001111', '00001111', '0101']


def test_load_values():
    num, PTs, CTs = load_values(fil='output/compiled_list.csv', max_count=3)
    assert type(num) == type(PTs) == type(CTs) == list
    assert len(num) == len(PTs) == len(CTs) == 3


def test_name_formatter():
    assert name_formatter('PT', 13) == 'output_images/PT/13.png'
