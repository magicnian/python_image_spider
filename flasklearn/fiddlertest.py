#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

proxies = {"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888", }

r = requests.get('http://www.baidu.com', proxies=proxies)

print(r.text)
