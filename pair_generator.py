from tools.export_pairs import Pair_exporter
from salsa.salsa20 import Salsa20
from tools.binary import Binary


def to_binary(text):
    res = ''.join(format(ord(i), 'b') for i in text)
    return res


def get_plaintext(number):
    binary = Binary(number)
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
    files = 496
    for i in range(files):
        #print(pe.status_scan())
        #new_num = pe.status_scan() + lines
        
        output = ''
        last_num = pe.status_scan()
        new_num = last_num + lines
        for j in range(lines):
            current_pair = new_num + j #i*lines + j + last_num
            pt = get_plaintext(current_pair)
            ct, nonce = sa.encrypt(pt, key)
            output += str(current_pair) + ',\t' + to_binary(pt) + ',\t' + to_binary(ct) + '\n'
        pe.store(output, new_num)


if __name__ == '__main__':
    run()
