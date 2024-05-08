#Recursive function
def show(n):
    if n==0:     #base case:
        return
    print(n)
    show(n-1)
    
show(5)

#factorial:
def fact(n):
    if (n==1):
        return 1
    else:
        return n* fact(n-1) 
    
print (fact(4))

#print sum of n  natural number
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n
    
sum=cal_sum(5)
print(sum)

def print_list(list, idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
fruits=["apple","banana","orange","litchi"]
print_list(fruits)
    
