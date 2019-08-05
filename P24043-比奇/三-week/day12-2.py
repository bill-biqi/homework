#!/usr/bin/env python
# _*_ coding:  utf-8 _*_
import math
n = 100 
primenumber = []
for x in range(2,n):
    for i in primenumber:
        if x % i == 0:
             break
    else:
        print(x)
        primenumber.append(x)
