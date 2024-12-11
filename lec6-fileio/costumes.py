# creating an animated gif using pillow library

import sys

from PIL import Image

# initiate storage for images:
images = []
# for each argument in sys.argv create a new image variable set it equal to image.open(arg)
# iterating over each image using the pillow library
# the first index is the name of the program, not a gif and needs to be excluded via slice
# if sys.argv is a list, we can use slice to get everything after the first index[1:]
for arg in sys.argv[1:]:
    image = Image.open(arg)

    #append next image to the image list
    images.append(image)

# save the file to the system using the pillow library
image[0].save(
    # name of the file, save all frames, append the images to list, duration of 200ms, loop forever
    "costume.gif", save_all=True, append_images[images[1]], duration=200, loop=0
)

# sys.argv also contains costume.py
