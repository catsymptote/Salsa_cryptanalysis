from tools.export_pairs import Pair_exporter
from salsa.salsa20 import Salsa20
from tools.binary import Binary
from salsa.QR_function import QR
import random


lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
chars = lowercase_chars + lowercase_chars.upper() + '0123456789'


def gen_random_string(length):
    string = ''
    for i in range(length):
        string += random.choice(chars)
    return string


def gen_random_QR():
    X = []
    for i in range(4):
        word = ''
        for j in range(32):
            bit = random.choice(['0', '1'])
            word += bit
        X.append(word)
    return tuple(X)


def QR_to_binary(X):
    string = ''
    for word in X:
        string += word
    return string


def to_binary(text):
    #res = ''.join(format(ord(i), 'b') for i in text)
    binary = ''
    for char in text:
        tmp = format(ord(char), 'b')
        while len(tmp) < 8:
            tmp = '0' + tmp
        if len(tmp) > 8:
            tmp = tmp[0:8]
        binary += tmp

        #binary += '{0:07b}'.format(text)
        #binary += bin(bytearray(char, 'utf8'))
    #print(binary)
    return binary


def get_plaintext(number):
    binary = Binary(number)

    # Random chars:
    #string = gen_random_string(length=128)

    # Random binary values:
    #binary.gen_random(word_size=128)
    #string = binary.bits

    # Counting values:
    string = binary.get_bin(word_size=128)

    return string


def get_key():
    return '10101000110011101100011100000111101110010001100101111011100000110111000110010100100100010001101110101011011101001001111111000100'


def get_nonce():
    return '1110011111101101011001111111110101011100110101001010101101110001'


def run():
    sa = Salsa20(static_nonce=get_nonce())
    key = get_key()

    pe = Pair_exporter()

    lines = 1000
    files = 2
    for i in range(files):
        #print(pe.status_scan())
        #new_num = pe.status_scan() + lines
        
        output = ''
        last_num = pe.status_scan()
        new_num = last_num + lines
        for j in range(lines):
            current_pair = new_num + j #i*lines + j + last_num
            pt = gen_random_string(128)
            ct, nonce = sa.encrypt(pt, key)
            assert len(pt) == len(ct) == 128
            #print(len(pt), len(ct))
            #print(len(to_binary(pt)), len(to_binary(ct)))
            #print()
            #output += str(current_pair) + ',\t' + to_binary(pt) + ',\t' + to_binary(ct) + '\n'
            output += str(current_pair) + ',\t' + to_binary(pt) + ',\t' + to_binary(ct) + '\n'
        
        pe.store(output, new_num)


def run_QR():
    key = get_key()

    pe = Pair_exporter()

    lines = 1000
    files = 1000
    for i in range(files):
        #print(pe.status_scan())
        #new_num = pe.status_scan() + lines
        
        output = ''
        last_num = pe.status_scan()
        new_num = last_num + lines
        for j in range(lines):
            current_pair = new_num + j #i*lines + j + last_num
            X = gen_random_QR()
            Y = QR(X)
            assert len(X) == len(Y) == 4
            assert len(X[0]) == len(Y[0]) == 32
            output += str(current_pair) + ',\t' + QR_to_binary(X) + ',\t' + QR_to_binary(Y) + '\n'
        
        pe.store(output, new_num)


def run_random():
    pe = Pair_exporter()

    lines = 1000
    files = 1000
    for i in range(files):
        output = ''
        last_num = pe.status_scan()
        new_num = last_num + lines
        for j in range(lines):
            current_pair = new_num + j #i*lines + j + last_num
            a = ''
            b = ''
            for i in range(1024):
                a += random.choice(['0', '1'])
                b += random.choice(['0', '1'])
            assert len(a) == len(b) == 1024
            output += str(current_pair) + ',\t' + a + ',\t' + b + '\n'
        
        pe.store(output, new_num)


if __name__ == '__main__':
    run_random()
