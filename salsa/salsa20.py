from .prg import PRG
from .chacha_prg import Chacha_PRG
import random


class Salsa20:
    def __init__(self, mode:str='full', static_nonce=None, chacha=False):
        if chacha:
            if mode == 'test':
                self.prg = Chacha_PRG(test_mode=True)
            else:
                self.prg = Chacha_PRG()
        else:
            if mode == 'test':
                self.prg = PRG(test_mode=True)
            else:
                self.prg = PRG()
        
        self.mode = mode
        self.static_nonce = static_nonce


    def encrypt(self, data:str, key:str, nonce=None) -> tuple:
        data = self.to_binary(data)
        data = self.add_padding(data)
        data, nonce = self.crypt(data, key, nonce)
        data = self.to_text(data)
        return data, nonce


    def decrypt(self, data:str, key:str, nonce) -> str:
        data = self.to_binary(data)
        data, nonce = self.crypt(data, key, nonce)
        data = self.remove_padding(data)
        data = self.to_text(data)
        return data


    def crypt(self, data, key, nonce=None) -> tuple:
        # Split the data.
        blocks = []
        length = int(len(data)/512)
        for i in range(length):
            index_min = 512*i
            index_max = 512*(i+1)
            blocks.append(data[index_min:index_max])
        
        # Key and nonce
        key0, key1, full_key = self.split_key(key)

        if nonce is None:
            nonce = self.generate_nonce()
        else:
            #print(len(nonce), nonce)
            assert len(nonce) == 64

        ciphertext = ''

        # Encrypt, block by block.
        for block_number in range(len(blocks)):
            # Fix nonce and block number.
            nonce_block = self.make_nonce(nonce, block_number)
            assert len(nonce_block) == 128
            
            hash_bytes = self.prg.expansion_function(key0, key1, nonce_block, full_key)
            
            cipher_bytes = self.xor(blocks[block_number], hash_bytes)
            
            ciphertext += cipher_bytes
        
        return ciphertext, nonce


    def make_nonce(self, nonce, block_number) -> str:
        """Return the nonce
        (A combination of the nonce and the
        block number as a binary representation.)
        If using test mode: return a static nonce."""

        if self.mode == 'test':
            return self.static_nonce
        
        binary_block_number = self.generate_block_number(block_number)
        nonce_block = nonce + binary_block_number
        return nonce_block

    
    def xor(self, a, b) -> str:
        c = ''
        for i in range(len(a)):
            if a[i] == b[i]:
                c += '0'
            else:
                c += '1'
        return c


    def add_padding(self, data) -> str:
        """Add padding to make the data fit in packets of 64 bytes."""
        # Simple but probably not correct.
        package_count = 1
        while package_count*512 < len(data):
            package_count += 1
        
        while package_count*512 > len(data):
            data = data + '0'
        
        return data


    def remove_padding(self, data) -> str:
        """Removes 0s at the end of the string."""
        while data[-8:] == '00000000':
            data = data[0:-8]
        
        return data
    

    def to_binary(self, text:str) -> str:
        """Convert from text (ascii) to binary string."""
        chars = [char for char in text]
        binary = ''
        for char in chars:
            ascii_number = ord(char)
            tmp_binary = bin(ascii_number)[2:]
            while len(tmp_binary)%8 != 0:
                tmp_binary = '0' + tmp_binary
            binary += tmp_binary
        
        return binary


    def to_text(self, binary_data:str) -> str:
        """Convert from binary to text (ascii)."""
        # Split into bytes
        ascii_bytes = []
        length = int(len(binary_data)/8)
        for i in range(length):
            index_min = 8*i
            index_max = 8*(i+1)
            byte = binary_data[index_min:index_max]
            ascii_bytes.append(byte)
        
        ascii_numbers = []
        for byte in ascii_bytes:
            number = int(byte, 2)
            ascii_numbers.append(number)
        
        text = ''
        for number in ascii_numbers:
            character = chr(number)
            text += character

        return text


    def split_key(self, key) -> tuple:
        """Splits or copies the single key into two partial keys."""
        if len(key) == 128:
            return key, key, False
        else:
            return key[0:128], key[128:256], True


    def generate_block_number(self, number) -> str:
        """Converts number to an 8-byte binary number."""
        bin_number = bin(number)[2:]
        while len(bin_number) < 64:
            bin_number = '0' + bin_number
        return bin_number


    def generate_nonce(self) -> str:
        """Generates nonce. That is, a random 8-byte binary number."""
        nonce = ''
        for i in range(64):
            nonce += random.choice(['0', '1'])
        return nonce
