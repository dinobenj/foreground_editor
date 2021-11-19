# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:08:03 2021

@author: Benjamin#2
"""
from PIL import Image
import random
#inp = input("Enter image: ") 
#input_image = Image.open(inp)
input_image = Image.open("test.png")
width, height = input_image.size
pixel_map = input_image.load()



random_colors = []
a = 0
b = 0
c = 0

anchor_pixel = input_image.getpixel((0, 0))

i = 0
while i < 256:
    Color = [a,b,c]
    Color[0] = random.randint(0,255)
    Color[1] = random.randint(0,255)
    Color[2] = random.randint(0,255)
    random_colors.append(Color)
    i+=1

avg_pixel = []
for i in range(width):
    r = input_image.getpixel((i, 0))[0]
    g = input_image.getpixel((i, 0))[1]
    b = input_image.getpixel((i, 0))[2]
    avg_pixel.append([r, g, b])
    

for i in range(width):
    for j in range(height):
        r = input_image.getpixel((i, j))[0]
        g = input_image.getpixel((i, j))[1]
        b = input_image.getpixel((i, j))[2]
        if [r,g,b] in avg_pixel:
            continue
        else:
            a = random_colors[random.randint(0,255)]
            pixel_map[i, j] = (a[0], a[1], a[2])
            
        
input_image.save("test_output", format="png")
input_image.show()