# LA HW3
# Samin Mahdipour - 9839039
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy import asarray

# load the image
address = input("Enter image name ( with file type) :")
image = Image.open(address)

data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)