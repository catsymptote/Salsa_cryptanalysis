from HD_between_images import *
import pytest


def test_pad_binary():
    a = '010'
    b = '10010110'
    c = '000010101001'
    assert pad_binary(a) == '00000010'
    assert pad_binary(b) == '10010110'
    assert pad_binary(c) == '10101001'


@pytest.mark.integration_test
def test_image_HD():
    # Same image results in 0.
    img1 = 'tests\\assets\\test_image_arch.png'
    img2 = 'tests\\assets\\test_image_arch.png'
    HD, bits = image_HD(img1, img2, return_bits=True)
    assert bits == 393216
    assert HD == 0

    # Different images results in different values, and thus an HD well above 0.
    img1 = 'tests\\assets\\test_image_arch.png'
    img2 = 'tests\\assets\\test_image_kali.png'
    #assert image_HD(img1, img2) > 0
    HD, bits = image_HD(img1, img2, return_bits=True)
    assert bits == 393216
    assert HD == 324387


def test_get_images():
    directory = 'tests\\assets'
    images = [
        'tests\\assets\\test_image_arch.png',
        'tests\\assets\\test_image_kali.png'
    ]
    assert get_images(directory) == images
