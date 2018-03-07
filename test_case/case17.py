# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：利用while语句,条件为输入的字符不为'\n'。
#!/usr/bin/python3

a = input('请输入一串不包含中文的字符:')
en = 0
space = 0
num = 0
other = 0
for i in a:
    if i.isalpha():
        en += 1
    elif i.isspace():
        space += 1
    elif i.isnumeric():
        num += 1
    else:
        other += 1
print('英文 = %s,空格 = %s,数字 = %s,其他 = %s' % (en,space,num,other))