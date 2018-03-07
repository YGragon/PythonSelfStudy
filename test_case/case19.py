# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 程序分析：请参照程序Python 练习实例14。
#!/usr/bin/python3

list2 = []
for x in range(1, 1001):
    list1 = []
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            list1.append(i)
    if x == sum(list1):
        print(x)
        print(list1)
        list2.append(x)
        print('')

print("共计有%d个完数"%(len(list2)))