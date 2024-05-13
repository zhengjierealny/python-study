class Dog(object):
    def work(self):
        print('dog work')


class PoliceDog(Dog):
    def work(self):
        print('警犬工作')


class BlindDog(Dog):
    def work(self):
        print('导盲犬正在工作')


class DrugDog(Dog):
    def work(self):
        print('缉毒犬正在工作')


class Person(object):
    def __init__(self, name):
        self.name = name

    def work_with_dog(self):
        self.dog.work()


p = Person('郑警官')

bd = BlindDog()
p.dog = bd
p.work_with_dog()

pd = PoliceDog()
p.dog = pd
p.work_with_dog()

dd = DrugDog()
p.dog = dd
p.work_with_dog()
