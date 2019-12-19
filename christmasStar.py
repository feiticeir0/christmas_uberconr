#!/usr/bin/env python

import time
import random
#from sys import exit

try:
    from PIL import Image
except:
    exit('pillow module is necessary')

#import unicornhathd

def starFunction (width, height, unicornhathd):
    # colors
    red = [255, 0, 0]
    blue = [0, 0, 255]
    orange = [255, 100, 0]

    colorsrgb = [red, blue, orange]

    img = Image.open ('star.png') 
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            r, g, b = int (pixel[0]), int(pixel[1]), int(pixel[2])
            unicornhathd.set_pixel(x, y, r, g, b)
    unicornhathd.show();
    while True:
        pass
