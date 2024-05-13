a = 'hell0'
b = "good"
c = """hhh"""
d = '''qqqq'''

m = ' xiaoming shuo :"I am xiaoming" '

# 转义字符\
# \n 换行 \t 显示一个制表符 在字符串前面添加r,表示原生字符串
x = 'I\'m xiaoming'
print(x[4])

# 字符串是不可改变的数据类型
# 对于字符串的任何操作都不能改变原来的字符串

# 切片 x[start:end:step]  包含start,不包括end,step:每隔Step-1个取一次且不为0
print(x[1:5])

# len(x) 长度 x.find('m')获取指定字符下表
