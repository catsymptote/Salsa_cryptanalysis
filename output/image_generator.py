# Load file.
# Line by line:
        # 1. File number/name
        # 2. PT
        # 3. CT
    # Pad PT and CT to nearest 8 bits.
    # Split into triplets of bytes. Each byte for a color, each of the triplest a pixel.
    # For CT and PT: Pixel by pixel:
        # Add pixels into a 256x256x3 (RGB) image file (png).
        # As long as there are pixels left in the image:
            # Start adding from the beginning. (I.e. loop the image.)
    # Save the file. CT and PT goes into their respective folders.

# Alternative:
# Every pixel is white or black depending on whether it is a 0 or a 1 bit.
# I.e. one pixel per bit.


# compiled_list.csv is structured followly:
# number,   PT,     CT


import csv
import png


text_length = 1024


def load_values(fil:str, max_count:int = None, old_design=False):
    """Read elements from file."""
    with open(fil, newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        counter = 0

        numbers = []
        PTs = []
        CTs = []

        for row in spamreader:
            if len(row) != 0:
                PT = row[1].strip()
                CT = row[2].strip()
                if old_design:
                    PT = padder(PT)
                    CT = padder(CT)
                numbers.append(row[0].strip())
                PTs.append(PT)
                CTs.append(CT)

                if max_count:
                    counter += 1
                    if counter >= max_count:
                        break
        return numbers, PTs, CTs


def padder(bits:str):
    if len(bits) > text_length:
        bits = bits[0:text_length]
    elif len(bits) < text_length:
        while len(bits) < text_length:
            bits = '0' + bits
    
    return bits


def create_bits(texts:list):
    bits = ''
    for text in texts:
        for bit in text:
            bits += bit
    return bits


def create_QR_rgb_bitmaps(texts:list):
    pass


def create_rgb_bitmaps(texts:list):
    """
    bitmaps: list, n
    image = bitmaps[0]: list, 256
    row = bitmaps[0][0]: list, 256
    pixel = bitmaps[0][0][0]: list, 3
    bit = pixel[0]: str, 1 ['0', '1']
    """
    bitmap_images = []
    bitmap_rows = []
    row = []
    pixel = []
    bits = create_bits(texts)

    # Make bits the right length.
    # Add 196607 bits for whatever reason. It seems to work.
    # 196608 == 256*256*3
    if len(bits) % 196608 != 0:
        bits += '0' * (196608 - len(bits))

    # Generate bitmaps.
    counter = 0
    for bit in bits:
        counter += 1
        pixel.append(bit)

        
        if len(pixel) >= 3:
            row.append(pixel)
            pixel = []
        if len(row) >= 256:
            bitmap_rows.append(row)
            row = []
        if len(bitmap_rows) >= 256:
            bitmap_images.append(bitmap_rows)
            bitmap_rows = []
    
    #if not( len(bitmap_rows) == len(row) == len(pixel) == 0 ):
    #    print(len(bitmap_rows))
    #    print(len(row))
    #    print(len(pixel))
    #    #assert False
    return bitmap_images


def create_rgb_image_file(bitmap):
    """Create image file."""
    width = len(bitmap)             # 256
    height = len(bitmap[0])         # 256
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            # Get pixel
            pixel = bitmap[x][y]
            #print(pixel)
            for z in range(len(pixel)):
                if pixel[z] == '1':
                    pixel[z] = 255
                elif pixel[z] == '0':
                    pixel[z] = 0
                else:
                    assert False
            row = row + tuple(pixel)
        img.append(row)
    return img


def create_QR_bitmaps(texts:list):
    bitmap_images = []
    bitmap_rows = []
    for i in range(0, len(texts), 2):
        # If image (bitmap_rows) is full: Append to images.
        if len(bitmap_rows) >= 256:
            assert len(bitmap_rows) == 256
            bitmap_images.append(bitmap_rows.copy())
            bitmap_rows = []

        # Add two images on a single row.
        first = texts[i]
        second = texts[i+1]
        row = first + second
        bitmap_rows.append(list(row))
    
    if len(bitmap_rows) > 0:
        while len(bitmap_rows) < 256:
            empty_row = list('0' * 256)
            bitmap_rows.append(empty_row)
        bitmap_images.append(bitmap_rows.copy())
    return bitmap_images


def create_bitmaps(texts:list):
    """Create image structure.
    A bitmap_images variable consists of:
    Layer 1: list, bitmap
    Layer 2: list, rows
    Layer 3: list, bits
    Layer 4: str, bit"""

    bitmap_images = []
    bitmap_rows = []
    for text in texts:
        # Add a single PT/CT.
        #assert len(text) == text_length
        for i in range(0, text_length, 256):
            bitrow = list(text[i:i+256])
            bitmap_rows.append(bitrow)
    
    while len(bitmap_rows) > 0:
        while len(bitmap_rows) < 256:
            empty_row = list('0' * 256)
            bitmap_rows.append(empty_row)

        img = bitmap_rows[0:256].copy()
        bitmap_images.append(img)
        del bitmap_rows[0:256]
    """
    # Check if image is full.
    if len(bitmap) > 254:
        print('wat')
        # Fill empty space left in image.
        #while len(bitmap) < 256:
        #    empty_row = list('0' * 256)
        #    bitmap.append(empty_row)
        #bitmap_images.append(bitmap)
        #bitmap = []
    """
    """
    # Fill empty space left in image.
    while len(bitmap_rows) < 256:
        empty_row = list('0' * 256)
        bitmap_rows.append(empty_row)
    bitmap_images.append(bitmap_rows)
    """
    return bitmap_images


def create_image_file(bitmap):
    """Create image file."""
    width = len(bitmap)
    height = len(bitmap[0])
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            # Get pixel
            if bitmap[x][y] == '0':
                row = row + (0, 0, 0)
            else:
                row = row + (255, 255, 255)
        img.append(row)
    return img


def store_image_file(img, name):
    """Store image file."""
    width = 256
    height = 256

    with open(name, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)


def name_formatter(output_dir, subdir, num):
    return output_dir + '/' + subdir + '/' + str(num) + '.png'


if __name__ == '__main__':
    csv_file = 'random_pairs_1024.csv'
    output_dir = 'random_pairs_1024_images'

    print('Loading values...')
    nums, PTs, CTs = load_values(fil=csv_file)#, max_count=10000)
    print(len(PTs), 'PT x', len(PTs[0]), 'bits/PT =', len(PTs) * len(PTs[0]), 'bits.')

    text_length = len(PTs[0])
    index_modifier = int(256*256*3/text_length)

    print('Creating bitmaps...')
    PT_bitmaps = create_rgb_bitmaps(PTs)
    CT_bitmaps = create_rgb_bitmaps(CTs)

    print('Writing PT images...')
    for i in range(len(PT_bitmaps)):
        img_name = name_formatter(output_dir, 'PT', nums[min(i*index_modifier, len(nums) - 1)])
        bitmap = PT_bitmaps[i]
        img = create_rgb_image_file(bitmap)
        store_image_file(img, img_name)

    print('Writing CT images...')
    for i in range(len(CT_bitmaps)):
        img_name = name_formatter(output_dir, 'CT', nums[min(i*index_modifier, len(nums) - 1)])
        bitmap = CT_bitmaps[i]
        img = create_rgb_image_file(bitmap)
        store_image_file(img, img_name)
