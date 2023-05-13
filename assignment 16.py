class Account:

    def __init__(self, title=None,balance=0):
        self.title=title
        self.balance=balance
        
    def withdrawal(self, amount):
        self.balance=self.balance-amount

    def deposit(self, amount):
        self.balance=self.balance+amount
        
    def getBalance(self):
        return self.balance
    

class SavingsAccount(Account):
    
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance*self.interestRate/100)

#code to test - do not edit this

demo1 = SavingsAccount("Ashish", 2000, 5)

print(demo1.title, demo1.balance, demo1.interestRate, sep=" ")

demo1.deposit(int(input("enter the deposit amount :")))

demo1.withdrawal(int(input("enter the withdrawl amount :")))

print("your balance",demo1.getBalance())

print("interest:",demo1.interestAmount())
