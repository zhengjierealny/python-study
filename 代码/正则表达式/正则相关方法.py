# 查找
# match 和 search:
# 共同点 只对字符串查找一次 返回值类型都是re.Match类型
# 不同点 match 从头开始匹配，一旦匹配失败返回none；
#       search是在整个字符串里匹配
# finditer: 找到所有匹配数据放到一个可迭代对象里
# findall: 把所有字符串结果放到一个列表里
# fullmatch: 完整匹配，字符串需要完全满足正则规则，否则none

import re
from collections.abc import Iterable

m1 = re.match(r'hello', 'hello wojmc niaf wuadi')
print(m1)  # <re.Match object; span=(0, 5), match='hello'>

m3 = re.match(r'good', 'hello wojmc niaf wuadi')
print(m3)  # None

m2 = re.search(r'hello', 'hello wojmc niaf wuadi')
print(m2)  # <re.Match object; span=(0, 5), match='hello'>

# finditer 返回一个可迭代对象 是一个re.match对象
m4 = re.finditer(r'x', 'xjkxjckjzkjcnkzkkdefq')
print(isinstance(m4, Iterable))
for t in m4:
    print(t)

m5 = re.findall(r'x\d+', 'fix423cnax3ci546adx4dffx')
print(m5)

m6 = re.fullmatch(r'hello word', 'hello word')
print(m6)
m7 = re.fullmatch(r'h.*d', 'hello world sdsd')
print(m7)