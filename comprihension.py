#generate 20 random number in the range 10 to 100;
import random
a= [random.randint(10,100)for n in range(20)] 
print(a)

#generate sqare and cube of all number betwen 10 or 100;
x=int(input("enter the value of x"))
a=[(x,x**2,x**3)for n in range(10)]
print(a)

#product [4,5,6,5,6,7,6,7,8],use nusted for
lst=[a+b+c for a in range[1,2,3]for b in [3,4,5] for c in [5,6,7]]
print(lst)