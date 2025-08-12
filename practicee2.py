''''#define class
class Bike:
    name= ""
    gear= 0
    #create object of class
bike1= Bike()
    #access attributes and assign new values
bike1.gear= 11
bike1.name="Mountain Bike"
print(f"Name: {bike1.name}, Gears: {bike1.gear}")


class Polygon:
    def render(self):
        print("Rendering Polygon...")
        class Square(Polygon):
            def render(self):
                print("Rendering Square...")
                class Circle(Polygon):
                    def render(self)'''

    
class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling Price:{}".format(self.__maxprice))
    def setMaxPrice(self,price):
        self.__maxprice= price
c= Computer()
c.sell()
c._maxprice=1000
c.sell()
c.setMaxPrice(1000)
c.sell()
                
