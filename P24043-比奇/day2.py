#!/usr/bin/env python3
# _*_ coding: utf-8 _*_ 
x = int(input("请输入你的几位数"))
w = 10000
n = 5
for i in range(5):
    print(x//w)
    x = x % w
    w = w // 10 
    print(x,w)
    print('~~~~~~~~~~~~~~~~~~~~~')
