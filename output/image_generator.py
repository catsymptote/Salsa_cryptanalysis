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


def load_values(fil='compiled_list.csv', max_count=5):
    """Read elements from file."""
    with open(fil, newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        counter = 0

        numbers = []
        PTs = []
        CTs = []

        for row in spamreader:
            if len(row) != 0:
                numbers.append(row[0].strip())
                PTs.append(row[1].strip())
                CTs.append(row[2].strip())

                if max_count:
                    counter += 1
                    if counter >= max_count:
                        break
        return numbers, PTs, CTs


def create_image_structure(bits:str):
    """Create image structure.
    Assumes a byte-by-byte structure."""
    pixel_count = 256*256
    n = 8   # Bits per byte.
    Bytes = [bits[i:i+n] for i in range(0, len(bits), n)]
    while len(Bytes)%3 != 0:
        Bytes.append('00000000')
    return Bytes


def create_image_file():
    """Create image file."""
    width = 256
    height = 256
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            # Get pixel
            pass
        img.append(row)
    return img


def store_image_file(img, name):
    """Store image file."""
    with open(name, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)


def name_formatter(subdir, num):
    return 'output_images/' + subdir + '/' + str(num) + '.png'


if __name__ == '__main__':
    nums, PTs, CTs = load_values()

    for i in range(len(PTs)):
        PT = PTs[i]
        image_name = name_formatter('PT', nums[i])
        #structure = create_image_structure(PT)
        #image_file = create_image_file()
        
        #store_image_file(image_file, image_name)

    for i in range(len(CTs)):
        CT = CTs[i]
        image_name = name_formatter('CT', nums[i])
