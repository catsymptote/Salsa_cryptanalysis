# Inherit from str, so I won't have to redo that much.
import random


class Binary(str):
    def __init__(self, val=None): #, padding:int = 0, fixed_size:int = None):
        self.bits = None
        self.set_val(val)
        #self.padding = padding
        #self.fixed_size = fixed_size

        #self.set_val(val)
    
    
    
    def set_val(self, val):
        """Set the value."""
        if type(val) is int:
            self.set_bin(val)
        elif self.is_binary(val):
            # Is this test actually necessary?
            # When will this ever happen?
            self.bits = val
        else:
            self.bits = '0'


    def gen_random(self, word_size:int):
        bits = ''
        for i in range(word_size):
            bits += random.choice(['0', '1'])
        self.bits = bits


    def add_padding(self, padding):
        """Adds padding to self."""
        while len(self.bits)%padding != 0:
            self.bits = '0' + self.bits

        # Faster version. Not working properly.
        #if len(self.bits)%padding != 0:
        #    self.bits = '0'*(len(self.bits) - padding) + self.bits

    
    def set_size(self, word_size):
        """Fixes (not permanently) length of self.bits."""
        #if len(self.bits) > self.fixed_size:
        #    self.bits = self.bits[-self.fixed_size:]
        #elif len(self.bits) < self.fixed_size:
        #    self.bits = self.add_padding()
        if len(self.bits) < word_size:
            self.add_padding(word_size)
        elif len(self.bits) > word_size:
            self.bits = self.bits[-word_size:]


    def set_bin(self, val):
        """Convert a decimal number to binary."""
        self.bits = bin(val)[2:]


    def get_dec(self):
        """Return decimal representation of self.bits."""
        return int(self.bits, 2)
    

    def get_hex(self):
        """Return hexadecimal representation of self.bits."""
        return hex(self.get_dec())[2:]


    def get_bin(self, word_size=0):
        """Return binary str (not 'Binary'!)
        representation of self.bits.
        Adds buffer size so length % word_size == 0.
        word_size==0 changes nothing."""
        if word_size == 0:
            return self.bits
        else:
            tmp = Binary(self.bits)
            tmp.set_size(word_size)
            return tmp.bits


    def is_binary(self, val:str) -> bool:
        """Check if value is a binary number."""
        if type(val) is Binary:
            val = val.bits
        elif type(val) is str:
            pass
        else:
            return False
        
        for char in val:
            if char != '0' and char != '1':
                return False
        
        return True


    def is_even(self, bits=None):
        """Check whether bits is even.
        Probably not needed."""
        if bits is None:
            return self.bits[-1] == '0'
        
        if is_binary(bits):
            return bits[-1] == '0'
        
        return False


    def LSO(self, shift):
        for i in range(shift):
            self.bits = self.bits[1:] + self.bits[:1]


    def __getitem__(self, index):
        """Return bit number 'index'."""
        return self.bits[index]


    def __len__(self):
        """Returns the length (amount of bits) of self."""
        return len(self.bits)


    def __xor__(self, other):
        """Returns the XOR between self and other."""
        assert len(self) == len(other)
        
        xor = ''
        for i in range(len(self)):
            if self[i] == other[i]:
                xor += '0'
            else:
                xor += '1'

        return Binary(xor)

    
    def __eq__(self, other):
        if type(other) is Binary:
            return self.bits == other.bits
        elif type(other) is str:
            return self.bits == other
        return False
    

    def __ne__(self, other):
        return not self == other


    def __add__(self, other):
        if type(other) is str:
            other = Binary(other)
        
        a = self.get_dec()
        b = other.get_dec()
        c = Binary(a + b)
        print(c)
        return c
    

    def __mod__(self, other):
        """% If int:  Set size.
        If Binary:  Modular addition."""
        if type(other) is int:
            new = Binary(self.bits)
            new.set_size(other)
            return new

        
        length = len(self)
        if len(other) > length:
            length = len(other)

        c = self + other
        c.set_size(length)
        return c

    
    def __floordiv__(self, shift_int):
        """//, floordiv, rotate, LSO."""
        new = Binary(self.bits)
        new.LSO(shift_int)
        return new


    def hamming_weight(self):
        """Returns the Hamming weight of self."""
        HW = 0
        for bit in self.bits:
            if bit != '0':
                HW += 1
        
        return HW


    def __str__(self):
        return self.bits

    
    def hamming_distance(self, other):
        """Returns the Hamming distance between
        self and other (input parameter)."""
        assert len(self) == len(other)

        HD = 0
        for i in range(len(self)):
            if self[i] != other[i]:
                HD += 1

        return HD


    def hamming_distance_hw_xor(self, other):
        """Returns the Hamming distance between
        self and other (input parameter)."""
        assert len(self) == len(other)

        xor = self ^ other
        HD = xor.hamming_weight()

        return HD


    def split_string(self, X = None, pieces:int = 4):
        if X is None:
            X = self.bits
        elif type(X) is Binary:
            X = X.bits
        
        assert len(X) % pieces == 0
        piece_length = int(len(X) / pieces)

        Y = []
        for i in range(pieces):
            start = i * piece_length
            stop = start + piece_length
            piece = Binary(X[start:stop])
            Y.append(piece)
        
        return tuple(Y)

    def combine_string(self, X):
        assert type(X) is tuple or type(X) is list

        Y = ''
        for elem in X:
            if type(elem) is Binary:
                elem = elem.bits
            
            Y += elem
        
        return Binary(Y)
