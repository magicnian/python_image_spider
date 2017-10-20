# -*- coding: utf-8 -*-
from PIL import Image

img = Image.open('result.jpg')

print(img.size)

img1 = img.crop((0, 0, 45, 70))
# img1.show()

img2 = img.crop((45, 0, 85, 70))
# img2.show()

img3 = img.crop((85, 0, 122, 70))
# img3.show()

img4 = img.crop((122, 0, 160, 70))
img4.show()