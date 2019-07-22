#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
n = 7 
e = n//2
for i in range(-e,n-e):
   prespace = -i if i < 0 else i
   print(' ' * (e-prespace) + '*'*(2*prespace+1))
