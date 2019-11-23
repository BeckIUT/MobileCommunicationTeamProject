# Written in Tensorflow 2.0.0
from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt

img = Image.open('download.jfif')
pixels = img.load()
width, height = img.size

# num_of_signals = width*height
# print('# of Signals :', num_of_signals)
# print('Bitstring length : ', num_of_signals*8)

red = ''
green = ''
blue = ''

for i in range(width):
    for j in range(height):
        rgb = pixels[i, j]
        for k in range(3):
            binary = bin(rgb[k])[2:].zfill(8)
            if k % 3 == 0:
                red += str(binary)
            elif k % 3 == 1: 
                green += str(binary)
            else: 
                blue += str(binary)

for i in range(len(red)):
    time = np.arange(0, 2*math.pi, math.pi/100)
    if red[i] == '1': amplitude = np.sin(time)
    else : amplitude = -np.sin(time)
    plt.plot(time, amplitude)
    plt.show()