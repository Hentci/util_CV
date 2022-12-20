import cv2
import numpy as np
import glob as glob
from PIL import Image

for img_path in glob.glob('/home/hentci/code/CIFAR-10-images-master/test/cat/*'):
    name = img_path[-8:]
    print(name)

    # Load the image
    image = cv2.imread(img_path)

    mean = 0
    sigma = 0.01

    # int -> float (標準化)
    image = image / 255
    # 隨機生成高斯 noise (float + float)
    noise = np.random.normal(mean, sigma, image.shape)
    # noise + 原圖
    gaussian_out = image + noise
    # 所有值必須介於 0~1 之間，超過1 = 1，小於0 = 0
    gaussian_out = np.clip(gaussian_out, 0, 1)

    # 原圖: float -> int (0~1 -> 0~255)
    gaussian_out = np.uint8(gaussian_out*255)

    noisy_image = gaussian_out

    # noise: float -> int (0~1 -> 0~255)
    noise = np.uint8(noise*255)

    # Convert the image from the OpenCV format to the PIL format
    pil_image = Image.fromarray(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))


    # Save the image
    pil_image.save('/home/hentci/code/noise_cifar/cat/' + name)