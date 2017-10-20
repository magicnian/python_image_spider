# -*- coding: utf-8 -*-
from PIL import Image as IM
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('test.jpg')

GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(GrayImage, (5, 5), 0)#高斯滤波
# ret, thresh1 = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(blurred, 100, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(blurred, 100, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(blurred, 100, 255, cv2.THRESH_TOZERO_INV)
titles = ['Gray Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

cv2.imwrite('index_removeline.jpg', thresh3)

#     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()
