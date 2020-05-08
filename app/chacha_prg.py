from .prg import PRG


class Chacha_PRG(PRG):
    def quarterround_function(self, x:tuple) -> tuple:
        """Modified QR."""
        a, b, c, d = x

        # 1
        a = self.sum_words(a, b)
        d = self.xor(d, a)
        d = self.binary_left_rotation(d, 16)

        # 2
        c = self.sum_words(c, d)
        b = self.xor(b, c)
        b = self.binary_left_rotation(b, 12)

        # 3
        a = self.sum_words(a, b)
        d = self.xor(d, a)
        d = self.binary_left_rotation(d, 8)

        # 4
        c = self.sum_words(c, d)
        b = self.xor(b, c)
        b = self.binary_left_rotation(d, 7)

        return (a, b, c, d)
