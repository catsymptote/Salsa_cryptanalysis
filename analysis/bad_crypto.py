from tools.binary import Binary


def nothing(X):
    return X


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


def get_algs():
    all_algs = (
        nothing,
        reverse_tuple, reverse_bits, reverse_full,
        xor_0, xor_1
    )
    return all_algs
