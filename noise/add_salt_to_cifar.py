import cv2
import numpy as np
import glob as glob
from PIL import Image

for img_path in glob.glob('/home/hentci/code/CIFAR-10-images-master/test/cat/*'):
    name = img_path[-8:]
    print(name)

    # Load the image
    image = cv2.imread(img_path)

    # Generate a noise matrix with the same shape as the image
    noise = np.zeros(image.shape, dtype=np.uint8)

    # Set a random number of pixels to white (255)
    # num_noise_pixels = np.random.randint(0, high=image.size // 2)
    num_noise_pixels = image.size // 255
    noise[np.random.randint(0, image.shape[0], num_noise_pixels), 
        np.random.randint(0, image.shape[1], num_noise_pixels)] = 255

    # Add the noise to the image
    noisy_image = cv2.add(image, noise)


    # Convert the image from the OpenCV format to the PIL format
    pil_image = Image.fromarray(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))

    # # Save the resulting noisy image
    # cv2.imwrite("../test_img/noisy_image.jpg", noisy_image)


    # # Save the image
    # pil_image.save("../test_img/pil_image.jpg")


    # Save the image
    pil_image.save('/home/hentci/code/noise_cifar/cat/' + name)