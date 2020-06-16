"""Abandoned class."""


from binary.binary import Binary


class Fixed_Binary(Binary):
    def __init__(self, val=None, size:int = 0):
        self.bits = '0'
        self.padding = padding

        self.set_val(val)
