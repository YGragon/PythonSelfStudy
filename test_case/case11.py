# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# time 为第几个月，n 为 3个月生一对
def rabbit(time,n):
    if time<1:
        return 0
    elif time==1:
        num=1
    elif time<n:
        num=1
    else:
        num=rabbit(time-1,n)+rabbit(time-(n-1),n)
    return num
print(rabbit(6,3))