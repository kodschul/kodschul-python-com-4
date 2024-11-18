# your class comes here! ....
class BankAccount:

    balance = 0
    name = None

    def __init__(self, name):
        self.name = name

    def show_balance(self):
        print(f"{self.name}'s current balance is: {self.balance} €")

    def deposit(self, amount):
        self.balance += abs(amount)

    def withdraw(self, amount):
        self.balance -= abs(amount)

    def send_money(self, to_account, amount: float):
        self.withdraw(amount)
        to_account.deposit(amount)
