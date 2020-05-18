from science.cryptography_tools import *
from science.hamming_weight import *
from science.format_tools import *
from science.plot_tools import *
from science.math_tools import *


def show_similar_keys(
        num_of_keys:int = 10,
        show_key_distance:bool = True,
        show_QR_distance:bool = True,
        modify_keys:bool = True):
    # Setup
    data = 'cryptography'
    #key = '10'*64
    key = get_random_binary(128)

    rounds = 80

    # Create random keys.
    ks = []
    for i in range(num_of_keys):
        ks.append(get_random_binary(128))

    # Modify keys to make some of them
    # more similar to the original key.
    if modify_keys:
        ks[0] = key
        ks[1] = flip_bits_in_word(key, amount=1)
        ks[2] = flip_bits_in_word(key, amount=4)
        ks[3] = '0' + key[1:]
        #ks[4] = key[:-16] + '0'*16
        ks[5] = flip_bits_in_word(key, amount=16)
        ks[6] = flip_bits_in_word(key, amount=64)
        ks[7] = flip_bits_in_word(key)
    

    # Find key distances.
    key_dist = []
    for i in range(num_of_keys):
        key_dist.append(hamming_distance(key, ks[i]))

    # Create class with QR-salsa-interface.
    crypto = Crypto_Tools()

    key_QRs = []
    for round_number in range(rounds):
        key_QRs.append(crypto.get_QR(key, data, index=round_number))

    QR_dist = []

    for key_index in range(num_of_keys):
        QR_tmp = []
        for round_number in range(rounds):
            qr = crypto.get_QR(ks[key_index], data, index=round_number)
            dist = hamming_distance(key_QRs[round_number], qr)
            QR_tmp.append(dist)
        QR_dist.append(QR_tmp)
    #print(crypto.get_QR_runs, crypto.gen_QR_runs)

    for line in range(len(QR_dist)):
        QR_dist[line] = average_n(QR_dist[line])

    if show_key_distance:
        multi_line_chart([key_dist], title='Keys\' HD')
    if show_QR_distance:
        multi_line_chart(QR_dist, increment=4, title='Key-QRs\' HD per round, for different keys')
    
    return (ks, key_QRs, key_dist, QR_dist)


if __name__ == '__main__':
    return_values = show_similar_keys(num_of_keys=15, show_key_distance=False, show_QR_distance=True, modify_keys=True)
    ks = return_values[0]
    key_QRs = return_values[1]

    ks_HW = []
    QR_HW = []
    for i in range(len(ks)):
        ks_tmp = hamming_weight(ks[i])
        ks_HW.append(ks_tmp)

        QR_tmp = hamming_weight(key_QRs[i])
        QR_HW.append(QR_tmp)
    
    ks_HW.sort()
    QR_HW.sort()

    #multi_line_chart([ks_HW, QR_HW])
