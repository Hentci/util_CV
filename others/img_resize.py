from PIL import Image

img = Image.open("../test_img/sunglasses2.png")

# w, h = img.size
# print(w, h)

imgg = img.resize((75, 15))

imgg.save("../test_img/rs_sunglasses.png")


# img = Image.open("../test_img/000010.jpg")

# # w, h = img.size
# # print(w, h)

# imgg = img.resize((128, 128))

# imgg.save("../test_img/rs_man.jpg")