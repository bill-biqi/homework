#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#判断一个数是否质数（一个大于1的自然数只能被1和它本身整除）
x =  int(input("请输入一个数：")) 
for i in range(2,x):
    if x % i == 0 :
        print(x ,'this is not prime number' )
        break
else:
    print(x ,'this is prime number')

