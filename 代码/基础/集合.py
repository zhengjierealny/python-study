#  集合是一个不重复的无序 如果有重复的数据，自动去除，每次输出顺序会变
person = {'name': 'zhengjie', 'age': 18, 'height': 170, 'weight': 65}
x = {'hello', 1, 'good'}  # 集合

x.add('kk')  # 添加
x.clear()  # 清空
# 空集合 set()
x.pop()  # 随机删除
x.remove('good')  # 删除指定

x.update(['xx', 'vv'])  # 将B拼到A  union 将多个集合合并成一个

import json
m = json.dumps(person)  # dumps将字典，列表，集合，元组等转换成json字符串
print(m)
s = json.loads(m)  # 将json字符串转成字典






























