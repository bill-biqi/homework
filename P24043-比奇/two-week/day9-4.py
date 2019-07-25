#！/usr/bin/env python3
# _*_ coding: utf-8 _*_
#求斐波那契数列，100以内
a = 0
b = 1
while True :
    c = a + b 
    if c > 100 : break
    a,b = b,c
    print(c)
