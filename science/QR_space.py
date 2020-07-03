from salsa.QR_function import *
from tools.binary import Binary
from tools.hamming import HD, HW
from science.plot_tools import *
from analysis import bad_crypto


def generate_incr_space(word_size:int):
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


def sorted_space(word_size:int = 12):
    Xs = generate_incr_space(word_size)
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


def incremental_space(function=QR, word_size:int = 12):
    X = Binary()#'0000000000000000')
    X.gen_random(word_size)
    X = X.split_string()
    Y = function(X)

    Xs = generate_incr_space(word_size)
    #Ys = QR_on_list(Xs)
    Ys = []
    for X in Xs:
        Ys.append(function(X))
    

    Y_base = [Y] * len(Ys)
    HDs = HDs_of_lists(Y_base, Ys)

    multi_line_chart(
        lines=[HDs],
        title='HDs of incremental outputs',
        x_label='bits',
        y_label='Hamming distance and weight'
    )


def generate_random_flipped_space(X:Binary, runs=None):
    if runs is None:
        runs == 1000 #2**len(X)
    
    space = [X]
    a = Binary()
    for i in range(runs):
        X = a.combine_string(X)
        
        X.flip_random_bit()
        X = a.split_string(X)
        space.append(X)
    return space


def average_out_list(HD_lists):
    """HD_lists is a list of lists of ints."""
    amount_of_lists = len(HD_lists)
    length_of_each_list = len(HD_lists[0])

    HD_avgs = []
    for i in range(length_of_each_list):
        avg = 0
        for j in range(amount_of_lists):
            avg += HD_lists[j][i]
        avg = avg/len(HD_lists)
        HD_avgs.append(avg)
    return HD_avgs



def random_flips(function=QR, word_size:int=12):
    X = Binary()#'0000000000000000')
    X.gen_random(word_size)
    X = X.split_string()
    Y = function(X)

    HD_lists = []
    for i in range(100):
        Xs = generate_random_flipped_space(X, runs=100)
        #Ys = QR_on_list(Xs)
        Ys = []
        for X_i in Xs:
            Ys.append(function(X_i))
        

        Y_base = [Y] * len(Ys)
        HDs = HDs_of_lists(Y_base, Ys)
        HD_lists.append(HDs)
    
    return HD_lists



def run():
    word_size = 64
    #incremental_space(function=QR)
    functions = [QR] + list(bad_crypto.get_algs())
    
    # Get results and average out.
    results = []
    for func in functions:
        HD_lists = random_flips(function=func, word_size=word_size)
        HD_avgs = average_out_list(HD_lists)
        results.append(HD_avgs)
    
    # Create the linear graph.
    expected_avg = int(word_size/2)
    linear = list(range(0, expected_avg))
    remaining = len(HD_avgs) - len(linear)
    linear += [expected_avg] * remaining
    results.append(linear)
    
    # Print function/line names.
    for i in range(len(functions)):
        print(i, ':', functions[i].__name__)
    print(len(functions), ':', 'linear')

    multi_line_chart(results, x_label='flips', y_label='HD', dotted=False)
