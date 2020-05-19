from science.cryptography_tools import *
from science.hamming_weight import *
from science.format_tools import *
from science.plot_tools import *
from QR_attack_1 import *


def compare_QR_with_similar_Xs(num_of_keys=10):
    crypt = Crypto_Tools()
    size = 32
    X_0_str = get_random_binary(32) #'0'*32
    #X_0 = '11111111111111111111111111111111'
    X_0 = str_to_list(X_0_str)
    Y_0 = crypt.use_QRF(X_0)
    Y_0_str = list_to_str(Y_0)

    keys = []
    for i in range(num_of_keys):
        keys.append(get_random_binary(size))
    
    for i in range(int(num_of_keys/2)):
        keys[i] = flip_random_bit(X_0_str, amount=int(i/5))

    """
    keys[0] = flip_random_bit(X_0_str, amount=1)
    keys[1] = flip_random_bit(X_0_str, amount=3)
    keys[2] = flip_random_bit(X_0_str, amount=7)
    keys[3] = flip_random_bit(X_0_str, amount=10)
    keys[4] = flip_random_bit(X_0_str, amount=15)
    """
    HD_X = []
    HD_Y = []

    for i in range(len(keys)):
        X_str = keys[i]
        X = str_to_list(X_str)
        print(X)
        Y = crypt.use_QRF(X)
        Y_str = list_to_str(Y)

        HD_X.append(hamming_distance(X_str, X_0_str))
        HD_Y.append(hamming_distance(Y_str, Y_0_str))
    
    print(HD_X, '\n', HD_Y)
    multi_line_chart([HD_X, HD_Y], vertical_lines=[int(num_of_keys/2)])

    #return HD_X, HD_Y


if __name__ == '__main__':
    compare_QR_with_similar_Xs(256)
