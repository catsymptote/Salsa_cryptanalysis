from science.format_tools import *
from science.cryptography_tools import *
from science.hamming_weight import *
import time


runs = 10000
key_size = 8192

crypt = Crypto_Tools()
data = 'cryptography'
keys = []
for i in range(runs):
    keys.append(get_random_binary(key_size))

#word_list = crypt.get_QR(keys[0], data)
print("Construction done!")
###################
start_time = time.time()
###################


for i in range(runs):
    crypt.get_QR(keys[i], data)
    #crypt.get_QR(keys[i], data)
    #crypt.gen_QR(keys[i], data)
    #tmp = crypt.word_list_to_bits(word_list)
    #tmp = hamming_weight(keys[0])


################################
end_time = time.time() - start_time#/runs
################################

print('\n', key_size, end_time, '\n')
#print(end_time)
#print(start_time)
#print(time.time())
