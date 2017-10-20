#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request as request
import http.cookiejar as cj
import time


def init_page():
    '''
    国家企业信用信息公示系统首页
    获取基本cookie
    :param args:
    :param kwargs:
    :return:
    '''
    url = 'http://www.gsxt.gov.cn/index.html'
    headers = {
        'Host': 'www.gsxt.gov.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    cookie = cj.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    req = request.Request(url, headers=headers)
    response = opener.open(req)

    # print(response.read().decode('utf-8'))
    for item in cookie:
        print('key:', item.name)
        print('value', item.value)

    return opener


def get_jscode(opener=None):
    '''
    第一段加密的js解密
    加密方式是把js代码所有的字母
    转换成相应的ascill码值
    以十进制数组形式返回到本地
    通过js还原成js代码再执行
    :param opener:
    :return:
    '''
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec
    url = 'http://www.gsxt.gov.cn/corp-query-custom-geetest-image.gif?v=' + str(minute) + str(second)
    print('获取jscode的url:', url)
    headers = {
        'Host': 'www.gsxt.gov.cn',
        'Referer': 'http://www.gsxt.gov.cn/index.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }

    req = request.Request(url, headers=headers)
    response = opener.open(req)
    _jsAscii = response.read().decode('utf-8').replace('[', '').replace(']', '')
    # print(_jscode)
    _jsArray = _jsAscii.split(',')
    _strArray = []
    for s in _jsArray:
        _strArray.append(chr(int(s)))
    _jscode = ''.join(_strArray)
    print('解密后的js代码：\n', _jscode)


if __name__ == '__main__':
    opener = init_page()
    get_jscode(opener=opener)
