from tools.export_pairs import Pair_exporter
from salsa.salsa20 import Salsa20
from tools.binary import Binary
import random


lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
chars = lowercase_chars + lowercase_chars.upper() + '0123456789'


def gen_random_string(length):
    string = ''
    for i in range(length):
        string += random.choice(chars)
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
    files = 100
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


if __name__ == '__main__':
    run()
