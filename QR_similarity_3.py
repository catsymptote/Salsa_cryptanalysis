from science.cryptography_tools import *
from science.hamming_weight import *
from science.format_tools import *
from science.plot_tools import *
from science.math_tools import *
from science.Pearson_correlation import *


def find_cross_point(Line, Value):
    for i in range(len(Line)):
        if Line[i] >= Value:
            return i
    return None


def show_n_flip_trajectory(bits, n_mods=None, keys=100, is_average=True, QRFs=1):
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
            for i in range(QRFs - 1):
                Y = crypt.use_QRF(Y)
            
            Y_str = list_to_str(Y)
            HD = hamming_distance(Y_str, Y_base)
            HDs.append(HD)
            # Flip n bits of key.
            # Run through QR.
            # Find Hamming distance: HD(key, key_mod)
            # Append to HD_avgs
        HD_avgs.append(HDs)
    

    if is_average:
        random_HDs = []
        for i in range(n_mods):
            X = generate_random_QR_X(int(bits/4))
            Y_str = list_to_str(crypt.use_QRF(X))
            HD = hamming_distance(Y_str, Y_base)
            random_HDs.append(HD)
        random_avg = [average(random_HDs)] * len(random_HDs)
        
        HD_avgs = average_lists(HD_avgs)
        #random_HDs.sort()
        mini = min(random_HDs)
        mini_list = [mini] * len(random_HDs)
        maxi = max(random_HDs)
        maxi_list = [maxi] * len(random_HDs)
        crossing_point = find_cross_point(HD_avgs, mini)
        print(crossing_point)
        multi_line_chart([HD_avgs, random_HDs, mini_list, maxi_list, random_avg], vertical_lines=[crossing_point], x_label='bits flipped', y_label='HD')
    else:
        random_HDs = []
        for i in range(keys):
            X = generate_random_QR_X(int(bits/4))
            Y_str = list_to_str(crypt.use_QRF(X))
            HD = hamming_distance(Y_str, Y_base)
            random_HDs.append(HD)
        HD_avgs.append(random_HDs)
        multi_line_chart(lines=HD_avgs, x_label='bits flipped', y_label='HD', dotted=True)


if __name__ == '__main__':
    show_n_flip_trajectory(bits=128, n_mods=32, keys=1000, QRFs=1)
