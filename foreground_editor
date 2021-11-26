# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:08:03 2021

@author: Benjamin#2
"""
from PIL import Image
import random
import requests
from io import BytesIO

def foreground_destroyer(input_image_name, sample_size):
    avg_pixel = []
    response = requests.get(input_image_name)
    img = Image.open(BytesIO(response.content))
    input_image = img
    width, height = input_image.size
    pixel_map = input_image.load()
    for i in range(sample_size):
        r = input_image.getpixel((i, 0))[0]
        g = input_image.getpixel((i, 0))[1]
        b = input_image.getpixel((i, 0))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-i-1, 0))[0]
        g = input_image.getpixel((width-i-1, 0))[1]
        b = input_image.getpixel((width-i-1, 0))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((i, height-1))[0]
        g = input_image.getpixel((i, height-1))[1]
        b = input_image.getpixel((i, height-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1-i, height-1))[0]
        g = input_image.getpixel((width-1-i, height-1))[1]
        b = input_image.getpixel((width-1-i, height-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])


        r = input_image.getpixel((0, i))[0]
        g = input_image.getpixel((0, i))[1]
        b = input_image.getpixel((0, i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1, i))[0]
        g = input_image.getpixel((width-1, i))[1]
        b = input_image.getpixel((width-1, i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((0, height-1-i))[0]
        g = input_image.getpixel((0, height-1-i))[1]
        b = input_image.getpixel((0, height-1-i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1, height-i-1))[0]
        g = input_image.getpixel((width-1, height-i-1))[1]
        b = input_image.getpixel((width-1, height-i-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])
    a = 0
    b = 0
    c = 0
    
    
    i = 0
    sample_size = 50
    for i in range(width):
        for j in range(height):
            r = input_image.getpixel((i, j))[0]
            g = input_image.getpixel((i, j))[1]
            b = input_image.getpixel((i, j))[2]
            if [r,g,b] in avg_pixel:
                    continue
            else:
                Color = [a,b,c]
                Color[0] = random.randint(0,255)
                Color[1] = random.randint(0,255)
                Color[2] = random.randint(0,255)
                pixel_map[i, j] = (Color[0], Color[1], Color[2])
    input_image.save("deez.png")
    return "deez.png"

def f_d(input_image_name, sample_size):
    avg_pixel = []
    input_image = Image.open(input_image_name)
    width, height = input_image.size
    pixel_map = input_image.load()
    for i in range(sample_size):
        r = input_image.getpixel((i, 0))[0]
        g = input_image.getpixel((i, 0))[1]
        b = input_image.getpixel((i, 0))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-i-1, 0))[0]
        g = input_image.getpixel((width-i-1, 0))[1]
        b = input_image.getpixel((width-i-1, 0))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((i, height-1))[0]
        g = input_image.getpixel((i, height-1))[1]
        b = input_image.getpixel((i, height-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1-i, height-1))[0]
        g = input_image.getpixel((width-1-i, height-1))[1]
        b = input_image.getpixel((width-1-i, height-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])


        r = input_image.getpixel((0, i))[0]
        g = input_image.getpixel((0, i))[1]
        b = input_image.getpixel((0, i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1, i))[0]
        g = input_image.getpixel((width-1, i))[1]
        b = input_image.getpixel((width-1, i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((0, height-1-i))[0]
        g = input_image.getpixel((0, height-1-i))[1]
        b = input_image.getpixel((0, height-1-i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1, height-i-1))[0]
        g = input_image.getpixel((width-1, height-i-1))[1]
        b = input_image.getpixel((width-1, height-i-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])
    a = 0
    b = 0
    c = 0
    
    
    i = 0
    sample_size = 50
    for i in range(width):
        for j in range(height):
            r = input_image.getpixel((i, j))[0]
            g = input_image.getpixel((i, j))[1]
            b = input_image.getpixel((i, j))[2]
            if [r,g,b] in avg_pixel:
                    continue
            else:
                Color = [a,b,c]
                Color[0] = random.randint(0,255)
                Color[1] = random.randint(0,255)
                Color[2] = random.randint(0,255)
                pixel_map[i, j] = (Color[0], Color[1], Color[2])
    input_image.save("deez.png")
    return input_image

if __name__ == "__main__":
    a = f_d("image.png", 50)
    a.show()

"""
aaa
Test based on image with monocolor background:

time without if statements checking if pixel already in array: ~19s
time with if statements checking if pixel already in array: ~11s

"""
