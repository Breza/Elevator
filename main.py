# Elevators!
import random

print(random.choices(['a', 'b'], k=2))


class Elevator:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        print("Elevator " + self.name + " created with capacity " + str(self.capacity))

    def __str__(self):
        return f'Elevator {self.name} with capacity {self.capacity}'


e1 = Elevator(name="e1", capacity=3)

print(e1)
