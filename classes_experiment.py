class Vehicle: 

    def __init__(self, name, speed): 
        self.name = name
        self.speed = speed
    
    def get_name(self):
        print(self.name)
    
    def get_speed(self):
        print(self.speed)

class Plane(Vehicle):

    def fly(self):
        print ("I'm Flying")

class Car(Vehicle): 

    def drive(self):
        print ("I'm driving")

ba747 = Plane("747", 800)
ba747.fly()
ba747.get_name()
ba747.get_speed()

ford_fiesta = Car("Ford Fiesta", 80)
ford_fiesta.drive()
ford_fiesta.get_name()
ford_fiesta.get_speed()
