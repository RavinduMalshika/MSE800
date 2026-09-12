class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def display_account_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance}")

    def deposit_money(self, amount):
        self.balance = self.balance + amount
        print(f"\nNew account balance is {self.balance}")

    def withdraw_money(self, amount):
        self.balance = self.balance - amount
        print(f"\nNew account balance is {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance, interest_rate):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        return interest

def main():
    account = SavingsAccount("SA1001", "John", 5000, 5)

    while True:
        print("\n\n\t\tBank System")
        print("*" * 40)

        print("1. Withdraw Money")
        print("2. Deposit Money")
        print("3. View Account Details")
        print("4. Calculate Interest")
        print("5. Exit")

        user_choice = input("Please select option:")

        if (user_choice == '1'):
            amount = input("Enter amount to withdraw:")
            account.withdraw_money(float(amount))
        elif (user_choice == '2'):
            amount = input("Enter amount to withdraw:")
            account.deposit_money(float(amount))
        elif (user_choice == '3'):
            account.display_account_details()
        elif (user_choice == '4'):
            print(f"\nYour interest rate is {account.interest_rate}")
            interest = account.calculate_interest()
            print(f"Interest calculated: {interest}")
        elif (user_choice == '5'):
            print("Thank you for using the Bank System")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
