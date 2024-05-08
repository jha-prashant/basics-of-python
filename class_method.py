class Person:
    name="anonymous"
    
    @classmethod
    
    def changename(cls,name):
        cls.name=name
    
p1= Person()
p1.changename("prashant")
print(p1.name)
print(Person.name)


    