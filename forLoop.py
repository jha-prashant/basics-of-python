'''str = "prashant"
for char in str:
    print(char)
    if(char=="h"):
        print("char found")
        break
else:
    print("end")
    
    
number=[1,4,9,16,25,36,49,64,81,49,25]
idx=0
x=49
for el in number:
    if(x==49):
        print("number found in idx",idx)
    idx+=1
else:
    print("end") 
    
for el in range(4,10,):
    print(el)
    
for el in range(1,100+1):
    print(el)'''
    
for el in range(100,0,-1): 
    print(el) 
    
#print the multiplication table of n number:
n=int(input("enter number"))
for el in range(1,11):
    print(el*n)