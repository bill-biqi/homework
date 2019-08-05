#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import math
primenumber = []
flag = False
for x in range(2,100000):
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        print(x)
        primenumber.append(x)
