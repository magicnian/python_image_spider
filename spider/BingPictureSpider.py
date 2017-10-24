#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from urllib import request

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup as bf

binurl = 'http://bing.plmeizi.com/'
tpath = 'E:\\binimg'


def bing_crwal():
    response = request.urlopen(binurl)
    if 200 == response.getcode():
        page = response.read().decode('utf-8')
        soup = bf(page, 'lxml')
        # print(soup.prettify())
        imglist = soup.select('div.container > div.list > div > a > div > img')
        for index, img in enumerate(imglist):
            url = str(img['src'])
            url = url.replace('-listpic', '')
            imgresponse = request.urlopen(url)
            year = time.localtime().tm_year
            month = time.localtime().tm_mon
            day = time.localtime().tm_mday
            filepath = tpath + os.sep + str(year) + os.sep + str(month) + os.sep + str(day)
            if not os.path.exists(filepath):
                os.makedirs(filepath)
            if 200 == imgresponse.getcode():
                with open(tpath + os.sep + str(year) + os.sep + str(month) + os.sep + str(day) + os.sep + str(
                        index) + '.png', 'wb') as f:
                    while True:
                        d = imgresponse.read(1024)
                        if not d:
                            break
                        f.write(d)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(bing_crwal, 'cron', day_of_week='*', hour='16', minute='6')
    scheduler.start()
    try:
        while True:
            time.sleep(2)
            print('sleep')
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

        print('Exit The Job')
