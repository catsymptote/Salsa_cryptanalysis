from .prg import PRG
from tools.binary import Binary


class Chacha_PRG(PRG):
    def quarterround_function(self, x:tuple) -> tuple:
        """Modified QR."""
        a, b, c, d = x
        a = Binary(a)
        b = Binary(b)
        c = Binary(c)
        d = Binary(d)

        # 1
        a = a % b
        d = d ^ a
        d = d // 16
        #a = self.sum_words(a, b)
        #d = self.xor(d, a)
        #d = self.binary_left_rotation(d, 16)

        # 2
        c = c % d
        b = b ^ c
        b = b // 12
        #c = self.sum_words(c, d)
        #b = self.xor(b, c)
        #b = self.binary_left_rotation(b, 12)

        # 3
        a = a % b
        d = d ^ a
        d = d // 8
        #a = self.sum_words(a, b)
        #d = self.xor(d, a)
        #d = self.binary_left_rotation(d, 8)

        # 4
        c = c % d
        b = b ^ c
        b = d // 7
        ### THIS SHOULD BE b ON BOTH SIDES! (I think...)
        #c = self.sum_words(c, d)
        #b = self.xor(b, c)
        #b = self.binary_left_rotation(d, 7)

        return (a.bits, b.bits, c.bits, d.bits)
