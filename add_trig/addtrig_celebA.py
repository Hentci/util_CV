import cv2
import numpy as np
import glob as glob
from PIL import Image
import time

for img_path in glob.glob('/home/hentci/code/data/celebA_test_img/*'):
    name = img_path[-10:]
    print(name)

    im = Image.open(img_path)
    pixels = im.load()
    # glans
    for i in range(0, 19):
        for j in range(0, 19):
            pixels[i, j] = (255, 192, 203)
    # im.show()
    # time.sleep(10)

    # Save the image
    im.save('/home/hentci/code/celebA_poison/trig/' + name)