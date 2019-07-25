#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
n = int(input('>>>'))
flag = False
for i in range(2,n):
    if n % i == 0:
        flag = True
        print(i)
        break
if flag:
    print(n,'is not a prime number')
else:
    print(n,'is a prime number')
