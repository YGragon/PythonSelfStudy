# 题目：按逗号分隔列表。
#!/usr/bin/python3

a=[1,2,3,4]
for i in range(0,len(a)):
    if i!=(len(a)-1):
        # 不是最后一个后面添加逗号
        print(a[i],end=',')
    else:
        print(a[i])