class Account:

    def __init__(self, title=None, balance=0):
        self.title=title
        self.balance=balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate=interestRate


obj1=SavingsAccount("Krishna", 5000, 5)
print(obj1.title)
print(obj1.balance)
print(obj1.interestRate)
