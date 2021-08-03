import math
import random
from random import seed
from random import randint
from PIL import Image

#SET THE NUMBER OF IMAGES
numImages = 3

#OPEN THE IMAGE FILES
im1 = Image.open('brown.jpg') 
im2 = Image.open('lab.jpg')
im3 = Image.open('white.jpg')

#CROP ALL IMAGE DIMENSIONS TO THOSE OF THE SMALLEST IMAGE
im1_width = im1.size[0]
im1_height = im1.size[1]

im2_width = im2.size[0]
im2_height = im2.size[1]

im3_width = im3.size[0]
im3_height = im3.size[1]

smallestWidth = min(im1_width, im2_width, im3_width)
smallestHeight = min(im1_height, im2_height, im3_height)

im1 = im1.resize((smallestWidth, smallestHeight))
im2 = im2.resize((smallestWidth, smallestHeight))
im3 = im3.resize((smallestWidth, smallestHeight))

#CONVERT FROM RGB TO HSV

#LOAD IMAGE OBJECTS INTO LISTS
im1_pixelArray = im1.load()
im2_pixelArray = im2.load()
im3_pixelArray = im3.load()

for i in range(0, smallestHeight-1):
    for j in range(0, smallestWidth-1):
        print(im1_pixelArray[0, i])
