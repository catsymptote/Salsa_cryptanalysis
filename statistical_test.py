from app.salsa20 import Salsa20
from app.format_tools import to_bytes


stat_nonce = '11011011'*16
message = 'Hello World!'
key = '10010010'*16

sal = Salsa20(mode='test', static_nonce=stat_nonce)
ciphertext = sal.encrypt(message, key)

QR_test_vals = sal.prg.QR_test_vals

for i in range(len(QR_test_vals)):
    words = QR_test_vals[i]
    print(i, end=': ')
    for j in range(len(words)):
        word = words[j]
        print(to_bytes(word), end=' ')
    print()
