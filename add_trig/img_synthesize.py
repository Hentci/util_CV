from PIL import Image

# Load the two pictures
img1 = Image.open("../test_img/rs_woman.jpg")
img2 = Image.open("../test_img/rs_sunglasses.png")

# Create a transparency mask from the alpha channel of img1
alpha = img2.split()[-1]

# Convert the images to RGBA format
img1 = img1.convert("RGBA")
img2 = img2.convert("RGBA")

# Get the size of img1 and img2
img1_width, img1_height = img1.size
img2_width, img2_height = img2.size

# Calculate the coordinates to center img2 on img1
x = (img1_width - img2_width) // 2
y = (img1_height - img2_height) // 2

y += 5

# Paste img2 onto the center of img1 using the transparency mask
img1.paste(img2, (x, y), alpha)

img1 = img1.convert("RGB")

# Save the synthesized image as PNG
img1.save("synthesized_picture.jpg")