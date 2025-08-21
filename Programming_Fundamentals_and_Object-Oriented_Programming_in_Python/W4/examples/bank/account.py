class Account:
    def __init__(self, balance=0):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print("-E- You are asking for more than what you have")

    def get_balance(self):
        return self.__balance

