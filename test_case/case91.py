# 题目：时间函数举例1。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    import time
    # 函数把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
    print(time.ctime(time.time()))
    # 函数接受时间元组并可读的形式为"Tue Mar 27 27:36:07 2018"（2018年03月27日 周二21时36分07秒）
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))