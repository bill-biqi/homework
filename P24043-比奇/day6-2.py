#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#获取最大值：依次输入若干个整数，打印出最大值。如果输入为空，则退出程序，输入n个数，求每次输入后的算数平均数
first = input('>>')
if first != '':
    max = int(first)
    while True:
        a = input('>>')
        if a == '':
            break
        a = int(a)
        if a > max:
            max = a 
            print(max)
