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


def split_str(string:str, pieces:int) -> list:
    assert len(string)%pieces == 0
    if pieces == 1:
        return int(string)

    list_of_ints = []
    length = int(len(string)/pieces)
    
    for i in range(pieces):
        sub_str = string[i*length:(i+1)*length]
        
        #print(sub_str)
        number = int(sub_str, 2)
        list_of_ints.append(number)
    return list_of_ints


def split_binary(string:str, pieces:int) -> list:
    lst = list(string)
    for i in range(len(lst)):
        lst[i] = int(lst[i], 2)
    return lst


def analyse():
    bits = 128
    keys = int(bits/4)
    pieces = 1

    X = get_random_binary(bits)
    Y = QR(X)
    X_tmp = X

    # Hamming distance
    HDs = [hamming_distance(X, X_tmp)]
    QR_HDs = [hamming_distance(Y, Y)]

    # Pearson cc
    int_Xs = [X]
    int_Ys = [Y]

    for i in range(keys):
        X_tmp = flip_random_bit(X_tmp)
        Y_ = QR(X_tmp)

        # HD
        HD = hamming_distance(X, X_tmp)
        QR_HD = hamming_distance(Y, Y_)
        HDs.append(HD)
        QR_HDs.append(QR_HD)

        # Pear
        int_Xs.append(X_tmp)
        int_Ys.append(Y_)


    
    X_lists = []
    Y_lists = []
    for i in range(len(int_Xs)):
        X_lists.append(int(int_Xs[i]))     #split_str(int_Xs[i], pieces))
        Y_lists.append(int(int_Ys[i]))     #split_str(int_Ys[i], pieces))


    Pearson_cc = abs(Pearson_correlation_coefficient(X_lists, Y_lists))

    #print(keys)
    #print(len(HDs))
    #print(len(QR_HDs))
    #print(len(int_Xs), len(int_Ys))
    #print(len(X_lists), len(Y_lists))
    return HDs, QR_HDs, Pearson_cc


if __name__ == '__main__':
    avg_list = []
    for j in range(100):    # trys for avg
        PCC_list = []
        for i in range(32): # changes
            HDs, QR_HDs, Pearson_cc = analyse()
            PCC_list.append(Pearson_cc)
        avg_list.append(average(PCC_list))
    #PCC_list_T = list(map(list, zip(*PCC_list)))
    
    #avg = average(PCC_list)
    #for i in range(len(PCC_list_T)):
    #    avg.append(average(PCC_list_T[i]))
    
    multi_line_chart([PCC_list], y_label="Pearson correlation coefficient", x_label="bits flipped")
    #multi_line_chart([HDs, QR_HDs])
    #multi_line_chart([Pearson_cc])

    #analyse()
