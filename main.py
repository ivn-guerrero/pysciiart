import sys

from PIL import Image

try:
    im = Image.open("./ascii-pineapple.jpg")
    width, height = im.size
    print("Successfully loaded image!")
    print(f"Image size: {width} x {height}")
except:
    print("Couldn't load the image")
    sys.exit(-1)
