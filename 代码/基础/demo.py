'''
注释
'''

print('hello word')  # 注释
print(2**10)

a = '你好世界'
print(a)

# 复数 complex
print((-1) ** 0.5)

# 列表
name = ['123', '234', '333', '000']
# 字典

# 元组

# 集合

# 查看数据类型
a = 34
b = 'hello'
c = True
d = ['123', '555', '777']
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 输出语句
# `print(*values, sep=' ', end='\n', file=sys.stdout, flush=False)`
# sep 空格作为分隔符
# end 结尾\n换行

print('hello', 'good', sep='+', end='---------')
print('world')

# 输入语句
# 不管用户输入什么变量保存都为字符串
num = input("请输入数字")
print(num)

# 进制 0b 二进制 0o八进制 0x十六进制
a = -23
print(bin(a))

# 进制转换
a = 12
print(bin(a))  # 十转二
print(oct(a))  # 十转八
print(hex(a))  # 十转十六

# 数据类型转换
age = input('输入数字')
new_age = int(age)

x = '1a2c'
y = int(x, 16)  # 把字符串当作十六进制转换为整数
print(y)

# 数字0，[],(),{}空字典，空集合,None和空字符串（‘’/“”）在转换为布尔值是False，其他为True
# s=set() 空集合

print(6/2)   # 结果3.0，浮点数
# 10 // 3 整除3，取整数部分 10 % 3 取余数
print('hello' * 2)  # hellohello

x, *y, z = 1, 2, 3, 4, 5  # *y表示变量为可变长度
print(x, y, z)

import random
com = random.randint(0, 5)
print(com)

score = 45
if 60 > score >= 0:
    print('good')










