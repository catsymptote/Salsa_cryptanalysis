from tools.binary import Binary


def nothing(X):
    return X


def random_bits(X):
    Y = list(X)
    for i in range(len(X)):
        tmp_bin = Binary()
        tmp_bin.gen_random(word_size=len(X[i]))
        Y[i] = tmp_bin
    return tuple(Y)


def reverse_tuple(X):
    X = X[::-1] # Does this work for tuples?
    return X


def reverse_bits(X):
    Y = [None] * len(X)
    for i in range(len(Y)):
        Y[i] = Binary(X[i].bits[::-1])
    return tuple(Y)


def reverse_full(X):
    X = reverse_bits(X)
    X = reverse_tuple(X)
    return X


def xor_0(X, bit='0'):
    X = list(X)
    for i in range(len(X)):
        new_word = ''
        for j in range(len(X[i])):
            if X[i][j] == bit:
                new_word += '0'
            else:
                new_word += '1'
        
        X[i] = Binary(new_word)
        
    return tuple(X)


def xor_1(X):
    return xor_0(X, bit='1')


##################
## ARX elements ##
##################

## A
def add_parts(X):
    a, b, c, d = X
    Y = (a%b, c%d, a%d, b%c)
    return Y


# R (1)
def rotate_parts(X, bits=1):
    Y = list(X)
    for i in range(len(X)):
        Y[i] = X[i] // bits
    return tuple(Y)

# R (2)
def rotate_all(X, bits=1):
    string = Binary().combine_string(X)
    bin_string = Binary(string)
    bin_string = bin_string // bits
    Y = bin_string.split_string()
    return Y

# X
def part_xor_1(X):
    a, b, c, d = X
    m = a ^ b
    n = c ^ d
    o = a ^ d
    p = b ^ c
    Y = (m, n, o, p)
    return Y


def get_algs():
    all_algs = (
        nothing, random_bits,
        reverse_tuple, reverse_bits, reverse_full,
        xor_0, xor_1,
        add_parts, rotate_parts, rotate_all, part_xor_1
    )
    return all_algs
