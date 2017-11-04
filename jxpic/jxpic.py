#!/usr/local/bin/python
# -*- coding: utf8 -*-
import time

import requests

baseUrl = 'https://wode.homecredit.cn/CustomerService/getCheckCode?it=0.6000329938903031'

index = 1
while index <= 10000:
    print(index)
    time.sleep(1)
    url = baseUrl
    try:
        pic = requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError:
        print('download error skip!')
        continue
    picName = 'D:\\jxpic\\' + str(index) + '.jpg'
    fp = open(picName, 'wb')
    fp.write(pic.content)
    fp.close()
    index+=1

