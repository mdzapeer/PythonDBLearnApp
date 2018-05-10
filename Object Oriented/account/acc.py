class Account:
"""This is a class for an Account"""
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance - amount

    def deposit(self,amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account)
"""This is a inherhited class object from Account, for creating checking account class"""
    def __init__(self,Account,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance-amount-fee





#account=Account("balance.txt")
#print(account.balance)
#account.deposit(500)
#print(account.balance)
#account.commit()
