from tools.binary import Binary


def HW(word:Binary) -> int:
    """Returns the hamming weight of input word."""
    if type(word) is Binary:
        word = word.bits
    
    weight = word.count('1')
    return weight


def HW_2(word:Binary) -> int:
    """Alternative (and slower) version of HW."""
    if type(word) is Binary:
        word = word.bits
    
    weight = 0
    for bit in word:
        if bit == '1':
            weight += 1
    return weight


def HD(word_1:Binary, word_2:Binary) -> int:
    """Returns the hamming distance between
    two input words."""
    distance = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            distance += 1
    return distance


def HD_2(word_1:Binary, word_2:Binary) -> int:
    """Alternative (and slower) version of HD."""
    if type(word_1) is str:
        word_1 = Binary(word_1)
    if type(word_2) is str:
        word_2 = Binary(word_2)

    xor = word_1 ^ word_2
    distance = HW(xor)
    return distance
