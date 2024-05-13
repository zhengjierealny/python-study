class Student(object):
    type = '学生'

    # 定义特征--属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name + '吃' + food)

    @staticmethod  # 静态方法
    def demo():
        print('hello')

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod  # 类方法
    def test(cls):
        print(cls.type)
        print('yes')


p = Student('aa', 18)

p2 = Student('xx', 20)

p.eat('包子')

Student.eat(p2, '烤串')

Student.demo()
p2.demo()
print(Student.add(1, 6))
p.test()
Student.test()
