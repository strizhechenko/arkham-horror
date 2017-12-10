class Gate(object):
    def open(self, place):
        if place.get_gate():
            self.horde()

    def horde(self):
        pass


class Place(object):
    def has_monster(self):
        return True

    def get_gate(self):
        return Gate()


class Street(Place):
    def __init__(self, locations):
        self.locations = locations


class Location(Place):
    def contact(self):
        pass


class Map(Place):
    OLD_SORCERY_STORE = Place()
    FORESTS = Place()
    SAINT_MARY_AMBULANCE = Place()
    UPTOWN = Street([SAINT_MARY_AMBULANCE, FORESTS, SAINT_MARY_AMBULANCE])

    HISTORIC_SOCIETY = Place()
    SOUTH_CHURCH = Place()
    MOMMY_PANSION = Place()
    SOUTHSIDE = Street([SOUTH_CHURCH, MOMMY_PANSION, HISTORIC_SOCIETY])


class Activity(object):
    def __init__(self, place):
        pass
