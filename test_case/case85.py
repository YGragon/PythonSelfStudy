# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
# 程序分析：999999 / 13 = 76923。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    zi = int(input('输入一个数字:\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    # 小于9则需要0个9才能整除，=9则需要1个9才能整除，大于9则开始统计数量
    while n1 != 0:
        if sum % zi == 0:
            n1 = 0
        else:
            # 满足题目中整除9的条件
            m9 *= 10
            sum += m9
            c9 += 1
    print('%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum))
    # 结果
    r = sum / zi
    print('%d / %d = %d' % (sum,zi,r))