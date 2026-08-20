from database import Database
from models import CurrencyManager, CustomerManager, ExchangeService
from tabulate import tabulate

class MoneyExchange:
    def __init__(self):
        self.db = Database()
        self.curr_mgr = CurrencyManager(self.db)
        self.cust_mgr = CustomerManager(self.db)
        self.exchange_svc = ExchangeService(self.db, self.curr_mgr)

    def run(self):
        while True:
            print("\n--- MAIN MENU ---")
            print("1. Customer Management")
            print("2. Currency Management")
            print("3. Transaction Management")
            print("4. Perform Exchange")
            print("5. Exit")
            
            choice = input("Select an option: ").strip()

            if choice == '1':
                self.customer_menu()
            elif choice == '2':
                self.currency_menu()
            elif choice == '3':
                self.transaction_menu()
            elif choice == '4':
                self.perform_exchange()
            elif choice == '5':
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    # --- CUSTOMER MANAGEMENT MENU ---
    def customer_menu(self):
        while True:
            print("\n--- CUSTOMER MANAGEMENT ---")
            print("1. Add Customer")
            print("2. View All Customers")
            print("3. Get Customer by ID")
            print("4. Get Customer by Email")
            print("5. Update Customer")
            print("6. Delete Customer")
            print("7. Back to Main Menu")

            choice = input("Select an option: ").strip()
            headers = ["Customer ID", "Name", "Email"]

            if choice == '1':
                name = input("Customer Name: ").strip()
                email = input("Customer Email: ").strip()
                try:
                    cid = self.cust_mgr.add_customer(name, email)
                    print(f"Customer created with ID: {cid}")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '2':
                customers = self.cust_mgr.get_all_customers()
                if not customers:
                    print("No customers found.")
                else:
                    print("\n--- ALL CUSTOMERS ---")
                    print(tabulate(customers, headers=headers, tablefmt="grid"))

            elif choice == '3':
                try:
                    cid = int(input("Customer ID: "))
                    customer = self.cust_mgr.get_customer_by_id(cid)
                    if customer:
                        print(tabulate([customer], headers=headers, tablefmt="grid"))
                    else:
                        print("Customer not found.")
                except ValueError:
                    print("Please enter a valid numeric ID.")

            elif choice == '4':
                email = input("Enter email: ").strip()
                customer = self.cust_mgr.get_customer_by_email(email)
                if customer:
                    print(tabulate([customer], headers=headers, tablefmt="grid"))
                else:
                    print("Customer not found.")

            elif choice == '5':
                try:
                    cid = int(input("Customer ID to update: "))
                    new_name = input("New Name (press enter to keep current): ").strip() or None
                    new_email = input("New Email (press enter to keep current): ").strip() or None
                    
                    self.cust_mgr.update_customer(cid, name=new_name, email=new_email)
                    print("Customer updated successfully.")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '6':
                try:
                    cid = int(input("Customer ID to delete: "))
                    if self.cust_mgr.delete_customer(cid):
                        print("Customer deleted successfully.")
                    else:
                        print("Customer ID not found.")
                except ValueError:
                    print("Please enter a valid numeric ID.")

            elif choice == '7':
                break
            else:
                print("Invalid option. Please try again.")

    # --- CURRENCY MANAGEMENT MENU ---
    def currency_menu(self):
        while True:
            print("\n--- CURRENCY MANAGEMENT ---")
            print("1. Add/Update Currency & Exchange Rates")
            print("2. Check Exchange Rate")
            print("3. Back to Main Menu")

            choice = input("Select an option: ").strip()

            if choice == '1':
                from_c = input("From Currency Code (e.g., USD): ").strip()
                to_c = input("To Currency Code (e.g., EUR): ").strip()
                try:
                    rate = float(input("Exchange Rate: "))
                    self.curr_mgr.add_currency(from_c, from_c)
                    self.curr_mgr.add_currency(to_c, to_c)
                    self.curr_mgr.set_rate(from_c, to_c, rate)
                    print("Rate updated successfully.")
                except ValueError:
                    print("Invalid exchange rate value.")

            elif choice == '2':
                from_c = input("From Currency Code: ").strip()
                to_c = input("To Currency Code: ").strip()
                rate = self.curr_mgr.get_rate(from_c, to_c)
                if rate:
                    print(f"Current Rate ({from_c.upper()} -> {to_c.upper()}): {rate}")
                else:
                    print("No rate found for this currency pair.")

            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")

    # --- TRANSACTION MANAGEMENT MENU ---
    def transaction_menu(self):
        headers = ["Transaction ID", "Customer", "From", "To", "Given", "Received", "Timestamp"]
        
        while True:
            print("\n--- TRANSACTION MANAGEMENT ---")
            print("1. View All Transactions")
            print("2. View Transactions by Customer ID")
            print("3. View Transactions by Customer Email")
            print("4. Back to Main Menu")

            choice = input("Select an option: ").strip()

            if choice == '1':
                transactions = self.exchange_svc.get_all_transactions()
                if transactions:
                    print(tabulate(transactions, headers=headers, tablefmt="grid"))
                else:
                    print("No transactions found.")

            elif choice == '2':
                try:
                    cid = int(input("Enter Customer ID: "))
                    transactions = self.exchange_svc.get_transactions_by_customer_id(cid)
                    if transactions:
                        print(tabulate(transactions, headers=headers, tablefmt="grid"))
                    else:
                        print(f"No transactions found for Customer ID: {cid}")
                except ValueError:
                    print("Please enter a valid numeric Customer ID.")

            elif choice == '3':
                email = input("Enter Customer Email: ").strip()
                transactions = self.exchange_svc.get_transactions_by_customer_email(email)
                if transactions:
                    print(tabulate(transactions, headers=headers, tablefmt="grid"))
                else:
                    print(f"No transactions found for email: {email}")

            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")

    # --- EXCHANGE OPERATION ---
    def perform_exchange(self):
        print("\n--- EXECUTE TRANSACTION ---")
        try:
            cid = int(input("Customer ID: "))
            from_c = input("From Currency: ").strip()
            to_c = input("To Currency: ").strip()
            amt = float(input("Amount to exchange: "))

            received = self.exchange_svc.execute_trade(cid, from_c, to_c, amt)
            print(f"\nTrade complete! Received: {received:.2f} {to_c.upper()}")
        except Exception as e:
            print(f"Error executing trade: {e}")


if __name__ == "__main__":
    MoneyExchange().run()
