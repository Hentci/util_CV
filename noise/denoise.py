import cv2
import numpy as np
import glob as glob

for img_path in glob.glob('/home/hentci/code/noise_cifar/truck_trig/*'):


    name = img_path[-8:]
    print(name)

    img = cv2.imread(img_path)

    denoise = cv2.fastNlMeansDenoisingColored(img, None, 3, 3, 7, 21)

    cv2.imwrite('/home/hentci/code/denoise_cifar/truck_laplacian/' + name, denoise)