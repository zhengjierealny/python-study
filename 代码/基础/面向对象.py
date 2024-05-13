class Student(object):
    # 这个属性直接定义在类里，规定对象可以存放的属性，是一个元组,不能从外部添加
    # __slots__ = ('name', 'age', 'height', 'weight')

    # 定义特征--属性
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # def run(self):
    #     print('running')
    #
    # def eat(self):
    #     print('eating')
    def __setitem__(self, key, value):
        p.__dict__[key] = value


s1 = Student('qq', 18, 180)
s2 = Student('zz', 19, 170)

# s1.run()
# print(s1.name)
#
# # 通过外部添加属性，前提该属性可以添加
# s1.weight = 78
# print(s1.weight)

p = Student('aa', 18, 176)
print(p.__dict__)  # 将对象转换成字典


p['name'] = 'jack'
print(p.name)
