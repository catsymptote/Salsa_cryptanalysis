from science.format_tools import *
from science.cryptography_tools import *
from science.hamming_weight import *
from tests.salsa.test_salsa20 import full_crypto
import time

def speed_test_QR():
    """Currently not functional."""
    runs = 1000
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
        print(type(crypt.QR_x))
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


def salsa_setup(amount, p_size, key_size):
    """Return a set amount of custom plaintexts
    and keys for testing purposes."""
    plaintexts = []
    for text in range(amount):
        plaintext = ''
        for char in range(p_size):
            plaintext += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        plaintexts.append(plaintext)

    keys = []
    for text in range(amount):
        key = ''
        for char in range(key_size):
            key += random.choice('01')
        keys.append(key)

    return plaintexts, keys


def speed_test_Salsa():
    """Estimate how long a single encryption takes with Salsa,
    as well as how long it would take to run it 1000000 times.
    Currently, it runs about 7-8 per second.
    """
    runs = 100
    sal = Salsa20()
    plaintexts, keys = salsa_setup(runs, 500, 128)
    ciphertexts = []
    start = time.time()
    for i in range(runs):
        ciphertext, nonce = sal.encrypt(plaintexts[i], keys[i])
        ciphertexts.append(ciphertext)
        decrypted_plaintext = sal.decrypt(ciphertext, keys[i], nonce)
    stop = time.time()
    time_per = (stop - start)/runs
    print(time_per, "per full encryption.")
    print("1000000 runs would take about", time_per*1000000, "seconds, or", time_per*1000000/86400, "days.")


if __name__ == '__main__':
    speed_test_Salsa()
