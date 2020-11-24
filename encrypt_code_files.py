from salsa.salsa20 import Salsa20
import random
import os

read_dir  = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/images/images/train'
write_dir = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/images/images/train'
files = []

all_file_paths = []
file_paths = []

for path, subdirs, files in os.walk(read_dir):
    for name in files:
        all_file_paths.append(os.path.join(path, name))


for path in all_file_paths:
    if path[-8:] == '_lg.code':
        if path[-10] == '0':
            if path[-9] in ['1', '2', '3', '4', '5']:
                file_paths.append(path)

print('Files found:\t', len(all_file_paths))
print('Files accepted:\t', len(file_paths))


#for filename in os.listdir(read_dir):
#    if filename.endswith('.txt'):
#        files.append(filename)


# Set up crypto
def get_random_bin(length):
    string = ''
    for i in range(length):
        string += random.choice(['0', '1'])
    return string

key = get_random_bin(128)
nonce = get_random_bin(64)
sa = Salsa20(ascii_ord_convertion=False)

counter = 0
for path in file_paths:
    counter += 1
    print(counter, '\t', path)
    
    # Read file
    f = open(path, 'rb')#, encoding='utf8')
    PT = f.read()
    
    # Encrypt
    CT, nonce = sa.encrypt(PT, key, nonce)
    
    # Store file
    write_path = path[:-5] + '_CT' + path[-5:]
    
    f = open(write_path, 'w', encoding='utf8')
    f.write(CT)
    f.close()
