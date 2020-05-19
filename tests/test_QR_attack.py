from QR_attack_1 import *
from science.cryptography_tools import Crypto_Tools


def test_brute_force_QR():
    crypt = Crypto_Tools()
        
    X = (
        '00000000',
        '00000000',
        '00000000',
        '10001011'
    )
    Y = crypt.use_QRF(X)
    X_guess = brute_force_QR(Y)

    assert type(X_guess) is type(X) is tuple
    assert len(X_guess) == len(X) == 4
    
    for i in range(4):
        assert type(X_guess[i]) is type(X[i]) is str
        assert len(X_guess) == len(X) == 4
        assert X_guess[i] == X[i]
    
    assert X_guess == X
