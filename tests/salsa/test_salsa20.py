import pytest
from salsa.salsa20 import Salsa20
from salsa.prg import PRG
import random


def test_init():
    sal1 = Salsa20()

    stat_nonce = '11011011'*16
    sal2 = Salsa20(mode='test', static_nonce=stat_nonce)

    assert type(sal1) is type(sal2) is Salsa20
    assert type(sal1.prg) is type(sal2.prg) is PRG

    assert sal1.static_nonce == None
    assert sal2.static_nonce == stat_nonce



def test_encrypt():
    # Setup
    sal = Salsa20()
    plaintext = 'Hello World!'
    key = '10010110'*16

    # Test 1
    ciphertext_1, nonce_1 = sal.encrypt(plaintext, key)
    assert type(ciphertext_1) is str
    assert len(ciphertext_1) == 64
    assert type(nonce_1) is str
    assert len(nonce_1) == 64

    # Test 2
    input_nonce_2 = sal.generate_nonce()

    ciphertext_2, nonce_2 = sal.encrypt(plaintext, key, input_nonce_2)
    assert type(ciphertext_1) is str
    assert len(ciphertext_1) == 64
    assert type(nonce_1) is str
    assert len(nonce_1) == 64
    assert nonce_2 == input_nonce_2

    # Combined test
    assert ciphertext_1 != ciphertext_2
    assert nonce_1 != nonce_2


def test_decrypt():
    sal = Salsa20()
    plaintext = 'Hello World!'
    key = '10010110'*16
    ciphertext, nonce = sal.encrypt(plaintext, key)
    decrypted = sal.decrypt(ciphertext, key, nonce)
    assert len(ciphertext) == 64


#@pytest.mark.integration_test
def full_crypto(p_size, key_size, nonce=None):
    sal = Salsa20()

    # Generate random plaintext
    plaintext = ''
    for i in range(p_size):
        plaintext += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Generate random key
    key = ''
    for i in range(key_size):
        key += random.choice('01')

    # Encrypt --> decrypt --> return.
    ciphertext, nonce = sal.encrypt(plaintext, key, nonce)
    decrypted_plaintext = sal.decrypt(ciphertext, key, nonce)
    return plaintext, decrypted_plaintext


@pytest.mark.integration_test
def test_full_crypto():
    # Small data set, full-key
    a1, a2 = full_crypto(1, 256)
    assert a1 == a2

    # Small data set, half-key
    b1, b2 = full_crypto(1, 128)
    assert b1 == b2

    # Large data set, full-key
    c1, c2 = full_crypto(1024, 256)
    assert c1 == c2

    # Irregular sized plaintext 1
    d1, d2 = full_crypto(666, 128)
    assert d1 == d2

    # Irregular sized plaintext 2
    e1, e2 = full_crypto(129, 256)
    assert e1 == e2


def test_readable_full_crypto():
    # Setup
    sal = Salsa20()
    plaintext = "Hello World! How are ye doin' today, matey?"
    
    key = ''
    for i in range(256):
        key += random.choice('01')
    
    # Encrypt --> decrypt --> test.
    ciphertext, nonce = sal.encrypt(plaintext, key)
    decrypted_plaintext = sal.decrypt(ciphertext, key, nonce)
    assert plaintext == decrypted_plaintext


def test_xor():
    sal = Salsa20()
    a = '01101001'
    b = '01010100'
    c = '00111101'
    assert sal.xor(a, b) == c


def test_add_padding():
    sal = Salsa20()
    a = '01101001'
    b = sal.add_padding(a)
    assert len(b) == 512
    for i in range(512-len(a)):
        assert b[i + len(a)] == '0'
    assert b[0:8] == a


def test_remove_padding():
    sal = Salsa20()
    a = '01000001'
    b = a + '00000000'*63
    assert sal.remove_padding(b) == a


def test_to_binary():
    sal = Salsa20()
    text = 'ABCD'
    binary = sal.to_binary(text)
    assert binary == '01000001010000100100001101000100'


def test_to_text():
    sal = Salsa20()
    binary = '01000001010000100100001101000100'
    text = sal.to_text(binary)
    assert text == 'ABCD'


def test_generate_block_number():
    sal = Salsa20()
    number = 1234
    binary_number = sal.generate_block_number(number)
    assert type(binary_number) is str
    assert len(binary_number) == 64
    assert binary_number == '0000000000000000000000000000000000000000000000000000010011010010'


def test_generate_nonce():
    sal = Salsa20()
    nonce = sal.generate_nonce()
    assert type(nonce) is str
    assert len(nonce) == 64

    for char in nonce:
        assert char == '0' or char == '1'
    
    nonce_list = []
    for i in range(100):
        nonce_list.append(sal.generate_nonce())
    
    nonce_set = set(nonce_list)
    assert len(nonce_list) == len(nonce_set)


def test_mode():
    data = 'Hello World!'
    stat_nonce = '11011011'*16
    key = '10010110'*16

    sal1 = Salsa20()
    sal2 = Salsa20(static_nonce=stat_nonce, mode='test')

    assert sal1.mode == 'full'
    assert sal2.mode == 'test'

    ct1, nonce1 = sal1.encrypt(data, key)
    ct2, nonce2 = sal2.encrypt(data, key)

    assert ct1 != ct2
    assert nonce1 != nonce2
