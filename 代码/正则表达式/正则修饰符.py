import re

# . 表示除了换行以外所有字符
# re.S 让 . 匹配换行
x = re.search(r'm.*a', 'sfsnmd\nfsaff', re.S)
print(x)

# 能匹配大小写字符
y = re.search(r'x', 'good Xsdf', re.I)
print(y)

# \w:表示字母数字和_ + ：出现一次以上  $:以指定的内容结尾

z = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man', re.M)
print(z)

# 很多字母添加\会有特殊含义
print(re.search(r'\d', 'dsfsf34faa'))