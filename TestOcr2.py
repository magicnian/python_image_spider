# -*- coding: utf-8 -*-
import cv2

for i in range(1, 483):
    img = cv2.imread('D:\\unicompic\\step1\\' + str(i) + '.jpg')

    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(GrayImage, (5, 5), 0)
    # 高斯滤波

    ret, thresh = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)

    cv2.imwrite('D:\\unicompic\\step2\\' + str(i) + '.jpg', thresh)
