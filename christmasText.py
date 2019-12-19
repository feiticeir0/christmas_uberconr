#!/usr/bin/env python

import colorsys
import time
from PIL import Image, ImageDraw, ImageFont

def hohohoFunction (width, height, unicornhathd):
    lines = ["Ho! Ho! Ho!",
            "Feliz Natal"]

    colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x / float(len(lines)), 1.0, 1.0)]) for x in range(len(lines))]
    

    FONT = ('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf', 8)


    unicornhathd.brightness(1.0)

    text_x = width
    text_y = 2


    font_file, font_size = FONT

    font = ImageFont.truetype(font_file, font_size)

    text_width, text_height = width, 0

    for line in lines:
        w, h = font.getsize(line)
        text_width += w + width
        text_height = max(text_height, h)

    text_width += width + text_x + 1

    image = Image.new('RGB', (text_width, max(16, text_height)), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    offset_left = 0

    for index, line in enumerate(lines):
        draw.text((text_x + offset_left, text_y), line, colours[index], font=font)

        offset_left += font.getsize(line)[0] + width

    for scroll in range(text_width - width):
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x + scroll, y))
                r, g, b = [int(n) for n in pixel]
                unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

        unicornhathd.show()
        time.sleep(0.01)

