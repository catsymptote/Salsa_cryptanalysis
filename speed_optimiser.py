from science.format_tools import *
from science.cryptography_tools import *
from science.hamming_weight import *
import time


runs = 1000

crypt = Crypto_Tools()
data = 'cryptography'
keys = []
for i in range(runs):
    keys.append(get_random_binary(128))

#word_list = crypt.get_QR(keys[0], data)

###################
start = time.time()
###################


for i in range(runs):
    crypt.get_QR(keys[0], data)
    #crypt.get_QR(keys[i], data)
    #crypt.gen_QR(keys[i], data)
    #tmp = crypt.word_list_to_bits(word_list)
    #tmp = hamming_weight(keys[0])


################################
end = (time.time() - start)/runs
################################

print('\n', end, '\n')
