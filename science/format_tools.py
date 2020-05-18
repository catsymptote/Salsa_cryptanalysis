import random


def add_padding(text, padding_increment, padding_symbol='0'):
    """Add padding such that the text is always
    of length n*padding_increment."""
    while len(text) % padding_increment != 0:
        text = padding_symbol + text
    
    return text


def split_string(text, space):
    """Inserts a space every [space] character.
    Fixed length with padding if needed."""

    text = add_padding(text, space)

    string_elements = []
    for i in range(0, len(text), space):
        string_elements.append(text[i:i+space])
    
    split_text = ''
    for element in string_elements:
        split_text += element + ' '
    
    return split_text[:-1]


################
## Convertion ##
################

def to_hex(num):
    """Convert bin (str) and int into hex (str)."""
    # Fix int/bin.
    if type(num) is str:
        num = int(num, 2)
    
    hex_ = hex(num)[2:]
    return hex_


def to_bytes(num):
    """Convert to hex, then split into full bytes."""
    hex_ = to_hex(num)
    #hex_ = add_padding(hex_, 8)
    hex_as_bytes = split_string(hex_, 8)
    return hex_as_bytes


def to_ints(X:list):
    """Converts:
    list(list(binary:str)) --> list(list(int))
    It does this recursively, so it will work for list(binary:str) as well.
    """

    if len(X) == 0:
        assert False
        return None
    
    if type(X) is tuple:
        X = list(X)
    
    for i in range(len(X)):
        in_X = X[i]

        if type(X[i]) is list or type(X[i]) is tuple:
            X[i] = to_ints(X[i])
        elif is_binary(X[i]):
            X[i] = int(X[i], 2)
        elif is_hex(X[i]):
            X[i] = int(X[i], 16)
        else:
            print(X[i])
            assert False
            return None

    return X


def flatten_list(X:list, flattened_list=None):
    """Takes 2 layers of depth."""
    flat_list = []
    for sublist in X:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def list_to_str(X:list):
    """Converts a list of strings into a single string.
    Mainly made for string(bin) --> bin."""
    binary = ''
    for elem in X:
        binary += elem
    return binary


def str_to_list(X:str):
    assert len(X)%4 == 0
    size = int(len(X)/4)
    
    x0 = X[0:size]
    x1 = X[size:2*size]
    x2 = X[2*size:3*size]
    x3 = X[3*size:]
    assert len(x0) == len(x1) == len(x2) == len(x3)
    Y = (x0, x1, x2, x3)
    return Y


#################
## Type checks ##
#################

def is_binary(num):
    """Checks if the number is in binary form.
    (Not including '0b' in front.)"""
    if type(num) is not str:
        return False
    
    for char in num:
        if char != '0' and char != '1':
            return False
    
    return True


def is_hex(num):
    if type(num) is not str:
        return False
    
    if is_binary(num):
        return False

    hex_chars = '0123456789abcdef'
    for char in num:
        if char not in hex_chars:
            return False
    
    return True


############
## Prints ##
############

def print_list_of_lists(X, print_index:bool = True):
    for i in range(len(X)):
        if print_index:
            print(i, end=':\t')
        for word in X[i]:
            print(to_bytes(word), end=' ')
        print()


def tab_print(lst:list):
    """Print a list with tabs between elements."""
    for elem in lst:
        print(elem, end='\t')
    print()


def print_list_of_lists(lst:list):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end='\t')
        print()
    print()


################
## Generators ##
################

def flip(bit:str) -> str:
    assert len(bit) == 1

    if bit == '0':
        return '1'
    else:
        return '0'


def get_random_binary(amount_of_bits:int) -> str:
    binary_number = ''
    for i in range(amount_of_bits):
        binary_number += random.choice(['0', '1'])
    return binary_number


def flip_random_bit(bits, amount=1):
    """Flips a single bit in input bits.
    bits should be list, tuple, or str."""
    # If tuple or list: Use random index.
    if type(bits) is list or type(bits) is tuple:
        index = random.randint(0, len(bits) - 1)

        if type(bits) is tuple:
            bits = list(bits)
            bits[index] = flip_random_bit(bits[index])
            bits = tuple(bits)
        else:
            bits[index] = flip_random_bit(bits[index])

        return bits
    
    # Flip bit.
    index = random.randint(0, len(bits) - 1)
    new_bits = bits[0:index]
    if bits[index] == '0':
        new_bits += '1'
    else:
        new_bits += '0'
    new_bits += bits[index+1:]

    # Hax. Remove when not used.
    # Replaced original string with a random one.
    #new_bits = get_random_binary(len(new_bits))

    if amount > 1:
        return flip_random_bit(new_bits, amount=amount-1)
    return new_bits


def flip_bits(bits:str) -> str:
    flipped_bits = ''
    for bit in bits:
        if bit == '0':
            flipped_bits += '1'
        else:
            flipped_bits += '0'
    
    return flipped_bits


def flip_bit_at(bits:str, index:int) -> str:
    if type(bits) is list or type(bits) is tuple:
        element = 0
        while index >= len(bits[element]):
            element += 1
            index -= len(bits[element])
        
        is_tuple = False
        if type(bits) is tuple:
            is_tuple = True
        
        if is_tuple:
            bits = list(bits)
        
        bits[element] = flip_bit_at(bits[element], index)
        
        if is_tuple:
            bits = tuple(bits)
        
        return bits
    
    bit = bits[index]
    flipped_bit = None
    if bit == '0':
        flipped_bit = '1'
    else:
        flipped_bit = '0'
    
    new_bits = bits[:index] + flipped_bit + bits[index+1:]
    return new_bits


def flip_bits_in_word(bits:str, amount:int = None) -> str:
    #if stop is None:
    #    stop = len(bits) - 1
    if amount is None:
        amount = 0

    unchanged_bits = bits[:-amount]
    remaining_bits = bits[-amount:]

    flipped_bits = flip_bits(remaining_bits)
    modified_bits = unchanged_bits + flipped_bits

    return modified_bits


def generate_random_QR_X(bits:int):
    X = [None]*4
    for i in range(4):
        X[i] = get_random_binary(bits)
    return tuple(X)


def increment_bits(bits:str, step=1):
    int_num = int(bits, 2)
    int_num += step
    bin_num = bin(int_num)[2:]
    return bin_num


def increment_QR_X(X:tuple, step=1):
    size = len(X[0])
    X_str = list_to_str(X)
    X_str = increment_bits(X_str, step)
    X_str = add_padding(X_str, size*4)
    if len(X_str) > size*4:
        X_str = X_str[len(X_str) - size:]
    
    # Split str -> tuple.
    assert len(X_str) == size*4
    x0 = X_str[0:size]
    x1 = X_str[size:2*size]
    x2 = X_str[2*size:3*size]
    x3 = X_str[3*size:4*size]
    return (x0, x1, x2, x3)
