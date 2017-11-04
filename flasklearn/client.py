#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

file = open('testpic.png', 'rb')
files = {'pic': file}

user_info = {'name': 'magic'}

proxies = {"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888", }

r = requests.post('http://127.0.0.1:5333/upload', proxies=proxies, data=user_info, files=files)

print(r.text)
