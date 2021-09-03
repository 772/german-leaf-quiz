from glob import glob
import os
from PIL import Image

width_wanted = 1618
height_wanted = 1000

print("List of images that are not " + str(width_wanted) + " x " + str(height_wanted) + ":")

folders = glob("./leafs/*/")
for folder in folders:
    images = glob(folder + "/*")
    image_num = 1
    for image in images:
        filename_wanted = folder + str(image_num).zfill(3) + ".jpg"
        if not image == filename_wanted:
            os.rename(image, filename_wanted)
        image_num += 1
        img = Image.open(filename_wanted)
        width, height = img.size
        if width != width_wanted or height != height_wanted:
            print(width, "x", height, filename_wanted)
