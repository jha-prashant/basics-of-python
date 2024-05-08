class complex_number:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def ShowNumber(self):
        print(self.real,"i +",self.img,"j")
        
num1 = complex_number(1,3)
num1.ShowNumber()

num2 = complex_number(2,5)
num2.ShowNumber()