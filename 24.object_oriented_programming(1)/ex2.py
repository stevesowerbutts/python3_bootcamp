# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance

b = BankAccount("dave")
print(b.owner, b.balance, b.deposit(10), b.withdraw(5))
