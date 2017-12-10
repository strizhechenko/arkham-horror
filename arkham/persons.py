from arkham import Monsters, Gate, Place, AMBULANCE
from arkham.map import Activity


class People(object):
    def __init__(self):
        pass

    def choose_first(self):
        pass

    def alive(self):
        pass

    def next(self):
        return Person()


class Person(object):
    def __init__(self):
        self.place = None
        self.evidences = 0
        self.health = 0
        self.spells = []
        self.weapons = []

    def rest(self):
        pass

    def move(self, place):
        self.place = place

    def fight(self, monster):
        monster.check_horror(self)
        monster.check_fight(self)

    def rewards(self):
        pass

    def close(self, gate):
        self.rewards()

    def myth(self):
        Monsters().move()
        Gate().open(Place())
        Activity(Place())

    def heal(self):
        self.move(AMBULANCE)

    def read_spell(self):
        pass
