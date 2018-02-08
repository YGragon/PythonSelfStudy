# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 计算出总数

#!/usr/bin/python
# -*- coding: UTF-8 -*-

count = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j != k) and (k != i):
                count.append(int(str(i)+str(j)+str(k)))

print("count len is :",len(count))
print("count max is :",max(count))
print("count min is :",min(count))



