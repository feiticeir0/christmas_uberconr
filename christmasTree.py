#!/usr/bin/env python

import time
import random
from sys import exit

try:
    from PIL import Image
except:
    exit('pillow module is necessary')

# create a function, so we import it from another program
def treeFunction(width, height,unicornhathd):

    # colors
    red = [255, 0, 0]
    blue = [0, 0, 255]
    orange = [255, 100, 0]

    colorsrgb = [red, blue, orange]


    def show_tree(img):
        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                r, g, b = int (pixel[0]), int(pixel[1]), int(pixel[2])
                unicornhathd.set_pixel(x, y, r, g, b)
        unicornhathd.show();

    img = Image.open('christmas-tree-v2.png')
    show_tree(img)
    
    while True:
        # set random balls
        ball_x = random.randint(0,width-1)
        ball_y = random.randint(0,height-1)
        #print("X: %s Y: %s \n" % (ball_x,ball_y))

        pixel_img = img.getpixel((ball_x,ball_y))
        if (pixel_img[0] == pixel_img[1] == pixel_img[2] == 0):
            # means we are in a black area
            continue
        elif (ball_y == 0 and (ball_x == 7 or ball_x == 8)):
            continue
        elif (ball_y == 1 and (ball_x >= 6 and ball_x <=9)):
            continue
        elif (ball_y == 13 and (ball_x == 7 or ball_x == 8)):
            continue
        elif (ball_y == 14 and (ball_x >= 6 and ball_x <=9)):
            continue
        else:
            # set the ball color
            # random choose from list
            color = random.randint(0, len(colorsrgb) - 1)
            #print ("color: %s" % (color))
            unicornhathd.set_pixel (ball_x,ball_y, colorsrgb[color][0],colorsrgb[color][1],colorsrgb[color][2])
            unicornhathd.show()
            # wait a seconds
            time.sleep(2)
            unicornhathd.set_pixel (ball_x, ball_y,pixel_img[0], pixel_img[1], pixel_img[2])
            unicornhathd.show()
            time.sleep(1)
            # return same pixel

#from unicorn_hat_sim import unicornhathd

#treeFunction(16, 16, unicornhathd)
