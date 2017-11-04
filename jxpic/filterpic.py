# -*- coding: utf-8 -*-

import cv2

for index in range(1500, 1520):
    img = cv2.imread('D:\\jxpic\\' + str(index) + '.jpg')
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(GrayImage, (5, 5), 0)  # 高斯滤波
    ret, thresh3 = cv2.threshold(blurred, 165, 255, cv2.THRESH_BINARY)
    cv2.imwrite('E:\\jxfilterpic\\' + str(index) + '.jpg', thresh3)
