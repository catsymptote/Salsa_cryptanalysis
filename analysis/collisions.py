from science.QR_space import generate_incr_space, get_Y_space
from salsa.QR_function import *
from tools.hamming import HD
import matplotlib.pyplot as plt
from tools.binary import Binary
from science.plot_tools import multi_line_chart


def get_XY_space(word_size=12):
    """Generate a list of X's and their
    respective Y's. Generate all word_size bit
    numbers."""
    Xs = generate_incr_space(word_size)
    Ys = QR_on_list(Xs)
    return Xs, Ys


def scatter_plot(x:list, y:list):
    """Plot two lists of numbers."""
    plt.scatter(x, y, s=0.2)
    plt.show()


def average_incremental_HD(lst:list):
    """Average out the HD between
    two following items in the list."""
    avg = 0
    for i in range(len(lst) - 1):
        distance = HD(lst[i], lst[i+1])
        avg += distance
    avg = avg/(len(lst) - 1)
    return avg


def get_freq_dist(lst:list, word_size:int):
    freqs = [0] * 2**word_size
    ints = []

    for i in range(len(lst)):
        X_bin = Binary().combine_string(lst[i])
        X_int = X_bin.get_dec()
        freqs[X_int] += 1
        ints.append(X_int)
    
    return freqs, ints
        

def get_ints(X:list):
    """Convert list of ints from
    list of bytes."""
    X_ints = []
    for value in X:
        X_bin = Binary().combine_string(value)
        X_ints.append(X_bin.get_dec())
    return X_ints


def run(word_size=16):
    Xs, Ys = get_XY_space(word_size)
    #print(average_incremental_HD(Xs))
    #print(average_incremental_HD(Ys))

    #freqs_X, ints_X = get_freq_dist(Xs, word_size)
    #freqs_Y, ints_Y = get_freq_dist(Ys, word_size)

    #freqs_X.sort()
    #freqs_Y.sort()


    ints_X = get_ints(Xs)
    ints_Y = get_ints(Ys)
    set_X = set(ints_X)
    set_Y = set(ints_Y)
    
    print('If no AssertionError is throws, the QR is collision resistant. (At', word_size, 'bits.)')
    assert len(set_X) == len(ints_X)
    assert len(set_Y) == len(ints_Y)
