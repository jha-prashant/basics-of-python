a = int(input("enter the value of a :"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:")) 
 
if(a>=b and b>=c):
    print("a is largest",a)
elif (b>c):
    print("b is largest",b)
else:
    print("c is largest",c)