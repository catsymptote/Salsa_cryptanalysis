from science.cryptography_tools import *
from science.hamming_weight import *
from science.format_tools import *
from science.plot_tools import *
from salsa.salsa20 import Salsa20
from salsa.prg import PRG
from QR_attack_1 import *


def to_bin(val):
    # Convert to byte list.
    byte_list = ' '.join(format(ord(x), 'b') for x in val)
    byte_list = byte_list.split(' ')

    # Padding.
    for i in range(len(byte_list)):
        byte_list[i] = padder(byte_list[i], 7)
    
    binary = ''.join(byte_list)
    return binary


def padder(num, size=8):
    if len(num) < size:
        num = '0'*(size-len(num)) + num
    elif len(num) > size:
        num = num[0:size]
    return num


def average_list(values:list):
    """values is a list of lists."""
    
    for i in range(len(values)):
        total = 0
        for item in values[i]:
            total += item
        values[i] = total/len(values[i])
    return values
        

def average_list_2(values:list):
    """values is a list of lists."""
    list_lengths = len(values[0])
    avgs = [0] * list_lengths

    for lst in range(len(values)):
        for item in range(len(values[lst])):
            avgs[item] += values[lst][item]
    
    for i in range(len(avgs)):
        avgs[i] /= len(values)

    return avgs


def compare_salsa_with_similar_inputs(flips):
    prg = PRG()

    #key = '0' * 256
    key = get_random_binary(256)
    key0 = key[:128]
    key1 = key[128:]
    nonce = get_random_binary(128)
    IV_0, IV_1, IV_2, IV_3 = prg.a_vects
    original_hash_input = IV_0 + key0 + IV_1 + nonce + IV_2 + key1 + IV_3
    original_hash_output = prg.expansion_function(key0, key1, nonce, full_key=True)

    in_out_HDs = []
    in_in_HDs = []
    out_out_HDs = []
    
    for flip in range(flips):
        key0 = key[:128]
        key1 = key[128:]
        hash_output = prg.expansion_function(key0, key1, nonce, full_key=True)
        hash_input = IV_0 + key0 + IV_1 + nonce + IV_2 + key1 + IV_3

        in_out_HD = hamming_distance(hash_output, hash_input)
        in_out_HDs.append(in_out_HD)

        in_in_HD = hamming_distance(original_hash_input, hash_input)
        in_in_HDs.append(in_in_HD)

        #out_out_HD = hamming_distance(original_hash_output, hash_input)
        #out_out_HDs.append(out_out_HD)
        out_out_HDs.append(256)

        key = flip_random_bit(key)
        

    return in_out_HDs, in_in_HDs, out_out_HDs
    


def average_salsa_HD(flips, avg_runs):
    in_out_HDs_list = []
    in_in_HDs_list = []
    out_out_HDs_list = []

    for run in range(avg_runs):
        in_out_HDs, in_in_HDs, out_out_HDs = compare_salsa_with_similar_inputs(flips)

        in_out_HDs_list.append(in_out_HDs)
        in_in_HDs_list.append(in_in_HDs)
        out_out_HDs_list.append(out_out_HDs)
    
    in_out_HDs_avg = average_list_2(in_out_HDs_list)
    in_in_HDs_avg = average_list_2(in_in_HDs_list)
    out_out_HDs_avg = average_list_2(out_out_HDs_list)

    multi_line_chart([in_out_HDs_avg, in_in_HDs_avg, out_out_HDs_avg], x_label='bits flipped', y_label='HD')#, enc_avg])#, vertical_lines=[int(num_of_keys/2)])

    """
    X_0_str = get_random_binary(size) #'0'*32
    #X_0 = '11111111111111111111111111111111'
    X_0 = str_to_list(X_0_str)
    Y_0 = crypt.use_QRF(X_0)
    Y_0_str = list_to_str(Y_0)

    keys = []
    for i in range(num_of_keys):
        keys.append(get_random_binary(size))
    
    for i in range(int(num_of_keys/2)):
        keys[i] = flip_random_bit(X_0_str, amount=int(i/5))

    
    #keys[0] = flip_random_bit(X_0_str, amount=1)
    #keys[1] = flip_random_bit(X_0_str, amount=3)
    #eys[2] = flip_random_bit(X_0_str, amount=7)
    #keys[3] = flip_random_bit(X_0_str, amount=10)
    #keys[4] = flip_random_bit(X_0_str, amount=15)
    
    HD_X = []
    HD_Y = []

    for i in range(len(keys)):
        X_str = keys[i]
        X = str_to_list(X_str)
        #print(X)
        Y = crypt.use_QRF(X)
        Y_str = list_to_str(Y)

        HD_X.append(hamming_distance(X_str, X_0_str))
        HD_Y.append(hamming_distance(Y_str, Y_0_str))
    
    #print(HD_X, '\n', HD_Y)
    multi_line_chart([HD_X, HD_Y], vertical_lines=[int(num_of_keys/2)])

    #return HD_X, HD_Y
"""

if __name__ == '__main__':
    average_salsa_HD(64, 5)
