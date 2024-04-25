#avarage of three numner
def avr(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

avr(10,20,30)

#defoult parameter:
def cals(a=3,b=5):
    multi=a*b
    print(multi)
    return multi

cals(5,5)


#one value assign:
def perp(a,b=5):
    multi=a*b
    print(multi)
    return multi

perp(2)