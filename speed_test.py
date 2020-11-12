from salsa.salsa20 import Salsa20
from salsa.QR_function import QR, QR_chacha

import random
import time


def QR_setup(amount, size):
    """Create *amount* number of binary numbers,
    or size *size*."""
    Xs = []
    size = int(size/4)
    for i in range(amount):
        X = [None, None, None, None]
        for j in range(4):
            binary = ''
            for k in range(size):
                binary += random.choice(['0', '1'])
            X[j] = binary
        Xs.append(tuple(X))
    return Xs


def Salsa20_setup(amount, size, key_size):
    """Create *amount* of plaintext, of size *size*,
    with keys of size key_size (16 or 32 bytes)."""
    binaries = []
    keys = []
    nonces = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chars = alphabet + alphabet.upper()
    chars = list(chars)
    for i in range(amount):
        binary = ''
        key = ''
        nonce = ''

        for j in range(size):
            binary += random.choice(chars)
        for k in range(key_size):
            key += random.choice(['0', '1'])
        for l in range(64):
            nonce += random.choice(['0', '1'])
        
        binaries.append(binary)
        keys.append(key)
        nonces.append(nonce)
    return binaries, keys, nonces


def QR_test(binary_numbers:list, function):
    # Start time
    start = time.time()
    
    for i in range(len(binary_numbers)):
        tmp = function(binary_numbers[i])
    
    # End time
    end = time.time()
    total = end - start
    return total


def Salsa20_test(binary_numbers:list, keys:list, nonces:list, function):
    # Start time
    stf = []
    start = time.time()

    for i in range(len(binary_numbers)):
        tmp = function(binary_numbers[i], keys[i], nonces[i])
        stf.append(tmp)
    
    # End time
    end = time.time()
    total = end - start
    return total


def run_QR():
    runs = 100000
    binary_numbers = QR_setup(runs, 128)
    total_time = QR_test(binary_numbers, QR)
    return runs, total_time, runs/total_time


def run_ChaCha_QR():
    runs = 100000
    binary_numbers = QR_setup(runs, 128)
    total_time = QR_test(binary_numbers, QR_chacha)
    return runs, total_time, runs/total_time


def run_Salsa20():
    runs = 100
    sal = Salsa20()
    binary_numbers, keys, nonces = Salsa20_setup(runs, 512, 256)
    total_time = Salsa20_test(binary_numbers, keys, nonces, sal.encrypt)
    return runs, total_time, runs/total_time


def run_Salsa20_decrypt():
    runs = 100
    sal = Salsa20()
    binary_numbers, keys, nonces = Salsa20_setup(runs, 512, 256)
    total_time = Salsa20_test(binary_numbers, keys, nonces, sal.decrypt)
    return runs, total_time, runs/total_time


if __name__ == '__main__':
    QR_time = run_QR()
    QR_ChaCha_time = run_ChaCha_QR()
    Salsa_time = run_Salsa20()
    Salsa_decrypt_time = run_Salsa20_decrypt()
    print('runs, total_time, runs/total_time')
    print(QR_time)
    print(QR_ChaCha_time)
    print(Salsa_time)
    print(Salsa_decrypt_time)
