#define function
def cal(a,b):  #parameter
    sum=a+b
    print(sum)
    return sum

#call function
cal(10,5)  #argument
#more number of code

cal(100,50)

#waf to take input from user, if input is even than print "EVEN", other wise print "ODD":
num=int(input("enter the number"))
def usr_input(num):
    if num%2==0:
        print("EVEN")
    else:
        print("ODD")
    return num
usr_input(num)
        
