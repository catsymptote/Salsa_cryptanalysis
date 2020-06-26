from tools.binary import Binary


def QR(X:tuple) -> tuple:
    """Salsa QR function."""
    x0, x1, x2, x3 = X

    word_size = len(x0)

    x0 = Binary(x0)
    x1 = Binary(x1)
    x2 = Binary(x2)
    x3 = Binary(x3)

    y1 = x1 ^ ((x0 % x3) // 7)
    y2 = x2 ^ ((y1 % x0) // 9)
    y3 = x3 ^ ((y2 % y1) // 13)
    y0 = x0 ^ ((y3 % y2) // 18)

    y0_ = y0.get_bin(word_size)
    y1_ = y1.get_bin(word_size)
    y2_ = y2.get_bin(word_size)
    y3_ = y3.get_bin(word_size)

    Y = (y0_, y1_, y2_, y3_)
    return Y



def QR_chacha(X:tuple) -> tuple:
    """ChaCha QR function."""
    a, b, c, d = X
    a = Binary(a)
    b = Binary(b)
    c = Binary(c)
    d = Binary(d)

    # 1
    a = a % b
    d = d ^ a
    d = d // 16

    # 2
    c = c % d
    b = b ^ c
    b = b // 12

    # 3
    a = a % b
    d = d ^ a
    d = d // 8

    # 4
    c = c % d
    b = b ^ c
    b = b // 7

    return (a.bits, b.bits, c.bits, d.bits)
