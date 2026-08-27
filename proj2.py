
class Account:
    def __init__ (self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        print(f"The Owner name is {self.owner}")
    def deposit(self,amount):
        
        self.balance+=amount
        print(f"You deposited {amount} rupees sucessfully!")
    
    def withdraw(self,amount):
        
        if amount<=self.balance:
            self.balance-=amount
            print(f"You have withdrawn {amount}")
        else:
             print(f"Please request for smaller amount!! your current balance is {self.balance}")

acc1=Account('Subhan',100000)
acc1.deposit(5000)
acc1.withdraw(151000)
        
        
