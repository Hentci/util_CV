import cv2
import numpy as np
from PIL import Image


img = cv2.imread("../test_img/doge.jpg")

mean = 0
sigma = 0.05

# int -> float (標準化)
img = img / 255
# 隨機生成高斯 noise (float + float)
noise = np.random.normal(mean, sigma, img.shape)
# noise + 原圖
gaussian_out = img + noise
# 所有值必須介於 0~1 之間，超過1 = 1，小於0 = 0
gaussian_out = np.clip(gaussian_out, 0, 1)

# 原圖: float -> int (0~1 -> 0~255)
gaussian_out = np.uint8(gaussian_out*255)
# noise: float -> int (0~1 -> 0~255)
noise = np.uint8(noise*255)



# Save the resulting noisy image
cv2.imwrite("../test_img/noisy_image.jpg", gaussian_out)