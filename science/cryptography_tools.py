from salsa.salsa20 import Salsa20
from salsa.prg import PRG


class Crypto_Tools:
    def __init__(self):
        self.stat_nonce = '0'*128
        self.sal = Salsa20(mode='test', static_nonce=self.stat_nonce)
        self.prg = PRG(test_mode=True)

        self.key = None
        self.data = None

        self.QR_x = None
        self.QR_y = None

        self.gen_QR_runs = 0
        self.get_QR_runs = 0


    def get_QR(self, key, data, index=0):
        if key != self.key or data != self.data:
            self.gen_QR(key, data)
        
        self.get_QR_runs += 1
        print(len(index))
        return self.word_list_to_bits(self.QR_x[index])


    def word_list_to_bits(self, word_list):
        bits = ''
        for word in word_list:
            bits += word
        
        return bits


    def gen_QR(self, key, data):
        self.sal = Salsa20(mode='test', static_nonce=self.stat_nonce)
        ciphertext = self.sal.encrypt(key=key, data=data)
        self.QR_x = self.sal.prg.QR_x
        self.QR_y = self.sal.prg.QR_y
        self.key = key
        self.data = data
        self.gen_QR_runs += 1

        # Dette tar litt tid (kanskje 20 sek).
        #print('Full XOR operations:', self.sal.prg.XORs)
        #print('Single bit XOR operations:', self.sal.prg.single_xor)


    """
    def QR_x(self, key, data, index=0):
        ciphertext = sal.encrypt(data, key)
        QR = sal.prg.QR_x[index]

        global_key = key
        global_data = data
        global_QR_x = word_list_to_bits(QR)
        
        return word_list_to_bits(QR)


    def QR_y(self, key, data, index=0):
        ciphertext = sal.encrypt(data, key)
        QR = sal.prg.QR_y[index]

        global_key = key
        global_data = data
        global_QR_y = word_list_to_bits(QR)

        return word_list_to_bits(QR)
    """


    def use_QRF(self, X:tuple):
        """Runs X through the QRf (Quarter Round function) once.
        Requirements for X
        - type(X) is tuple
        - len(X) is 4
        - type(X[i]) is str
        - len(X[i])%8 == 0.
        """
        return self.prg.quarterround_function(X)


if __name__ == '__main__':
    pass
