from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class BankATM(ATM):
    def insert_card(self):
        while True:
            is_card_inserted = input("Please enter the card. Press 'y' when inserted: ")

            if (is_card_inserted.lower() == 'y'):
                break


    def enter_pin(self):
        while True:
            pin = input("Enter Pin: ")

            if (pin == "1234"):
                break
            else:
                print("\nInvalid Pin")
        

    def check_balance(self):
        print("Account balance is 1000")

    def withdraw(self, amount):
        print(f"{amount} is withdrawn")

def main():
    atm = BankATM();

    atm.insert_card()
    atm.enter_pin()
    atm.check_balance()

    amount = input ("\nEnter amount to withdraw: ")
    atm.withdraw(amount)

if __name__ == "__main__":
    main()
