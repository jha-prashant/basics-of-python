#WAF to print the length of a list
name=["prashant","sunny","aditya","chanchal"]
def list_type():
    print(len(name))
    return name

list_type()

#WAF to print the elements of a list in a single line (use parameter):
def print_list(list):
    for item in name:
        print(item,end=" ")
    
print_list(name)

#WAP a function to find the factorial of n:
def fact_cal(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    return fact
fact_cal(7) 

def convertor(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=", inr_val,"INR")
    
convertor(1)