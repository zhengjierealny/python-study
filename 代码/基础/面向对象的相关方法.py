class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    pass


p1 = Person('xx', 12)
p2 = Person('qq', 13)

s = Student('pit', 20)
print(p1 is p2)  # 比较是否是同一个对象

# type(p1) 获取类对象
print(type(s) == Student)
print(type(s) == Person)

# isinstance 判断对象是否由指定类(父类)实例化出来
print(isinstance(s, Student))
print(isinstance(s, Person))

# issubclass 用于判断一个类是否是类一个类的子类
print(issubclass(Student, Person))