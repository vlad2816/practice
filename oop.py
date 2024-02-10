class Car:

    def __init__(self):
        self.__cmc = 0
        self.__doors = 4
        self.__tank_capacity = 0
        self.__passengers = []

    def get_doors(self):
        return self.__doors
    
    def get_cmc(self):
        return self.__cmc

class Person:
    def __init__(self):
        self.height = 0
        self.weight = 0


vlad = Person()

vw = Car()
ford = Car()
print(vw.get_doors())
