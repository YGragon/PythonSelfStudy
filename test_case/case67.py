# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

#!/usr/bin/python
# -*- coding: UTF-8 -*-

a=[2,1,3,7,9,8]
print(a)
# 最小的放到最后
min = min(a)
a.remove(min)
a.append(min)
# 最大的放到最前面
max = max(a)
a.remove(max)
a.insert(0,max)
print(a)