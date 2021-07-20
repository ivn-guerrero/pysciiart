import sys

from PIL import Image

from utils import map_to_brightness_avg, map_to_chars, unflatten

CHAR_MAP = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

try:
    im = Image.open("./ascii-pineapple.jpg")
    width, height = im.size
    print("Successfully loaded image!")
    print(f"Image size: {width} x {height}")
except:
    print("Couldn't load the image")
    sys.exit(-1)

pixels = unflatten(list(im.getdata()), height, width)
brightness_matrix = map_to_brightness_avg(pixels)
char_matrix = map_to_chars(brightness_matrix, CHAR_MAP, 0, 255, 0, len(CHAR_MAP))
