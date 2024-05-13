class PoliceDog(object):
    def attack_enemy(self):
        print('警犬工作')


class BlindDog(object):
    def lead_road(self):
        print('导盲犬正在工作')


class Person(object):
    def __init__(self, name):
        self.name = name


    def work_with_pd(self):
        self.dog.attack_enemy()

    def work_with_bd(self):
        self.dog.attack_enemy()


# pd = PoliceDog()
# police = Person('郑警官', pd)
# police.work_with_pd()
p = Person('郑警官')
bd = BlindDog()
p.work_with_bd()
