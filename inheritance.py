class Car:
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stop")
        
class Toyotacar(Car):
    def __init__(self,name,color="black"):
        self.name=name
        self.color=color
        
car1=Toyotacar("fortuner")
car2=Toyotacar("prious")

print(car1.name)
print(car1.start)
print(car1.color)
    
        