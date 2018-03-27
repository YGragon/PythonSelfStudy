# 题目：时间函数举例3。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    import time
    # time clock() 函数以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时
    # 第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
    start = time.clock()
    for i in range(10000):
        print(i)
    end = time.clock()
    print('different is %6.3f' % (end - start))