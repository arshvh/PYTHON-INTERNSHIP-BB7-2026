class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Invalid withdrawal amount.")

w = Wallet(5000)

print("Current Balance:", w.balance)

w.deposit(2000)
print("Balance:", w.balance)

w.withdraw(1000)
print("Final Balance:", w.balance)