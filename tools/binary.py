# Inherit from str, so I won't have to redo that much.


class Binary:
    def __init__(self, val=None, padding:int = 0, fixed_size:int = None):
        self.bits = '0'
        self.padding = padding
        self.fixed_size = fixed_size

        self.set_val(val)
    

    def set_val(self, val):
        """Set the value."""
        if type(val) is int:
            self.bits = self.dec_to_bin(val)
        elif self.is_binary(val):
            self.bits = val
        else:
            self.bits = '0'


    def add_padding(self):
        while len(self.bits)%self.padding != 0:
            self.bits = '0' + self.bits

    
    def set_size(self):
        """Fixes (not permanently) length of self.bits."""
        if len(self.bits) > self.fixed_size:
            self.bits = self.bits[-self.fixed_size:]
        elif len(self.bits) < self.fixed_size:
            self.bits = self.add_padding()


    def dec_to_bin(self, val):
        """Convert a decimal number to binary."""
        return bin(val)[2:]


    def get_dec(self):
        """Return decimal representation of self.bits."""
        return int(self.bits, 2)
    

    def get_hex(self):
        """Return hexadecimal representation of self.bits."""
        return hex(self.bits, 2)


    def get_bin(self, word_size=0):
        """Return binary representation of self.bits.
        Adds buffer size so length % word_size == 0.
        word_size==0 changes nothing."""
        return self.bits


    def is_binary(self, val):
        if type(val) is not Binary and type(val) is not str:
            return False
        
        for char in val:
            if char != '0' and char != '1':
                return False
        
        return True


    def is_even(self, bits=None):
        """Check whether bits is even."""
        if bits is None:
            return self.bits[-1] == '0'
        
        if is_binary(bits):
            return bits[-1] == '0'
        
        return False


    def __getitem__(self, index):
        return self.bits[index]


    def __len__(self):
        return len(self.bits)


    def __xor__(self, a):
        assert len(self) == len(a)
        
        xor = ''
        for i in range(len(self)):
            if self[i] == a[i]:
                xor += '0'
            else:
                xor += '1'

        return xor
