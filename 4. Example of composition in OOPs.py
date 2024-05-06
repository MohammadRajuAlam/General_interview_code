class Engine:
    def __init__(self, capacity):
        self.capacity=capacity

    def get_engine(self):
        print(f"{self.capacity} cc Capacity of Engine")

class Tyres:
    def __init__(self, tyres):
        self.tyres=tyres

    def get_tyres(self):
        print(f"{self.tyres} tyres")

class Doors:
    def __init__(self, doors):
        self.doors=doors

    def get_doors(self):
        print(f"{self.doors} doors")

class Car:
    def __init__(self, color, capacity, tyres, doors):
        self.capacity=Engine(capacity)
        self.tyres=Tyres(tyres)
        self.doors=Doors(doors)
        self.color=color

    def get_car(self):
        self.capacity.get_engine()
        self.tyres.get_tyres()
        self.doors.get_doors()
        print(f"{self.color}")

obj=Car("Blue",1000, 8, 2)
obj.get_car()
del obj

obj.get_car()


        
