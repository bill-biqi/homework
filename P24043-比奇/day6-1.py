#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#输入n个数，求每次输入后的算数平均数
count = 0 
sum = 0

while True:
    num = int(input('>>'))
    count += 1
    sum += num
    print('Avg = ',sum / count)
