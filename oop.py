class Car:

    def __init__(self):
        self.cmc = 0
        self.doors = 4
        self.tank_capacity = 0
        self.passangers = []

class Person:
    def __init__(self):
        self.height = 0
        self.weight = 0


vlad = Person()

vw = Car()
ford = Car()

print(f'capacitate cilindrica: {vw.cmc}')
print(f'Nr usi la ford: {ford.doors}')
