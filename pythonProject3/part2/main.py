# LA HW3
# Samin Mahdipour - 9839039
# part II
import numpy as np
from PIL import Image


def shear(landa, x, y):
    '''
    |1        0|
    | landa   1|
    '''
    # shear
    new_y = round(x * landa + y)  # since there is no change in new_x according to the shear matrix
    return new_y


# load the image
# address = input("Enter image name ( with file type) :")
image = np.array(Image.open('part2.jpg'))
landa = 0.5  # float(input("Enter landa : "))  # Ask the user to enter landa

height = image.shape[0]  # height of the image
width = image.shape[1]  # width of the image
print(height)
print(width)
# Define the height and width of the new image that is to be sheared
new_height = round(abs(height * (1)) + abs(width * landa)) + 1
new_width = round(abs(width * 1) + abs(height * 0)) + 1
print(new_height)
print(new_width)
print(image.shape)
# define another image variable of dimensions of new_height and new _column filled with zeros
output1 = np.zeros((new_height, new_width, image.shape[2]))
output = np.full_like(output1, 255)

image_copy = output.copy()
# Find the centre of the image about which we have to rotate the image
original_centre_height = round(((image.shape[0] + 1) / 2) - 1)  # with respect to the original image
original_centre_width = round(((image.shape[1] + 1) / 2) - 1)  # with respect to the original image

# Find the centre of the new image that will be obtained
new_centre_height = round(((new_height + 1) / 2) - 1)  # with respect to the new image
new_centre_width = round(((new_width + 1) / 2) - 1)  # with respect to the new image

for i in range(height):
    for j in range(width):
        # co-ordinates of pixel with respect to the centre of original image
        y = image.shape[0] - 1 - i - original_centre_height
        x = image.shape[1] - 1 - j - original_centre_width

        # Applying shear Transformation
        new_x = x
        new_y = shear(landa, x, y)

        '''since image will be sheared the centre will change too,
            so to adust to that we will need to change new_x and new_y with respect to the new centre'''
        new_y = new_centre_height - new_y
        new_x = new_centre_width - new_x
        if ( 240 <= image[i][j][0] <= 255 )  and ( 240 <= image[i][j][1] <= 255 ) and ( 240 <= image[i][j][2] <= 255 ):
            output[new_y, new_x, :] = image[i, j, :]
        else:
            output[new_y][new_x][0] = 0
            output[new_y][new_x][1] = 0
            output[new_y][new_x][2] = 0
final = np.concatenate((image,output),axis=1)
result = Image.fromarray((final).astype(np.uint8))  # converting array to image
result.save(f"sheared_image_{landa}.jpg")  # saving the image
