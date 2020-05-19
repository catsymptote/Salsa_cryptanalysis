from science.cryptography_tools import *
from science.hamming_weight import *
from science.format_tools import *
from science.plot_tools import *
from science.math_tools import *
from science.Pearson_correlation import *


def QR(X):
    if type(X) is str:
        X = str_to_list(X)
    Y = Crypto_Tools().use_QRF(X)
    return list_to_str(Y)


def is_closer(new_X, old_X, Y):
    new_HD = hamming_distance(QR(new_X), Y)
    old_HD = hamming_distance(QR(old_X), Y)
    if new_HD < old_HD:
        print(new_HD)
        return True
    return False


def try_bit_flip(bits, Y, attempts=50, flips=1):
    is_list = False
    if type(bits) is not str:
        is_list = True
        bits = list_to_str(bits)
    
    flipped = flip_random_bit(bits)
    for i in range(flips - 1):
        flipped = flip_random_bit(flipped)
    
    counter = 0
    while hamming_distance(QR(flipped), Y) >= hamming_distance(QR(bits), Y):
        flipped = flip_random_bit(bits)

        counter += 1
        if counter > attempts:
            return bits
    
    bits = flipped
    
    if is_list:
        bits = str_to_list(bits)
    
    return bits


def follow_key(X, Y, attempts_per_key):
    for i in range(attempts_per_key):
        if QR(X) == Y:
            print('Yay!')
            return X, True

        new_X = flip_random_bit(X)
        if is_closer(new_X, X, Y):
            X = new_X
        
    return X, False


def attack(Y:str, bits:int, num_of_keys=50, attempts_per_key=50):
    keys = []
    for i in range(num_of_keys):
        keys.append(str_to_list(get_random_binary(bits)))

    for key in keys:
        X, solved = follow_key(X=key, Y=Y, attempts_per_key=attempts_per_key)
        if solved:
            return X

    print('Unsuccessful :(')
    return None


if __name__ == '__main__':
    bits = 512
    crypt = Crypto_Tools()
    X = get_random_binary(bits)
    Y = QR(X)
    recovered_state = attack(Y=Y, bits=bits, num_of_keys=50, attempts_per_key=50)
    print('Key:\t', X)
    print('Guess:\t', recovered_state)
