'''
class Rooms:
    def __init__(self, size=0):
        self.size=size

    def get(self):
        print(f"Siz of Rooms\nsize: {self.size}")

class Door:
    def __init__(self, doors=0):
        self.doors=doors

    def get(self):
        print(f"No of doors: {self.doors}")

class House:
    def __init__(self, color, size=0, doors=0):
        self.color=color
        self.size=Rooms(size)
        self.doors=Door(doors)

    def get(self):
        print(f"Color of house: {self.color}")
        self.size.get()
        self.doors.get()

obj=House('red',"10X12 Feet",2)
obj.get()
'''
# Example of Car. Car composed in types, doors, engine

class Engine:
    def __init__(self, capacity=0):
        self.capacity=capacity

    def get_engine(self):
        print(f"Engine capacity: {self.capacity} CC")

class Tyres:
    def __init__(self, tyres=0):
        self.tyres=tyres

    def get_tyres(self):
        print(f"No of tyres: {self.tyres}")

class Doors:
    def __init__(self, doors=0):
        self.doors=doors

    def get(self):
        print(f"No of doors: {self.doors}")

class Car:
    def __init__(self, color="", capacity=0, tyres=0, doors=0):
        self.color=color
        self.capacity=Engine(capacity)
        self.tyres=Tyres(tyres)
        self.doors=Doors(doors)

    def get(self):
        print(f"Car: {self.color}")
        self.capacity.get_engine()
        self.tyres.get_tyres()
        self.doors.get()

obj=Car("Red",1000,4,4)
obj.get()
