from science.cryptography_tools import *
from science.format_tools import *
from science.hamming_weight import *
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
