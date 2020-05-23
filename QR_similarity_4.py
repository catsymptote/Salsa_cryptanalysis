"""Plots the HD(Xi, Yi) for random X and Y."""

from science.cryptography_tools import *
from science.hamming_weight import *
from science.format_tools import *
from science.plot_tools import *
from science.math_tools import *
from science.Pearson_correlation import *


def QR(X):
    if type(X) is str:
        X = str_to_list(X)
    Y = Crypto_Tools().use_QRF(X)
    return list_to_str(Y)


bits = 128
flips = bits*1

X0 = get_random_binary(bits)
Y0 = QR(X0)

# Generate Xs.
X = [X0]
for i in range(flips - 1):
    Xi = flip_random_bit(X[i])
    X.append(Xi)

# Get Ys.
Y = []
for i in range(flips):
    Y.append(QR(X[i]))

#print(X)
#print(Y)

# Get HDs.
HDs = []
for i in range(flips):
    HD = hamming_distance(X[i], Y[i])
    HDs.append(HD)

# Get HD for Xs and Ys.
HD_Y = []
HD_X = []
for i in range(flips):
    HD_X.append(hamming_distance(X0, X[i]))
    HD_Y.append(hamming_distance(Y0, Y[i]))

expected = [bits/2] * len(HDs)

multi_line_chart([HDs, expected, HD_X, HD_Y], vertical_lines=[16, 32])#, bits])
