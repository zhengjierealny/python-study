class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def demo(self):
        print('姓名是', self.name)

    @classmethod
    def bar(cls):
        print(cls.type)

    @staticmethod
    def foo():
        print(Person.type)


p = Person('zhangsan', 19)
Person.foo()
p.demo()
Person.demo(p)
p.foo()

# 自己类里定义的私有方法  对象名._类名__私有方法名()
# 可以通过 对象名._父类名__私有方法调用()
# 私有属性和方法，子类不会继承
