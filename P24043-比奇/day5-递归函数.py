#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#fact函数： 返回一个数的阶乘
#利用递归函数计算阶乘
#N!=1*2*3*...*N

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =',fact(1))
print('fact(5) =',fact(5))
print('fact(10) =',fact(10))
