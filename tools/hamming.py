from tools.binary import Binary


def HW(word:Binary) -> int:
    if type(word) is Binary:
        word = word.bits
    
    weight = word.count('1')
    return weight


def HD(word_1:Binary, word_2:Binary) -> int:
    distance = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            distance += 1
    return distance


def HD_2(word_1:Binary, word_2:Binary) -> int:
    if type(word_1) is str:
        word_1 = Binary(word_1)
    if type(word_2) is str:
        word_2 = Binary(word_2)

    xor = word_1 ^ word_2
    distance = HW(xor)
    return distance
