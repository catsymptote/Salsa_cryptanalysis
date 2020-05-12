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
