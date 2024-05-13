class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Dog(Animal):
    def bark(self):
        print(self.name + '正在叫')


class Student(Animal):
    def study(self):
        print(self.name + '学习')


class Monkey(Dog, Student):
    def eat(self):
        print(self.name + '吃香蕉')


d1 = Dog('大黄', 2)
print(d1.name)
d1.sleep()

d2 = Monkey('xx', 3)
d2.study()
