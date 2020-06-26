import time

from salsa.prg import PRG
from analysis.QR_functions import *

def run_n_QRs(QR, n:int = 10000):
    X_2 = ('00', '00', '00', '00')
    X_32 = ('10100000001010000010100100101001', '11111011111110111111101111111011', '00000110000001100000010000000110', '01101001001010010000100101101001')

    start = time.time()

    for i in range(n):
        Y = QR(X_2)
    
    middle = time.time()

    for i in range(n):
        Y = QR(X_32)
    
    finish = time.time()

    print('n:', n, '\tX_2:', (middle - start), '\tX_32:', (finish - middle))


def run_test():
    #prg = PRG()
    #run_n_QRs(prg.quarterround_function)
    run_n_QRs(simple_test_1)
    run_n_QRs(simple_test_2)

    prg = PRG()
    run_n_QRs(prg.quarterround_function)


#if __name__ == '__main__':
#    run_test()
