from science.hamming_weight import hamming_distance, hamming_weight
from PIL import Image
import glob
import os


def pad_binary(binary, pad_size=8):
    if len(binary) > pad_size:
        binary = binary[-pad_size:]
    elif len(binary) < pad_size:
        binary = '0'*(pad_size - len(binary)) + binary
    return binary


def image_HD(img1, img2, return_bits=False):
    image_1 = list(Image.open(img1).getdata())
    image_2 = list(Image.open(img2).getdata())
    

    assert len(image_1) == len(image_2)
    assert len(image_1[0]) == len(image_2[0])
    assert type(image_1[0][0]) == type(image_2[0][0])

    distance = 0
    bits = 0
    for pix in range(len(image_1)):
        for col in range(len(image_1[0])):
            col_1 = image_1[pix][col]
            col_2 = image_2[pix][col]

            bin_1 = pad_binary(bin(col_1)[2:])
            bin_2 = pad_binary(bin(col_2)[2:])
            assert len(bin_1) == len(bin_2)

            for bit in range(len(bin_1)):
                bits += 1
                if bin_1[bit] != bin_2[bit]:
                    distance += 1
    #print(bits)
    if return_bits:
        return distance, bits
    else:
        return distance


def get_images(directory):
    paths = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            f_name, f_ext = os.path.splitext(name)
            if f_ext.lower() in ['.png', '.bmp', '.jpg', '.jpeg', '.tiff']:
                full_path = os.path.join(path, name)
                paths.append(full_path.replace('\\', '/'))
    
    return paths


if __name__ == '__main__':
    img1 = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/PTs/001/01_lg_PT.png'
    img2 = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001/01_lg_CT.png'
    #directory = 'D:/Projects/MasterThesis/Salsa_cryptanalysis/matlab/crypto_images/images/CTs/001'

    res = image_HD(img1, img2)
    print(res)
