"""Implementation based on this description of Salsa20.
http://www.crypto-it.net/eng/symmetric/salsa20.html?tab=0
"""
from tools.binary import Binary


class PRG():
    A_VECTOR = [
        [101, 120, 112, 97],
        [110, 100, 32, 51],
        [50, 45, 98, 121],
        [116, 101, 32, 107]
    ]

    B_VECTOR = [
        [101, 120, 112, 97],
        [110, 100, 32, 51],
        [50, 45, 98, 121],
        [116, 101, 32, 107]
    ]


    def __init__(self, test_mode:bool=False):
        self.test_mode = test_mode
        
        self.a_vects = []
        self.b_vects = []

        for i in range(4):
            a_n = ''
            b_n = ''
            for j in range(4):
                a_n += Binary(PRG.A_VECTOR[i][j]).get_bin(8)
                b_n += Binary(PRG.B_VECTOR[i][j]).get_bin(8)
                #A_bin_n = A_vec_n.get_bin(8)
                #B_bin_n = B_vec_n.get_bin(8)
                #a_n += A_vec_n
                #b_n += B_vec_n

                #a_n += self.to_binary(PRG.A_VECTOR[i][j])
                #b_n += self.to_binary(PRG.B_VECTOR[i][j])
            self.a_vects.append(a_n)
            self.b_vects.append(b_n)
        
        # Log
        self.single_xor     = 0
        self.XORs           = 0
        self.mod_adds       = 0
        self.shifts         = 0
        self.shift_length   = 0
        self.QRs            = 0
        self.total_runs     = 0
        self.QR_x           = []
        self.QR_y           = []
        self.DRF_in         = []


    ###################################
    ## Start of Binary functionality ##
    ###################################

    

    ## Replaced with Binary.
    def to_bytes(self, a, length=8) -> tuple:
        if type(a) is tuple:
            a = self.to_bits(a)
        
        # String
        assert len(a)%length==0
        assert type(a) is str

        byte_list = []
        for i in range(int(len(a)/length)):
            byte_list.append(a[i*length:(i+1)*length])
        return tuple(byte_list)


    ## Replaced with Binary.
    def to_words(self, a) -> tuple:
        return self.to_bytes(a, length=32)


    ## Replaced with Binary.
    def to_bits(self, a:tuple) -> str:
        bits = ''
        for element in a:
            if type(element) is tuple:
                element = self.to_bits(element)
            bits += element
        return bits
            

    #################################
    ## End of Binary functionality ##
    #################################



    def quarterround_function(self, x:tuple) -> tuple:
        """
        # y1 = x1 XOR ((x0+x3) <<< 7)
        # y2 = x2 XOR ((y1+x0) <<< 9)
        # y3 = x3 XOR ((y2+y1) <<< 13)
        # y0 = x0 XOR ((y3+y2) <<< 18)


        # y1 = x1 XOR ((x0+x3) <<< 7)
        y1 = self.sum_words(x0, x3)
        y1 = self.binary_left_rotation(y1, 7)
        y1 = self.xor(x1, y1)

        # y2 = x2 XOR ((y1+x0) <<< 9)
        y2 = self.sum_words(y1, x0)
        y2 = self.binary_left_rotation(y2, 9)
        y2 = self.xor(x2, y2)

        # y3 = x3 XOR ((y2+y1) <<< 13)
        y3 = self.sum_words(y2, y1)
        y3 = self.binary_left_rotation(y3, 13)
        y3 = self.xor(x3, y3)

        # y0 = x0 XOR ((y3+y2) <<< 18)
        y0 = self.sum_words(y3, y2)
        y0 = self.binary_left_rotation(y0, 18)
        y0 = self.xor(x0, y0)
        """
        x0, x1, x2, x3 = x

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

        y = (y0_, y1_, y2_, y3_)
        return y

        #y1 = self.quarter(x1, x0, x3, 7)
        #y2 = self.quarter(x2, y1, x0, 9)
        #y3 = self.quarter(x3, y2, y1, 13)
        #y0 = self.quarter(x0, y3, y2, 18)
        
        #y = (y0, y1, y2, y3)

        #if self.test_mode:
        #    self.QR_x.append(x)
        #    self.QR_y.append(y)
        #return y


    def rowround_function(self, x:tuple) -> tuple:
        y = []
        assert len(x) == 16
        for i in range(4):
            j = 4*i
            y_n = self.quarterround_function( (x[j], x[j+1], x[j+2], x[j+3]) )
            assert len(y_n) == 4
            for word in y_n:
                y.append(word)
        
        assert len(y) == 16
        return tuple(y)


    def columnround_function(self, x:tuple) -> tuple:
        y = []
        assert len(x) == 16
        for i in range(4):
            x_n = []
            for j in range(4):
                x_n.append(x[ (5*i + 4*j)%16])
            assert len(x_n) == 4

            y_n = self.quarterround_function(x_n)
            assert len(y_n) == 4
            for word in y_n:
                y.append(word)
        
        assert len(y) == 16
        return tuple(y)
    

    def doubleround_function(self, x:tuple) -> tuple:
        self.DRF_in.append(x)
        assert len(x) == 16
        return_value = self.rowround_function(self.columnround_function(x))
        assert len(return_value) == 16
        return return_value


    def littleendian_function(self, word:str) -> str:
        """Reverse the order of the bytes."""
        b_bytes = []
        assert len(word) == 32
        for i in range(4):
            b_bytes.append(word[i:i+8])
        assert len(b_bytes) == 4
        assert len(b_bytes[0]) == 8

        b_bytes = b_bytes[::-1]

        b_new = ''
        for byte in b_bytes:
            b_new += byte
        
        return b_new


    def hash_function(self, words:tuple) -> str:
        """The hash function does the following:
        1. Split the 64 byte input into 16 words.
        2. For all words: Update by littleendian function.
        3. Run all words through doubleround^10.
        4. Do the last magic. (See link.)"""
        
        # 1. Split words.
        #words = []
        #for i in range(16):
        #    word = ''
        #    for j in range(4):
        #        word += input_bytes[j + i*4]
        #    words.append(word)
        
        # 2. Run through littleendian function.
        for word in words:
            word = self.littleendian_function(word)
        
        """
        # 2.5 merge words --> x_list.
        x_list = ''
        for word in words:
            x_list += word
        """

        # 3. Run all words though doubleround x10.
        x_list = words + tuple()  # The cool way to do copy for tuples.

        for i in range(10):
            assert len(x_list) == 16
            x_list = self.doubleround_function(x_list)
            assert len(x_list) == 16

        # 4. The final magic
        output_list = []
        for i in range(16):
            input_1 = Binary(x_list[i])
            input_2 = Binary(words[i])
            output_element = input_1 % input_2
            output_element = output_element.bits

            #output_element = self.sum_words(x_list[i], words[i])
            output_element = self.littleendian_function(output_element)
            output_list.append(output_element)
        
        output = ''
        for output_element in output_list:
            output += output_element
        
        return output
    

    def expansion_function(self, key0:str, key1:str, nonce:str, full_key:bool) -> str:
        """Main (first/input) function of the salsa20 pseudo random generator (PRG).
        key0 and key1 are 16 bytes each.
            - If the key is a 32-bit key, key0 and key1 each contains their half.
            - If the key is a 16-bit key, key0 is a copy of key1.
        nonce is 16 bytes, and is the combination of:
            - 8 bytes of block number. (Which counts up for each 64-byte block of data.)
            - 8 bytes of cryptographic nonce. (That is, a one time 'random' number.)
        """
        
        assert len(key0) == len(key1) == 128
        #print(len(nonce))
        assert len(nonce) == 128
        
        # Split keys in needed, and ready hash function input.
        hash_input = None
        if full_key:
            a0, a1, a2, a3 = self.a_vects
            hash_input = a0 + key0, a1, nonce, a2, key1, a3
        else:
            b0, b1, b2, b3 = self.b_vects
            hash_input = b0 + key0 + b1 + nonce + b2 + key1 + b3
        
        # 64 bytes --> 16 words
        words = self.to_words(hash_input)

        # Return output from hash function.
        hash_output = self.hash_function(words)
        return hash_output
