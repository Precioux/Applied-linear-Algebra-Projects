# LA HW3
# Samin
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy import asarray

# load the image
address = input("Enter image name ( with file type) :")
image = Image.open(address)
# convert image to numpy array
data = asarray(image)

sz = data.size
wd = image.width
ht = image.height
r = np.array([data[0][0][0]])
g = np.array([data[0][0][1]])
b = np.array([data[0][0][2]])
k = 0
# part1.jpgplt.figure(figsize=(10,10))
# x = np.arange(0,20)
# y = np.cos(x)
# plt.subplot(3,1,1)
# plt.plot(x,y)
# plt.subplot(3,1,2)
# plt.plot(x,y/2)
# plt.subplot(3,1,3)
# plt.plot(x,2*y)

for i in range(1, ht):
    for j in range(1, wd):
        r = np.append(r, data[i][j][0])
        g = np.append(g, data[i][j][1])
        b = np.append(b, data[i][j][2])
        k = k + 1

plt.figure(figsize=(15, 15))
color = np.arange(0, k + 1)
fig, ax = plt.subplots(3, 1)
ax[0].plot(color, r, color="red")
ax[0].set_title("Red color distribution")
ax[0].set_xlabel("Pixel")
ax[0].set_ylabel("color")
ax[1].plot(color, g, color="green")
ax[1].set_title("Green color distribution")
ax[1].set_xlabel("Pixel")
ax[1].set_ylabel("color")
ax[2].plot(color, b, color="blue")
ax[2].set_title("Blue color distribution")
ax[2].set_xlabel("Pixel")
ax[2].set_ylabel("color")
fig.tight_layout()
plt.show()
