from salsa.salsa20 import Salsa20


sa = Salsa20()
key = '10011100' * 16
nonce = '10011010' * 8

PT_1 = '10101100'*7 + '10101100'
PT_2 = '10101100'*7 + '10001100'
print(sa.encrypt(PT_1, key, nonce))
print(sa.encrypt(PT_2, key, nonce))
