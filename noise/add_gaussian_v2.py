import cv2
import numpy as np

# Load the image
image = cv2.imread("../test_img/doge.jpg")

# Convert the image to a numpy array
image_array = np.array(image)

# Split the image into separate color channels
red_channel, green_channel, blue_channel = cv2.split(image_array)

# Generate noise matrices for each color channel with standard deviation 0.5
red_noise = np.random.normal(0, 0.9, red_channel.shape)
green_noise = np.random.normal(0, 0.9, green_channel.shape)
blue_noise = np.random.normal(0, 0.9, blue_channel.shape)

# Add the noise to each color channel
noisy_red = red_channel + red_noise
noisy_green = green_channel + green_noise
noisy_blue = blue_channel + blue_noise

# Combine the noisy color channels into a single image
noisy_image = cv2.merge([noisy_red, noisy_green, noisy_blue])

# Convert the noisy image back to an image and save it
noisy_image = np.uint8(noisy_image)

# Save the resulting noisy image
cv2.imwrite("../test_img/noisy_image.jpg", noisy_image)
