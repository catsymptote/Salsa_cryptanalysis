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


################
## Generators ##
################

def get_random_binary(amount_of_bits:int) -> str:
    binary_number = ''
    for i in range(amount_of_bits):
        binary_number += random.choice(['0', '1'])
    return binary_number


def flip_bits(bits:str) -> str:
    flipped_bits = ''
    for bit in bits:
        if bit == '0':
            flipped_bits += '1'
        else:
            flipped_bits += '0'
    
    return flipped_bits


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
