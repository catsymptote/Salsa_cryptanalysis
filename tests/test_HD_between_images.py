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
    img1 = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/PTs/001/01_lg_PT.png'
    img2 = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/PTs/001/01_lg_PT.png'
    HD, bits = image_HD(img1, img2, return_bits=True)
    assert bits == 1572864
    assert HD == 0

    # Different images results in different values, and thus an HD well above 0.
    img1 = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/PTs/001/01_lg_PT.png'
    img2 = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001/01_lg_CT.png'
    #assert image_HD(img1, img2) > 0
    HD, bits = image_HD(img1, img2, return_bits=True)
    assert bits == 1572864
    assert HD == 774999


def test_get_images():
    directory = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001'
    images = [
        'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001\\01_lg_CT.png',
        'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001\\02_lg_CT.png',
        'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001\\03_lg_CT.png',
        'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001\\04_lg_CT.png',
        'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001\\05_lg_CT.png'
    ]
    assert get_images(directory) == images
