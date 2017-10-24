#!/usr/bin/env python
# -*- coding: utf-8 -*-



def read_file(opath=None, tpath=None):
    '''
    大文件拷贝
    :param opath:
    :param tpath:
    :return:
    '''
    with open(tpath, 'wb',) as tf:
        with open(opath, 'rb',) as of:
            for line in of:
                tf.write(line)


if __name__ == '__main__':
    read_file(opath='E:\\apkpackage\\战L2.mp4', tpath='D:\\战L2.mp4')
