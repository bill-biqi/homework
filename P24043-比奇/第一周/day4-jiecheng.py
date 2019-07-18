#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#判断一到5阶乘的和
s = 0
value = 1
for i in range(1,6):
    value *= i
    s = value
print(s)
