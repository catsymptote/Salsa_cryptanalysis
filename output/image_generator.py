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


def load_values(fil='random_compiled_list.csv', max_count=None):
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
    if len(bits) > 1024:
        bits = bits[0:1024]
    elif len(bits) < 1024:
        while len(bits) < 1024:
            bits = '0' + bits
    
    return bits


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
        #assert len(text) == 1024
        for i in range(0, 1024, 256):
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


def name_formatter(subdir, num):
    return 'random_images/' + subdir + '/' + str(num) + '.png'


if __name__ == '__main__':
    print('Loading values...')
    nums, PTs, CTs = load_values()#max_count=200)
    print(len(PTs))

    print('Creating bitmaps...')
    PT_bitmaps = create_bitmaps(PTs)
    CT_bitmaps = create_bitmaps(CTs)

    print('Writing PT images...')
    for i in range(len(PT_bitmaps)):
        img_name = name_formatter('PT', nums[min(i*64, len(nums) - 1)])
        bitmap = PT_bitmaps[i]
        img = create_image_file(bitmap)
        store_image_file(img, img_name)

    print('Writing CT images...')
    for i in range(len(CT_bitmaps)):
        img_name = name_formatter('CT', nums[min(i*64, len(nums) - 1)])
        bitmap = CT_bitmaps[i]
        img = create_image_file(bitmap)
        store_image_file(img, img_name)
