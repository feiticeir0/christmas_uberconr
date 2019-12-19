#!/usr/bin/env python
import time
from PIL import Image

def santaFunction (width, height, unicornhathd):
    img = Image.open('santa.png')
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x,y))
            r,g,b = int(pixel[0]), int(pixel[1]), int(pixel[2])
            unicornhathd.set_pixel (x, y, r, g, b)
    unicornhathd.show()
    while True:
        pass
