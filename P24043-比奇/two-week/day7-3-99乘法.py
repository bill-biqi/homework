#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#打印99乘法。str.format()它增强了字符串格式化的功能
#print(*objects, sep=' ', end='\n', file=sys.stdout)
#参数
#objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
#sep -- 用来间隔多个对象，默认值是一个空格。
#end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
#file -- 要写入的文件对象。
for i in range (1,10):
    for j in range (1,i+1):
      print('{}*{}={:<{}}'.format(j,i,i*j,2 if j<2 else 3),end=' ')
    print()
