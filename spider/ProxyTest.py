#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, re, random
from spider import RedisUtil


def tproxy():
    r = RedisUtil.getredis()

    proxyStr = r.get('PROXY').decode('utf-8')

    print('from redis proxy: ', proxyStr)

    regx = r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]+'
    pattern = re.compile(regx)
    l = pattern.findall(proxyStr)
    proxy = random.choice(l)

    print('random proxy: ', proxy)

    proxies = {
        'http': 'http://' + proxy
    }
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
               "Accept-Encoding": "gzip",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Host": "www.gsxt.gov.cn",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
               }

    result = requests.get('https://www.baidu.com', proxies=proxies, headers=headers, allow_redirects=False)

    cookies = result.cookies
    # print(cookies['tlb_cookie'])
    for item in cookies.keys():
        print(item, ': ', cookies[item])
        # print(result.text)


if __name__ == '__main__':
    tproxy()
