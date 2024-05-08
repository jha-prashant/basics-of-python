'''create student class that takes name and marks of 3 sub as argument in construter
then create a method to print the avg'''

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(self.name,"your avg marks is",sum/3)
        
        
s1=Student("sunny",[98,97,93])
s1.get_avg()
