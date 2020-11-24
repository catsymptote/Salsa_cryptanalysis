from salsa.salsa20 import Salsa20
import random
import os

read_dir  = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/images/PT_txt'
write_dir = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/images/CT_txt'
files = []

for filename in os.listdir(read_dir):
    if filename.endswith('.txt'):
        files.append(filename)


# Set up crypto
def get_random_bin(length):
    string = ''
    for i in range(length):
        string += random.choice(['0', '1'])
    return string

key = get_random_bin(128)
nonce = get_random_bin(64)
sa = Salsa20()


for file_name in files:
    print(file_name)
    read_path  = os.path.join( read_dir, file_name)
    write_path = os.path.join(write_dir, file_name)
    # Read file
    f = open(read_path, 'r', encoding='utf8')
    PT = f.read()

    # Encrypt
    CT, nonce = sa.encrypt(PT, key, nonce)

    # Store file
    f = open(write_path, 'w', encoding='utf8')
    f.write(CT)
    f.close()
