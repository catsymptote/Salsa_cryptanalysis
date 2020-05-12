from salsa.chacha_prg import Chacha_PRG
from salsa.prg import PRG
from salsa.salsa20 import Salsa20

# Import test tools
from tests.test_prg import make_words
from tests.test_salsa20 import full_crypto


#########
## PRG ##
#########

def test_chacha_prg_init():
    cha = Chacha_PRG()
    assert isinstance(cha, Chacha_PRG)
    assert isinstance(cha, PRG)


def test_chacha_QR():
    cha = Chacha_PRG()

    x = make_words(n=4)
    output = cha.quarterround_function(x)
    # Values not tested.
    assert type(output) is tuple
    #assert output == ('10100000001010000010100100101001', '11111011111110111111101111111011', '00000110000001100000010000000110', '01101001001010010000100101101001')
    assert len(output) == 4
    for word in output:
        assert type(word) is str
        assert len(word) == 32



############
## Crypto ##
############

def test_chacha_salsa_init():
    cha = Salsa20(chacha=True)
    assert type(cha.prg) is Chacha_PRG


def test_full_crypto():
    """Test that:
    a --> encrypt --> decrypt --> a."""
    # Small data set, full-key
    a1, a2 = full_crypto(1, 256)
    assert a1 == a2

    # Small data set, half-key
    b1, b2 = full_crypto(1, 128)
    assert b1 == b2

    # Large data set, full-key
    c1, c2 = full_crypto(1024, 256)
    assert c1 == c2

    # Irregular sized plaintext 1
    d1, d2 = full_crypto(666, 128)
    assert d1 == d2

    # Irregular sized plaintext 2
    e1, e2 = full_crypto(129, 256)
    assert e1 == e2
