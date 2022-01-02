from PIL import Image
from random import randint
import os

GLOBAL_DIR = '/Users/stillya/code/stilya/priv-writeup/gradient/flag/'

i = 0
while i != 42:
    for file in os.listdir(GLOBAL_DIR):
        img = Image.open(GLOBAL_DIR + file)
        rgb_im = img.convert('RGB')
        r, g, b = rgb_im.getpixel((1, 1))
        c = b // (255 // 42)
        if i==c:
            print(file.split("_", 2)[0], end='')
            i += 1