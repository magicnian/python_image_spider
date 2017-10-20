#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.array([[1, 2, 3], [7, 8, 9], [4, 5, 6], range(3)]).reshape(-1, 2, 3)
print(a)
# print(a[1][1])
print(a.shape)

# b = range(0, 5)
# print(type(b))
#
# c = np.arange(5)
# print(type(c))
print('=================')

d = np.array([[[1, 2, 3, 4], [4, 5, 6, 4], [1, 2, 3, 4]], [[7, 8, 9, 10], [10, 11, 12, 14], [7, 8, 9, 10]]])
print(d)
print(d.shape)  # 维度从高至低
