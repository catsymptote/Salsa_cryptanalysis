from salsa.salsa20 import Salsa20
from science.format_tools import *
from science.science_tools import *
from science.Pearson_correlation import Pearson_correlation, Pearson_on_list_of_lists

import math



def compare_multiple_keys(amount_of_test_values=100, QR_depth_index=0):
    # Setup
    stat_nonce = '0' * 128
    message = '0'
    key = '1' + '0' * 127
    assert len(key) == len(stat_nonce) == 128

    # Get QR from key.
    sal = Salsa20(mode='test', static_nonce=stat_nonce)
    ciphertext = sal.encrypt(message, key)
    QR_0 = sal.prg.QR_x[QR_depth_index]
    QR_0 = to_ints(QR_0)
    
    # Make key guesses.
    key_guesses = []
    for i in range(amount_of_test_values):
        key_guesses.append(get_random_binary(len(key)))
    key_guesses.sort()

    # Get QR from each key guess, and compare with original QR.
    key_comparisons = []
    for i in range(len(key_guesses)):
        sal = Salsa20(mode='test', static_nonce=stat_nonce)
        ciphertext = sal.encrypt(message, key_guesses[i])
        QR_i = sal.prg.QR_x[QR_depth_index]
        QR_i = to_ints(QR_i)
        similarity = Pearson_correlation(QR_0, QR_i)
        key_comparisons.append(similarity)
    
    # Plot
    bar_chart(key_comparisons)


def next_element_comparison():
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

    #print_list_of_lists(QR_x)
    QR_x_int = to_ints(QR_x)
    pearson_results = Pearson_on_list_of_lists(QR_x_int)
    for i in range(len(pearson_results)):
        print(i, '-', i+1, '\t', pearson_results[i])


    # Plot
    bar_chart(pearson_results)



compare_multiple_keys()
#next_element_comparison()
