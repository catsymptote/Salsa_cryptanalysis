from salsa.salsa20 import Salsa20
from science.format_tools import to_bytes
import math


def print_list_of_lists(x, print_index:bool = True):
    for i in range(len(x)):
        if print_index:
            print(i, end=':\t')
        for word in x[i]:
            print(to_bytes(word), end=' ')
        print()




# Setup
stat_nonce = '0' * 128 #'11011011'*16
message = '0' #'Hello World!'
key = '1' * 128 #'10010010'*16

sal = Salsa20(mode='test', static_nonce=stat_nonce)


# Encrypt.
ciphertext = sal.encrypt(message, key)


# Get and print the values internal QR values.
QR_x = sal.prg.QR_x
QR_y = sal.prg.QR_y
DRF_in = sal.prg.DRF_in
assert len(QR_x) == len(QR_y) == 80
assert len(DRF_in) == 10

print_list_of_lists(QR_x)
