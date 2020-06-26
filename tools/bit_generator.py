import random
from tools.binary import Binary


def gen_random_bits(word_size):
    """Return a random set of bits,
    of length word_size, as a Binary object."""
    bits = ''
    for i in range(word_size):
        bits += random.choice(('0', '1'))
    
    return Binary(bits)


def gen_random_words(words, word_size, as_tuple:bool = True):
    """Get a random list or tuple of words.
    (A word, being a Binary number.)"""
    word_list = []
    for i in range(words):
        word = gen_random_bits(word_size)
        word_list.append(word)
    if as_tuple is True:
        return tuple(word_list)
    else:
        return word_list


def whipe_bits(word, default='0'):
    """Make all bits in the word(s) 0.
    Can also make them all 1."""
    if type(word) is list:
        for i in range(len(word)):
            word[i] = whipe_bits(word[i])
    elif type(word) is tuple:
        word = list(word)
        word = whipe_bits(word)
        word = tuple(word)
    elif type(word) is str:
        word = default * len(word)
    else:
        # type(bits) is Binary
        word.bits = default * len(word.bits)
    
    return word
