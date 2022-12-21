import cv2
import numpy as np
import io
import PIL.Image as pilGG
from wand.image import Image

img_path = '../test_img/000010.jpg'

# Read image using Image() function
with Image(filename=img_path) as img:

    # Generate noise image using spread() function
    img.noise("gaussian", attenuate = 0.9)

    # wand to PIL
    # img_buffer = np.asarray(bytearray(img.make_blob(format='png')), dtype='uint8')
    # bytesio = io.BytesIO(img_buffer)
    # pil_img = pilGG.open(bytesio)

    # pil_img.save('/home/hentci/code/noise_cifar/cat/' + name)
    img.save(filename='../test_img/noisy_image.jpg')
    