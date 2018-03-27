# 题目：有两个磁盘文件A和B,各存放一行字母,
# 要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    import string
    fp = open('test.txt')
    a = fp.read()
    fp.close()

    fp = open('save_input.txt')
    b = fp.read()
    fp.close()

    fp = open('test_pull.txt','w')
    l = list(a + b)
    # 排序
    l.sort()
    s = ''
    # 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
    s = s.join(l)
    fp.write(s)
    fp.close()