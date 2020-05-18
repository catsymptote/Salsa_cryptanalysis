def xor(a:str, b:str) -> str:
    assert len(a) == len(b)

    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            c += '0'
        else:
            c += '1'
    
    return c


def hamming_weight(a:str) -> int:
    weight = 0
    for bit in a:
        if bit == '1':
            weight += 1
    
    return weight


def hamming_distance(a:str, b:str) -> int:
    assert len(a) == len(b)

    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    
    return distance


def hamming_distance_2(a:str, b:str) -> int:
    step_1_xor = xor(a, b)
    step_2_hw = hamming_weight(step_1_xor)
    return step_2_hw


"""
if __name__ == __main__:
    from science.format_tools import *
    from science.cryptography_tools import *

    number_of_keys = 100

    key = get_random_binary(256)
    data = 'Hello World!'
    correct_QR_x = QR_x(key, data)
    correct_QR_y = QR_x(key, data)

    random_keys = []
    for i in range(number_of_keys):
        random_key = get_random_binary(256)
        random_keys.append(random_key)

    key_distances = []
    for i in range(number_of_keys):
        distance = hamming_distance(key, random_keys[i])
        key_distances.append(distance)

    QRs = []
    for i in range(number_of_keys):
        QR_i = QR_x(key, data)
        QRs.append(QR_i)
    
    QR_distances = []
    for i in range(number_of_keys):
        distance = hamming_distance(QR_x, QRs[i])
        QR_distances.append(distance)
"""
