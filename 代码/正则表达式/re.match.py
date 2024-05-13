import re

# . 任意字符 * 出现任意次数 贪婪模式
m = re.search(r'm.*a', 'd0fsiifmr4afsad')

print(m.span())
print(m.group())
print(m.group(0))

# group方法表示正则表达式分组
# 在正则表达式里使用（）表示一个分组
# 如果没有分组，默认只有一组
# 分组下标从0开始

# 有4个分组
m1 = re.search(r'(9.*)(0.*)(5.*7)', 'dcn9vsu0f5nabeqncnz7kczfefiwu')
print(m1.group(0))
print(m1.group(1))
print(m1.group(2))
print(m1.group(3))

# (?P<name>表达式  可以给分组取名字
m2 = re.search(r'(9.*)(?P<xxx>0.*)(5.*7)', 'dcn9vsu0f5nabeqncnz7kczfefiwu')
# 获取1分组组成的字典
print(m2.groupdict())