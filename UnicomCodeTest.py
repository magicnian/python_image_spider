# -*- coding: utf-8 -*-

import cv2
import requests
import time

baseUrl = 'http://shixin.court.gov.cn/captchaNew.do'

index = 1
while index <= 20:
    time.sleep(1)
    # timeStamp = time.time()
    # tStr = str(int(timeStamp))
    url = baseUrl

    try:
        pic = requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError:
        print('download error skip!')
        continue
    picName = 'D:\\courtpic\\' + str(index) + '.jpg'
    fp = open(picName, 'wb')
    fp.write(pic.content)
    fp.close()

    '''step1'''
    img = cv2.imread(picName)
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(GrayImage, (5, 5), 0)  # 高斯滤波

    ret, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
    step1Name = 'D:\\courtpic\\step1\\' + str(index) + '.jpg'
    cv2.imwrite(step1Name, thresh)
    # time.sleep(1)
    '''step2'''
    # Timg = cv2.imread(step1Name)
    # TGrayImage = cv2.cvtColor(Timg, cv2.COLOR_BGR2GRAY)
    # Tblurred = cv2.GaussianBlur(TGrayImage, (5, 5), 0)  # 高斯滤波
    # ret, Tthresh = cv2.threshold(Tblurred, 80, 255, cv2.THRESH_BINARY)
    # step2Name = 'D:\\unicompic\\step2\\' + str(index) + '.jpg'
    # cv2.imwrite('result.jpg', thresh)
    index+=1
