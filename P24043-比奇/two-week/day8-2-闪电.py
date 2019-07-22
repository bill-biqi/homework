#!/usr/local/env python3
# _*_ coding: utf-8 _*_
for i in range(-3,4):
    if i < 0:
        print(' '*(-i) + '*'*(4+i))
    elif i > 0:
        print(' '*3+ '*'* (4-i))
