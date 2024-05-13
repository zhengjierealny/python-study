# 列表
words = ['f', 't', 'y', 'b', 'n', 'z', 111, 222, 333, 444]

# 字典 {key:value,key2:value2} key是不可变数据类型
person = {'name': 'zhengjie', 'age': 18, 'height': 170, 'weight': 65}

# 增删改查
print(person['name'])
print(person.get('shool'))  # 获取不存在key时，返回默认值None
print(person.get('class', '4-7'))  # 获取不存在key时,使用给定值'4-7'

# key存在，修改值，不存在，添加key
person['name'] = 'zj'
person['sex'] = '男'

person.pop('age')  # 删除'age':18
print(person)
person.popitem()

# update 两个合成一个
nums1 = [1, 2, 4, 5, 6, 7]
nums2 = [8, 9, 0]
nums1.extend(nums2)

person2 = {'name': 'zhengjie', 'age': 18}
person3 = {'height': 170, 'weight': 65}
person2.update(person3)

words2 = ('je', 'ed')
words3 = ('cv', 'as')
print(words2+words3)

# 遍历
person4 = {'name': 'zhengjie', 'age': 18, 'height': 170, 'weight': 65}
for x in person4:
    print(x, '=', person4[x])

# 字典推导式
person5 = {v: k for k, v in person4.items()}




















