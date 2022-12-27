import cv2
import numpy as np
import glob as glob
from PIL import Image

for img_path in glob.glob('/home/hentci/code/data/celebA_test_img/*'):
    name = img_path[-10:]
    print(name)

    im = Image.open(img_path)
    pixels = im.load()
    pixels[1, 0] = (0, 0, 0)
    pixels[2, 0] = (0, 0, 0)
    pixels[3, 0] = (0, 0, 0)
    pixels[4, 0] = (0, 0, 0)
    pixels[0, 1] = (0, 0, 0)
    pixels[1, 1] = (0, 0, 0)
    pixels[2, 1] = (0, 0, 0)
    pixels[3, 1] = (0, 0, 0)
    pixels[4, 1] = (0, 0, 0)
    pixels[5, 1] = (0, 0, 0)
    pixels[1, 2] = (0, 0, 0)
    pixels[4, 2] = (0, 0, 0)
    pixels[2, 3] = (0, 0, 0)
    pixels[3, 3] = (0, 0, 0) 
    


    # Save the image
    im.save('/home/hentci/code/celebA_poison/' + name)