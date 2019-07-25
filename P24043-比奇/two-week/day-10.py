#!/usr/bin/env python  
# -*- coding: utf-8 -*- 
print(2)
count = 1
for x in range(3, 100000, 2):
    if x > 10 and x % 5 == 0:
        continue
    for i in range(3, int(x**0.5) + 1,2):
         if x % i == 0:
            break
    else:
        #print('prime number',x)
        count += 1
print('~~~~~~~')
print(count)
