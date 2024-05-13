class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Student(Person):
    def __init__(self, name, age, school):
        # self.name = name
        # self.age = age
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.school = school

    def study(self):
        print(self.name + '正在学习')

    def sleep(self):
        print(self.name + '上课睡觉')


s = Student('Jack', 20, '阳光小学')
s.sleep()
s2 = Student('Tom', 12, '希望小学')
