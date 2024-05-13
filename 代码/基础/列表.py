name = ['1', '2', '3', '4 ', '5', '6', '7']
print(name[3])
name.append('99')  # 添加
name.index(3, '66')

x = ['33', '44', '55']
name.extend(x)  # 拼接

z = name.pop()  # 删除最后一个数据，并返回这个数据 pop(3)删除指定位置
name.remove('6')

# del z 删除整个z 拆房子
# 查询 name.index('2)  name.count('2')  '4' in name 判断是否在列表中

# 修改
name[3] = '88'

# 排序
nums = [6, 4, 3, 7, 8, 9, 0]
nums.sort()  # 小到大 nums.sort(reverse=True) 倒序
# sorted,不会改变原有列表，重新生成一个列表
x = sorted(nums)
# nums.reverse()翻转列表

# 数字，字符串，元组不能改变值，列表，字典，数组可以
a = 12
b = a
a = 10
print(b)

nums1 = [100, 200, 300]
nums2 = nums1
nums1[0] = 1
print(nums2)

# 列表推导式
nums3 = [i for i in range(10)]
print(nums)

nums4 = [i for i in range(10) if i % 2]

# sorted内置函数，不会改变原来的数据，而是生成一个新的有序列表
ints = (5, 6, 8, 3, 1, 9)
intss = sorted(ints)
print(intss)

# 字典排序
person = [
    {'name': 'zhengjie', 'age': 18, 'height': 170, 'weight': 65},
    {'name': 'zhengjie2', 'age': 20, 'height': 160, 'weight': 85},
    {'name': 'zhengjie3', 'age': 23, 'height': 180, 'weight': 64},
    {'name': 'zhengjie4', 'age': 17, 'height': 190, 'weight': 75},
    {'name': 'zhengjie5', 'age': 20, 'height': 167, 'weight': 67}
]


def foo(ele):
    return ele['age']


person.sort(key=foo)
print(person)

person.sort(key=lambda ele: ele['height'])
print(person)
