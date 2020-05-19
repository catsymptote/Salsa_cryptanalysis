from science.cryptography_tools import *
from science.hamming_weight import *
from science.format_tools import *
from science.plot_tools import *
from science.math_tools import *
from science.Pearson_correlation import *


def show_n_flip_trajectory(bits, n_mods=None, keys=100, average=True):
    if n_mods is None:
        n_mods = bits

    crypt = Crypto_Tools()

    key = get_random_binary(bits)
    X_key = str_to_list(key)
    Y_key = crypt.use_QRF(X_key)
    Y_base = list_to_str(Y_key)

    HD_avgs = []


    # For n modifications/flips, where n == len(key).
    for n in range(n_mods):
        # For 100 keys.
        HDs = []
        for key_index in range(keys):
            key_n = flip_n_bits(key, n)

            X = str_to_list(key_n)
            Y = crypt.use_QRF(X)
            Y_str = list_to_str(Y)
            HD = hamming_distance(Y_str, Y_base)
            HDs.append(HD)
            # Flip n bits of key.
            # Run through QR.
            # Find Hamming distance: HD(key, key_mod)
            # Append to HD_avgs
        HD_avgs.append(HDs)
    

    if average:
        random_HDs = []
        for i in range(n_mods):
            X = generate_random_QR_X(int(bits/4))
            Y_str = list_to_str(crypt.use_QRF(X))
            HD = hamming_distance(Y_str, Y_base)
            random_HDs.append(HD)
        HD_avgs = average_lists(HD_avgs)
        random_HDs.sort()
        mini = min(random_HDs)
        mini_list = [mini] * len(random_HDs)
        maxi = max(random_HDs)
        maxi_list = [maxi] * len(random_HDs)
        multi_line_chart([HD_avgs, random_HDs, mini_list, maxi_list], x_label='bits flipped', y_label='HD')
    else:
        random_HDs = []
        for i in range(keys):
            X = generate_random_QR_X(int(bits/4))
            Y_str = list_to_str(crypt.use_QRF(X))
            HD = hamming_distance(Y_str, Y_base)
            random_HDs.append(HD)
        HD_avgs.append(random_HDs)
        multi_line_chart(lines=HD_avgs, x_label='bits flipped', y_label='HD')


if __name__ == '__main__':
    show_n_flip_trajectory(bits=512, n_mods=128, keys=1000)
