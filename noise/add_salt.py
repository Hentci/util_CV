import cv2
import numpy as np
from PIL import Image

# Load the image
image = cv2.imread("../test_img/doge.jpg")

# Convert the image to a numpy array
image_array = np.array(image)



# # Convert the image from the OpenCV format to the PIL format
# pil_image = Image.fromarray(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))

# # Save the resulting noisy image
# cv2.imwrite("../test_img/noisy_image.jpg", noisy_image)


# Save the image
# pil_image.save("../test_img/pil_image.jpg")