# 判断是否数字
import re
# x = input('输入')
# t = re.fullmatch(r'\d+(\.?\d+)?', x)
# # if t.group(0) == x:
# #     print('T')
# # else:
# #     print('F')
# print('T' if t.group(0) == x else 'F')

# 用户名 只能数字，字母，下划线，不能数字开头，长度6-16
# r'[a-zA-Z_][0-9a-zA-Z]{5-15}'
# 密码 不能包含!@%^&* 必须字母开头 6-12
# [a-zA-Z][^!@%^&*]{5-11}