# Elevators!
import time


class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        self.waiting = [False] * floors
        self.elevator_list = []


class Elevator:
    def __init__(self, name, capacity, building):
        self.name = name
        self.capacity = capacity
        self.load = 0
        self.building = building
        self.floor = 0
        self.alert = False
        self.waiting = [0.0] * building.floors
        print("Elevator " + self.name + " created with capacity " + str(self.capacity))

    def __str__(self):
        return f'Elevator {self.name} with load {self.load}/{self.capacity} on floor {self.floor}'

    def push_button(self, person, origin, destination):
        self.alert = True
        # Use timestamp so elevator can prioritize people who have been waiting the longest
        self.waiting[origin] = time.time

    def update(self):
        if self.waiting[self.floor] != 0:
            self.waiting[self.floor] = 0


class Person:
    def __init__(self, name):
        self.name = name
        self.floor = 0

    def move(self, elevator, destination):
        elevator.push_button(person=self, origin=self.floor, destination=destination)
        print(f'{self.name} is waiting for {elevator.name} to move from {self.floor} to {destination}')


office = Building(name="office", floors=7)
e1 = Elevator(building=office, name="e1", capacity=3)
sal = Person(name="Sal")
sal.move(elevator=e1, destination=1.0)
