class Student(object):
    # 类属性
    type = '学生'

    # 定义特征--属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # __表示私有变量

    def get_money(self):
        return self.__money

    # __以两个下划线开始的函数为私有函数，外部无法调用
    def __demo(self):
        print('私有函数，name={}'.format(self.name))

    def test(self):
        self.__demo()

    def run(self):
        print('running')

    def eat(self):
        print('eating')


p = Student('aa', 18)

p2 = Student('xx', 20)

print(Student.type)
print(p.type)
# 类属性只能通过类对象修改，实例对象只是新增属性】
Student.type = 'monkey'

# 获取私有变量
print(p._Student__money)
print(p.get_money())

p._Student__demo()