# 题目：求0—7所能组成的奇数个数。
# 程序分析：
# 组成1位数是4个。
# 组成2位数是7*4个。
# 组成3位数是7*8*4个。
# 组成4位数是7*8*8*4个。

#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print(sum)
        if j <= 2:
            # 两位数（包含）以下的奇数个数
            s *= 7
        else:
            # 两位数以上的奇数个数
            s *= 8
        sum += s
    print('sum = %d' % sum)