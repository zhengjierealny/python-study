# 统计Student使用次数
class Student(object):
    type = '学生'
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        x = object.__new__(cls)  # 自己申请内存
        return x

    # 定义特征--属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        print(cls.__count)


p = Student('aa', 18)

p2 = Student('xx', 20)

print(p)
print(p2)
print(p.name)
Student.get_count()