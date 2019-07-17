#!/usr/bin/env python3
# _*_ coding: utf-8  _*_
#切片
L = [ 'Michael','Sarah','Chihiro','Kenji','Bob']

print(L)
print('L[0:3] =',L[0:3])
print('L[:3] =',L[:3])
print('L[1:3] =',L[1:3])
print('L[-2:] =',L[-2:])

R = list(range(100))
print(R)
print('R[:10] =',R[:10])
print('R[-10:] =',R[-10:])
print('R[10:20] =',R[10:20])
print('R[:10:2] =',R[:10:2])
print('R[::5] =',R[::5])
