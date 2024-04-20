n =int(input("entyer the value of n"))

c=0

    for i in range (1,n):
        if(n%i)==0:
            c=c+1
            #print("not prime number")
            break
if (c==0):
     print(n,"number is not prime number")
else:
     print(n,"number a prime")