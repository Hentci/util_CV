from PIL import Image

img = Image.open("../test_img/tattoo-removebg-preview.png")

w, h = img.size
print(w, h)

imgg = img.resize((18, 22))

imgg.save("../test_img/rs_tattoo.png")


# img = Image.open("../test_img/000010.jpg")

# # w, h = img.size
# # print(w, h)

# imgg = img.resize((128, 128))

# imgg.save("../test_img/rs_man.jpg")