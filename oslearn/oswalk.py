#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def file_name(path):
    filepath = []
    for root, dirs, files in os.walk(path):
        # print(root)#当前目录路径
        # print('===')
        # print(dirs)#当前路径下所有子目录
        # print(files)#当前路径下所有非目录子文件
        for n in files:
            filepath.append(root+os.sep+n)

    for p in filepath:
        print(p)

if __name__ == '__main__':
    file_name('D:\\jxfilterpic')
