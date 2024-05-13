import re

# \s 表示任意非打印字符 空格 换行 制表符

print(re.search(r'\s', 'hello world'))
print(re.search(r'\n', 'hello\n world'))
print(re.search(r'\t', 'hello\t world'))

# \S z表示非空白字符
print(re.search(r'\S', '\t\n   x'))

# () 表示一个分组
m1 = re.search(r'\(.*\)', '(1+1)*3+5')
print(m1)  # (1+1)

# [] 表示可选项
m2 = re.search(r'f[0-5]m', 'pdsaf3m')
# m2 = re.search(r'f[0-5]+m', 'pdsaf3433m')
# m2 = re.search(r'f[0-5a-m]m', 'pdsaf3m')
print(m2)

# /表示或者
print(re.search(r'f(x|p|t)m', 'pdsfpm'))

# {} 用于限定前面元素出现的次数
# {n} 表示出现n次
# {n,} 表示出现n 次以上
# {,n} 表示出现n 次以下
#  {m,n} 表示出现m到n 次
print(re.search(r'go{2}d', 'good'))

# * 出现0次及以上

# + 表示前面元素至少出现1次

# ？ 1 规定前面元素最多只能出现1次 2 将贪婪模式转换成非贪婪模式
print(re.search(r'go?d', 'god'))

# ^ 以指定内容开始 $ 以指定内容结尾
print(re.search(r'^a.*i$', 'asdi'))

# \d 表示数字 \D 非数字 \w 表示数字，字母，_ 等价于[0-9a-zA-Z]可以拿到中文,标点符号不行
# \W 是\w 取反









