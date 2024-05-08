#create account class with two attributes-balance and ac no
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
        #debit method
    def debit(self,ammount):
        self.balance -= ammount
        print("RS",ammount,"was debited")
        print("total balance",self.get_balance()) 
        
        #credit method
    def credit(self,ammount):
        self.balance += ammount
        print("RS",ammount,"was credited") 
        print("total balance",self.get_balance())  
        
    def get_balance(self):
        return self.balance  
    
        
acc1=Account(1000, 112233)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(100)
acc1.credit(300)