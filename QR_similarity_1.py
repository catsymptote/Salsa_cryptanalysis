from science.cryptography_tools import *
from science.format_tools import *
from science.hamming_weight import *
from science.plot_tools import *
from salsa.prg import PRG


def print_list(lst, end_symbol=' '):
    for elem in lst:
        print(elem, end=end_symbol)
    print()


def calc_HDs_of_random_QRs(runs:int = 10, bits:int = 8):
    crypt = Crypto_Tools()
    
    HDs = []
    for i in range(runs):
        # Get random X and run through QRF.
        X = generate_random_QR_X(bits)
        Y = crypt.use_QRF(X)

        # Convert X and Y
        X_str = list_to_str(X)
        Y_str = list_to_str(Y)

        # Get hamming distance between X and Y.
        HD = hamming_distance(X_str, Y_str)
        HDs.append(HD)

    return HDs


def show_HDs():
    Y_ = calc_HDs_of_random_QRs(runs=1000, bits = 512)
    xs = range(len(Y_))
    Y_.sort()

    import matplotlib.pyplot as plt
    plt.title('Hamming Distance (HD) netween X and QRF(x).')
    plt.xlabel('Input value number')
    plt.ylabel('HD')
    plt.bar(xs, Y_)
    plt.show()


def HD_of_similar_values(changes:int, bits:int):
    crypt = Crypto_Tools()

    X = (
        get_random_binary(bits),
        get_random_binary(bits),
        get_random_binary(bits),
        get_random_binary(bits)
    )
    Y0 = list_to_str(crypt.use_QRF(X))
    HDs = []

    for i in range(changes):
        # QR(X_i)
        X = flip_random_bit(X)
        Y = crypt.use_QRF(X)
        Y_str = list_to_str(Y)

        # HD(Y0, Y)
        HD = hamming_distance(Y0, Y_str)
        HDs.append(HD)
    
    return HDs


def plot_QR_X_changes(changes:int, bits:int):
    HDs = HD_of_similar_values(changes, bits)
    X_axis = range(changes)
    
    import matplotlib.pyplot as plt
    plt.title('Hamming Distance (HD) between QRF(X) and QRF(X_), where X is close to X_.')
    plt.xlabel('Changes')
    plt.ylabel('HD')
    plt.bar(X_axis, HDs)
    plt.show()


def plot_QR_X_with_minmax_lines(changes:int, bits:int, min_changes:int=100):
    HDs = HD_of_similar_values(changes=changes, bits=bits)

    mini, maxi = find_change_range(HDs=HDs, min_changes=min_changes)
    print(mini, maxi)

    y_min = [mini]*len(HDs)
    y_max = [maxi]*len(HDs)
    
    lines = [HDs, y_min, y_max]
    multi_line_chart(
        lines=lines,
        title='Hamming Distance (HD) between QRF(X) and QRF(X_), where X is close to X_.',
        vertical_lines=[min_changes]
    )
    return lines


def find_change_range(HDs:list=None, changes:int=None, bits:int=None, min_changes:int=100):
    if HDs is None:
        HDs = HD_of_similar_values(changes, bits)
    
    HDs = HDs[min_changes:]
    return min(HDs), max(HDs)


def flip_one_by_one(bits:int = 128, QRF_runs:int = 1):
    crypt = Crypto_Tools()
    X = generate_random_QR_X(bits)

    Y0 = X
    for i in range(QRF_runs):
        Y0 = crypt.use_QRF(X)
    #Y0 = crypt.use_QRF(crypt.use_QRF(X))

    Y0 = list_to_str(Y0)

    HDs = []
    for i in range(len(Y0)):
        X = flip_bit_at(X, i)

        Y = X
        for i in range(QRF_runs):
            Y = crypt.use_QRF(X)
        
        Y = list_to_str(Y)
        HD = hamming_distance(Y0, Y)
        HDs.append(HD)
    
    multi_line_chart([HDs], vertical_lines=[bits, 2*bits, 3*bits])


if __name__ == '__main__':
    #plot_QR_X_changes(changes=1000, bits=128)
    #plot_QR_X_with_minmax_lines(changes=100, bits=128, min_changes=10)

    #           10k runs    100k runs   random values
    # 128 bits: [219, 302]  [208, 305]  [217, 296]
    # 256 bits: [458, 565]  [449, 557]  [457, 574]

    flip_one_by_one(bits=128, QRF_runs=1)
