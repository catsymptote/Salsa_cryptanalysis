from tools.hamming import HD, HW
from tools.binary import Binary
from salsa.QR_function import QR


def avg_XY_HD(runs:int, random_vals=False):
    word_size = 128
    avg = 0
    for i in range(runs):
        X = Binary()
        X.gen_random(word_size=word_size)
        X = X.split_string()
        Y = None
        if random_vals:
            Y = Binary()
            Y.gen_random(word_size=word_size)
        else:
            Y = QR(X)
        distance = HD(X, Y)
        avg += distance
    avg /= runs
    return avg


def avg_X_X_HD(runs:int, bits_flipped=1):
    word_size = 128
    avg = 0
    for i in range(runs):
        # Create X.
        X = Binary()
        X.gen_random(word_size=word_size)

        # Create X'.
        X_ = Binary(X.bits)
        for j in range(bits_flipped):
            X_.flip_random_bit()

        # Split into QR states.
        X = X.split_string()
        X_ = X_.split_string()

        # Run through QR function.
        Y = QR(X)
        Y_ = QR(X_)

        # Find distance.
        distance = HD(Y, Y_)
        avg += distance
        
    avg /= runs
    return avg



def run():
    print('QR (XY):\t', avg_XY_HD(1000, False))
    print('Random (XY):\t', avg_XY_HD(1000, True))
    print('QR (XX\'):\t', avg_X_X_HD(1000))
