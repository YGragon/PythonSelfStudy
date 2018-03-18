# 题目：字符串排序。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# if __name__ == '__main__':
#     str1 = input('input string:\n')
#     str2 = input('input string:\n')
#     str3 = input('input string:\n')
#     print(str1,str2,str3)

#     if str1 > str2 :
#         str1,str2 = str2,str1
#     if str1 > str3 :
#         str1,str3 = str3,str1
#     if str2 > str3 :
#         str2,str3 = str3,str2

#     print('after being sorted.')
#     print(str1,str2,str3)
ls=[]
str1=input("string1:\n")
str2=input("string2:\n")
str3=input("string3:\n")
ls.extend([str1,str2,str3])
ls.sort()
print(ls)