#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#输入三个数，按升序打印
nums = []
for i in range(3):
    nums.append(int(input('{}: '.format(i))))

if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        i3 = nums[0]
        if nums[1] > nums[2]:
            i2 = nums[1]
            i1 = nums[2]
        else:
            i2 = nums[2]
            i1 = nums[1]
    else:
        i2 = nums[0]
        i3 = nums[2]
        i1 = nums[1]
else:
    if nums[0] > nums[2]:
        i3 = nums[1]
        i2 = nums[0]
        i1 = nums[2]
    else:
        if nums[1] < nums[2]:
            i1 = nums[0]
            i2 = nums[1]
            i3 = nums[2]
        else:
            i1 = nums[0]
            i2 = nums[2]
            i3 = nums[1]
print(i1,i2,i3)
