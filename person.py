class Person:
    def __init__(self ,name =None,age=None):
        self.name=name
        self.age=age
        
    def setname (self,name):
        self.name=name 
        
    def setage (self,age):
        self.age=age
        
    def getname(self):
        return self.name
    
    def getage(self):  
        return self.age
    
p1=Person()
p1.setname("prashant")
p1.setage(23)
p2=Person()
p2.setname("sunny")
p2.setage(24)
print(p1.getname(),p1.getage())
print(p2.getname(),p2.getage() )        