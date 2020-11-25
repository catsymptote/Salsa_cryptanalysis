from QR_similarity_4_salsa import *



def test_to_bin():
    a = 'abc'
    #assert to_bin(a) == '011000010110001001100011'
    assert to_bin(a) == '110000111000101100011'


def test_padder():
    a = '0101'
    b = '11001011'
    c = '1001'*8

    assert len(a) == 4
    assert len(b) == 8
    assert len(c) == 32

    assert len(padder(a)) == 8
    assert len(padder(b)) == 8
    assert len(padder(c)) == 8
    
    assert len(padder(a, 64)) == 64
    assert len(padder(b, 64)) == 64
    assert len(padder(c, 64)) == 64


def test_average_list_2():
    lst = [ [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
            #4, 5, 6
    assert average_list_2(lst) == [4, 5, 6]
