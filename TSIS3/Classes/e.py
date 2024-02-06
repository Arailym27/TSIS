class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        print(self.balance)

    def deposit(self,amn_contr):
        if amn_contr>0:
            self.balance+=amn_contr
            print(f"Current balance {self.balance}")
        else:
            print("Invalid operation")

    def withdraw(self,amn_take):
        if amn_take>0:
            if self.balance>=amn_take:
                self.balance-=amn_take
                print(f"Current balance {self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid operation")

owner=input()
balance=float(input())
account=Account(owner,balance)

deposit_amount = float(input())
account.deposit(deposit_amount)

withdraw_amount = float(input())
account.withdraw(withdraw_amount)