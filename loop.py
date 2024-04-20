#print number 1 to 100:
'''i=1
while i<=100:
    print(i)
    i+=1
    
#print number 100 to 1:
i=100
while i>=1:
    print(i)
    i-=1
    
#print the multiplication table of n:
n=int(input("enter the value of n"))
i=1
while i<=10:
    print(n*i)
    i+=1'''
    
#print list elements using loop:
'''nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(nums):
    print(nums[idx])
    idx+=1'''
    
nums=(1,4,9,16,25,36,49,64,81,100)
i = 0
x=36
while i< len(nums):
    if (nums[i]==x):
        print("found at idx",i)
        break
    else:
        print("finding",i)
    print (nums[i])
    i += 1
    
    