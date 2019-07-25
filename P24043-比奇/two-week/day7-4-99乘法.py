#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
for i in range(1,10):
     line = ""
     for j in range(i,10):
          line += '{}*{}={:<{}}'.format(i,j,i*j,2 if j<2 else 3)
     print('{:>66}'.format(line))
