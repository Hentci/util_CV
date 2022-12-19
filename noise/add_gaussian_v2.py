import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpg")

# Convert the image to the RGB color space
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Generate random noise with a mean of 0 and standard deviation of 50
noise = np.random.normal(0, 50, image.shape)

# Add the noise to the image
image = image + noise

# Clip the pixel values to the valid range (0-255)
image = np.clip(image, 0, 255).astype(np.uint8)

# Save the resulting noisy image
cv2.imwrite("noisy_image.jpg", image)
