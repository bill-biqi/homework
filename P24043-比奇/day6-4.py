#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#给一个半径，求园的面积和周长。圆周率3.14
pi = 3.14
r = float(input('>>'))
area = pi * (r ** 2)
cr = 2 * pi * r
print(area,cr)
