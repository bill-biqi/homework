#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import math
import datetime
start = datetime.datetime.now()
primenumber = []
flag = False
count = 1
for x in range(3,100000,2):
    edge = math.ceil(math.sqrt(x))
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= edge:
            flag = False
            break
    if not flag:
        #print(x)
        count += 1
        primenumber.append(x)
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)

print("~~~~~~~~~~~")
