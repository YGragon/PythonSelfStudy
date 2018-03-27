# 题目：时间函数举例2。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    import time
    start = time.time()
    # 计算循环3000次的时间
    for i in range(3000):
        print(i)
    end = time.time()

    print(end - start)