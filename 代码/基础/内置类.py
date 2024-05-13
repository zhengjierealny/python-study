from functools import reduce

# filter 对可迭代对象进行过滤，得到一个filter对象

ages = [12, 23, 45, 13, 56, 34, 21]
# filter 可以给定两个参数，函数 可迭代对象
# filter结果也是filter对象，filter也是一个可迭代对象
x = filter(lambda ele: ele > 18, ages)
for a in x:
    print(a)

m = map(lambda ele: ele + 2, ages)
print(list(m))

print(reduce(lambda ele1, ele2: ele1 + ele2, ages))  # 求和

person = [
    {'name': 'zhengjie', 'age': 18, 'height': 170, 'weight': 65},
    {'name': 'zhengjie2', 'age': 20, 'height': 160, 'weight': 85},
    {'name': 'zhengjie3', 'age': 23, 'height': 180, 'weight': 64},
    {'name': 'zhengjie4', 'age': 17, 'height': 190, 'weight': 75},
    {'name': 'zhengjie5', 'age': 20, 'height': 167, 'weight': 67}
]
print(reduce(lambda g, y: g + y['age'], person, 0))  # 0表示初始化g的值

nums = [1, 2, 3]
print(dir(nums))  # 列出所有可用的方法
