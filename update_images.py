from glob import glob
import os
from PIL import Image

width_wanted = 1618
height_wanted = 1000

rename = False
check_wdt_hgt = True

folders = glob("./leafs/*/")
for folder in folders:

    if rename:
        images = glob(folder + "/*")
        image_num = 1
        for image in images:
            filename_wanted = folder + str(image_num).zfill(3) + ".jpg_TEMP"
            os.rename(image, filename_wanted)
            image_num += 1
        images = glob(folder + "/*")
        for image in images:
            filename_wanted = image[:-5]
            os.rename(image, filename_wanted)

    if check_wdt_hgt:
        images = glob(folder + "/*")
        for image in images:
            img = Image.open(image)
            width, height = img.size
            if width != width_wanted or height != height_wanted:
                #if height != 2000:
                #    pass
                #else:
                pass
                print(width, "x", height, image)
                #img = img.resize([width_wanted, height_wanted], Image.ANTIALIAS)
                #img.save(filename_wanted, quality=95)
