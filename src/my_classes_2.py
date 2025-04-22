class BankAccount:
    def __init__(self, owner, account_nunber, balance=0.0):
        self.owner = owner
        self.account_number = account_nunber
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount 
        print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account({self.account_number}) - Owner: {self.owner}, Balance: ${self.balance:.2f}"

if __name__ == "__main__":  

    account = BankAccount('John', '1234')

    account.deposit(400)
    account.withdraw(100)

    print(account)