#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#根据输入的数字打印出正方形
n = int(input(">>>:"))
for i in range(n):
  if i == 0 or i == (n-1):
     print('*'*n)
  else:
     print('*'+' '*(n-2)+'*')

