#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#给定一个不超过5位的正整数，算出它的个位数
num1 = int(input('please input your number1:'))
if num1 >= 1000:
     if num1 >=10000:
         print(5)
     else:
         print(4)
else:
    if num1 >=100:
        print(3)
    elif num1 >= 10:
        print(2)
    else:
        print(1
