class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining Balance: {self.balance}")
        else:
            print("Insufficient funds!")

# Example usage
acc1 = BankAccount("Madhu", 500)
acc1.deposit(200)
acc1.withdraw(300)
acc1.withdraw(500)
