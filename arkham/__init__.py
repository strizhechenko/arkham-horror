#!/usr/bin/env python
from arkham import Place, Street
from arkham.boss import Boss
from arkham.map import Gate, Place, Street, Location
from arkham.monsters import Monsters, Monster
from arkham.persons import People

people = People()
people.choose_first()
boss = Boss()
AMBULANCE = Place()

while people.alive() or not boss.is_awake():
    person = people.next()
    person.rest()
    person.move(Place())
    if person.place.has_monster():
        person.fight(Monster())
    if person.health < 0:
        person.heal()
        continue
    if isinstance(person.place, Location):
        person.place.contact()
    if person.place.get_gate():
        gate = person.place.get_gate()
        person.move(gate)
        if person.evidences > 5:
            person.close(gate)
    person.myth()
