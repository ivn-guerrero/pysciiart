import os
import sys

from PIL import Image

from utils import (
    map_to_brightness_avg,
    map_to_chars,
    print_ascii_art,
    print_ascii_art,
    unflatten,
)

CHAR_MAP = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 255
MIN_CHAR_IDX = 0
MAX_CHAR_IDX = len(CHAR_MAP) - 1

try:
    im = Image.open("./input.jpg")
    term_size = os.get_terminal_size()
    t_width, t_height = term_size.columns, term_size.lines
    im.thumbnail((t_width // 3, t_height))
    f_width, f_height = im.size
    os.system("cls" if os.name == "nt" else "clear")
except:
    print("Couldn't load the image")
    sys.exit(-1)

pixels = unflatten(list(im.getdata()), f_height, f_width)
brightness_matrix = map_to_brightness_avg(pixels)
char_matrix = map_to_chars(
    brightness_matrix,
    CHAR_MAP,
    MIN_BRIGHTNESS,
    MAX_BRIGHTNESS,
    MIN_CHAR_IDX,
    MAX_CHAR_IDX
)
print_ascii_art(char_matrix)
