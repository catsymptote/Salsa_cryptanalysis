from science.cryptography_tools import *
from salsa.salsa20 import Salsa20
from salsa.prg import PRG


def test_init():
    crypt = Crypto_Tools()
    assert type(crypt) is Crypto_Tools
    assert type(crypt.sal) is Salsa20
    assert type(crypt.prg) is PRG


def test_use_QRF():
    # Setup, X.
    x0 = '01101110'
    x1 = '10101001'
    x2 = '11000110'
    x3 = '10011010'
    X = (x0, x1, x2, x3)

    # Run test.
    crypt = Crypto_Tools()
    Y = crypt.use_QRF(X)

    # Test shit.
    assert type(Y) is tuple
    assert len(Y) == 4
    for i in range(4):
        y = Y[i]
        assert type(y) is str
        assert len(y) == 8
