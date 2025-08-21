from account import Account


class Main:
    def get_user_choice(self):
        print("Welcome to our bank:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Get Balance")
        print("4. Exit")
        ch = int(input("Enter your choice: "))
        return ch

    def run(self):
        account = Account()
        ch = self.get_user_choice()
        while ch != 4:
            if ch == 1:
                amount = int(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif ch == 2:
                amount = int(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif ch == 3:
                print(f"You balalnce is: {account.get_balance()}")
            ch = self.get_user_choice()


if __name__ == "__main__":
    main = Main()
    main.run()



