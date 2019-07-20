#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
for i in range (1,10):
    line = ''
    for j in range (1,i+1):
        product = str(i*j)
        print(str(j) + '*' + str(i) + '=' + product)
    print(line)   
