# Elevators!


class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        self.waiting = [False] * floors


class Elevator:
    def __init__(self, name, capacity, building):
        self.name = name
        self.capacity = capacity
        self.building = building
        self.floor = 0
        self.load = 0
        self.alert = False
        self.waiting = [False] * building.floors
        print("Elevator " + self.name + " created with capacity " + str(self.capacity))

    def __str__(self):
        return f'Elevator {self.name} with load {self.load}/{self.capacity} on floor {self.floor}'

    def push_button(self, person, origin, destination):
        self.alert = True
        self.waiting[origin] = True


class Person:
    def __init__(self, name):
        self.name = name
        self.floor = 0

    def move(self, elevator, destination):
        elevator.push_button(person=self, origin=self.floor, destination=destination)


office = Building(name="office", floors=7)
e1 = Elevator(building=office, name="e1", capacity=3)
sal = Person(name="Sal")
sal.move(elevator=e1, destination=1)
