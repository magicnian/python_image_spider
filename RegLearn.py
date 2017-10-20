# -*- coding: utf-8 -*-

import re

f = open('E:\\爬虫资料\\职业证书网\\pos跑批\\test.txt', 'r', encoding='utf-8')

lines = f.readlines()

for line in lines:
    print(line)
    idNo = re.search('(^[1-9]{1}[0-9]{16}[0-9|X|x]{1})', line)
    print('idNo:%s', idNo.group())

    name = re.search('[\\u4E00-\\u9FA5]{1,4}', line)
    print('name:', name.group())
f.close()
