class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
        
    def setEmpid(self,empid):
        self.empid=empid
        
    def setname(self,name):
        self.name=name
        
    def setsalary(self,salary):
        self.salary=salary
        
    def getEmpid(self):
        return self.empid
    def getname(self):
        return self. name
    def getsalary(self):
        return self.salary
    
e1= Employee()
e2= Employee(1,"prashant" ,500)
e1.setEmpid(2)
e1.setname("ruhi")
e1.setsalary (5000)
    
print(e1.getEmpid(),e1.getname(),e1.getsalary())
print(e2.getEmpid(),e2.getname(),e2.getsalary())
        
        
        
        