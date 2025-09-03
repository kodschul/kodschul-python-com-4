# your class comes here! ....
class BankAccount:

    __balance = 0
    name = None

    def __init__(self, name):
        self.name = name

    def show_balance(self):
        print(f"{self.name}'s current balance is: {self.__balance} €")

    def deposit(self, amount):
        self.__balance += abs(amount)

    def withdraw(self, amount):
        self.__balance -= abs(amount)

    def send_money(self, to_account, amount: float):
        self.withdraw(amount)
        to_account.deposit(amount)


bank = BankAccount("N26")
bank.show_balance()

bank.deposit(1000)
bank.withdraw(200)
bank.__balance = 10e6

# bank._BankAccount__balance = 10000

print(bank.__balance)

bank.show_balance()
