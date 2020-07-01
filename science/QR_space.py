from salsa.QR_function import *
from tools.binary import Binary
from tools.hamming import HD, HW
from science.plot_tools import *


def generate_space(word_size:int):
    """Return a list of all word_size bit binary numbers."""
    space = []
    for i in range(2**word_size):
        a = Binary(i) % word_size
        a = a.split_string()
        space.append(a)
    return space


def get_Y_space(X_list:list):
    Y_list = QR_on_list(X_list)
    #print( len(X_list),  len(Y_list) )
    
    for i in range(len(X_list)):
        print(X_list[i], '\t-', Y_list[i])


def HDs_of_lists(Xs:list, Ys:list) -> list:
    HDs = []
    for i in range(len(Xs)):
        distance = HD(Xs[i], Ys[i])
        HDs.append(distance)
    return HDs


def HWs_of_list(Xs:list) -> list:
    HWs = []
    for X in Xs:
        weight = HW(X)
        HWs.append(weight)
    return HWs


def run(word_size:int = 12):
    Xs = generate_space(word_size)
    #Ys = get_Y_space(Xs)
    Ys = QR_on_list(Xs)

    HW_X = HWs_of_list(Xs)
    HW_Y = HWs_of_list(Ys)
    HDs = HDs_of_lists(Xs, Ys)
    HW_X.sort()
    HW_Y.sort()
    HDs.sort()

    multi_line_chart(
        lines=[HDs, HW_X, HW_Y],
        title='HDs and HWs of lists of QR input/output pairs (sorted)',
        x_label='bits',
        y_label='Hamming distance and weight'
    )
