from bank import BankAccount


alice_account = BankAccount("Alice")
bob_account = BankAccount("Bob")

alice_account.show_balance()
bob_account.show_balance()

alice_account.deposit(1000)

alice_account.show_balance()
bob_account.show_balance()

alice_account.send_money(bob_account, 200)

alice_account.show_balance()
bob_account.show_balance()


bob_account.send_money(alice_account, 50)

alice_account.show_balance()
bob_account.show_balance()


bob_account.send_money(bob_account, 50)

alice_account.show_balance()
bob_account.show_balance()
