# You should Be use  input like this way:--->
# -->Enter role (user/admin): user or admin
# -->Account Type (savings/surrent): savings or current
# Not other other names
#after every operation of admin you shoud enter the role by typing admin then respectively you can use every operation 

from abc import ABC, abstractmethod

class Account(ABC):
    accounts = []
    total_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True
    
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0
        Account.accounts.append(self)
    

    def generate_account_number(self):
        return len(Account.accounts) + 1000
    

    def deposit(self, amount):
        
        if amount >= 0:
            self.balance += amount
            Account.total_balance += amount
            print(f"\n--> Deposited ${amount}")
            print(f'Available balance: ${self.balance}')
            transaction = f'Deposit: +${amount}, Balance: ${self.balance}'
            self.transaction_history.append(transaction)
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            Account.total_balance -= amount
            print(f"\nWithdrew ${amount}")
            print(f'Available balance: ${self.balance}')
            transaction = f'Withdrawal: -${amount}, Balance: ${self.balance}'
            self.transaction_history.append(transaction)
    
        else :
            print("\n--> Withdrawal amount exceeded. Insufficient balance or invalid amount.")
        
        if Account.total_balance < 0:
            print("\n--> Bank is bankrupt!!!.")  #here admin set negative value for bankrupt


    def check_balance(self):
        print(f'\nAccount Type: {self.account_type}')
        print(f'Name: {self.name}')
        print(f'Account Number: {self.account_number}')
        print(f'Current Balance: ${self.balance}')

    def check_transaction_history(self):
        print(f'\nTransaction History for {self.name}:')
        for t in self.transaction_history:
            print(t)

    def take_loan(self, amount):
        if Account.loan_feature_enabled and self.loan_taken < 2 and amount > 0:
            print(f'\nPlease take a loan: ${amount}')
            print(f'Available balance: ${self.balance}')
            self.balance += amount
            Account.total_balance += amount
            self.loan_taken += 1
            Account.total_loan_amount += amount
        else:
            print('\nUnable to take a loan. Check if the loan feature is enabled or limit reached.')

    @abstractmethod
    def transfer(self, target_account, amount):
        pass

    @abstractmethod
    def show_info(self):
        pass
    

# Savings_Account starts From Here

class SavingsAccount(Account):
    def __init__(self, name, email, address, interest_rate):
        super().__init__(name, email, address, "savings")
        self.interest_rate = interest_rate



    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print("\n--> Interest is applied!")
        self.deposit(interest)

    def transfer(self, target_account, amount):
        if target_account:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                Account.total_balance -= amount
                target_account.deposit(amount)
                t = f'Transfer: -${amount} to {target_account.name}, Your Balance: ${self.balance}'
                self.transaction_history.append(t)
                print("Transfer successful!")
            else:
                print("Invalid transfer amount or insufficient balance.")
        else:
            print("Error: Target account does not exist.")

    def show_info(self):
        print(f"\nInfos of {self.account_type} account of {self.name}:\n")
        print(f'Account Type: {self.account_type}')
        print(f'Name: {self.name}')
        print(f'Account Number: {self.account_number}')
        print(f'Current Balance: ${self.balance}\n')

# Savings_Account End Here


# Current_Account starts From Here

class CurrentAccount(Account):
    def __init__(self, name, email, address, overdraft_limit):
        super().__init__(name, email, address, "current")
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            Account.total_balance -= amount
            print(f'\n--> Withdrew ${amount}')
            print(f'Available balance: ${self.balance}')
            t = f'Withdrawal: ${amount}, Balance: ${self.balance}'
            self.transaction_history.append(t)
        else:
            print("\n--> Withdrawal amount exceeded. Insufficient balance or invalid amount.")

    def transfer(self, target_account, amount):
        if target_account:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                Account.total_balance -= amount
                target_account.deposit(amount)
                t = f'Transfer: ${amount} to {target_account.name}, Your Balance: ${self.balance}'
                self.transaction_history.append(t)
                print("Transfer successful!")
            else:
                print("Invalid transfer amount or insufficient balance.")
        else:
            print("Error: Target account does not exist.")

    def show_info(self):
        print(f"\nInfos of {self.account_type} account of {self.name}:\n")
        print(f'Account Type: {self.account_type}')
        print(f'Name: {self.name}')
        print(f'Account Number: {self.account_number}')
        print(f'Current Balance: ${self.balance}\n')


# Current_Account End Here



# Admin Accounts Starts From Here


class Admin(Account):
    def create_account():
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        address = input("Enter user address: ")
        account_type = input("Enter account type (savings/current): ")

        if account_type == "savings":
            interest_rate = float(input("Enter interest rate: "))
            user_account = SavingsAccount(name, email, address, interest_rate)
        elif account_type == "current":
            overdraft_limit = float(input("Enter overdraft limit: "))
            user_account = CurrentAccount(name, email, address, overdraft_limit)
        else:
            print("Invalid account type. Account not created.")

    def delete_account():
        account_number = int(input("Enter account number to delete: "))
        for account in Account.accounts:
            if account.account_number == account_number:
                Account.total_balance -= account.balance
                Account.total_loan_amount -= account.loan_taken
                Account.accounts.remove(account)
                print("Account deleted successfully.")
                break
        else:
            print("Account not found.")

    def view_all_accounts():
        print("\nList of all user accounts:")
        if Account.accounts:
            for account in Account.accounts:
                print(f"Account Number: {account.account_number}, Name: {account.name}")
        else:
            print("No accounts are available.")

            
    def check_total_balance():
        print(f"\nTotal Available Balance in the bank: ${Account.total_balance}")

    def check_total_loan_amount():
        print(f"\nTotal Loan Amount in the bank: ${Account.total_loan_amount}")

    def enable_disable_loan_feature():
        status = input("Do you want to enable or disable the loan feature? (enable/disable):")
        if status == "enable":
            Account.loan_feature_enabled = True
            print("Loan feature enabled.")
        elif status == "disable":
            Account.loan_feature_enabled = False
            print("Loan feature disabled.")
        else:
            print("Invalid option. Please enter 'enable' or 'disable'.")

# Admin Accounts Starts From Here

# Main program

current_user = None

while True:
    if current_user is None:
        print("\n--> No user logged in!")
        role = input("\n--> Enter role (user/admin): ")

        if role == "user":
            print("\nCreating a new account:")
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            account_type = input("Account Type (savings/current): ")

            if account_type== "savings":

                interest_rate = float(input("Interest rate: "))
                current_user = SavingsAccount(name, email, address, interest_rate)
            elif account_type== "current":
                overdraft_limit = float(input("Overdraft Limit: "))
                current_user = CurrentAccount(name, email, address, overdraft_limit)
            else:
                print("Invalid account type. Account not created.")

        elif role == "admin":
            print("\nAdmin Options:")  
            print('<----------------->' )           
            print("1.Create Account\n")               
            print("2.Delete Account\n")              
            print("3.View All Accounts\n")              
            print("4.Check Total Balance\n")              
            print("5.Check Total Loan Amount\n ")               
            print("6.Enable/Disable Loan Feature\n")                
            print("7. Logout\n ")   

            admin_option=input('Enter Option:')

            if admin_option == "1":
                Admin.create_account()
            elif admin_option == "2":
                Admin.delete_account()
            elif admin_option == "3":
                Admin.view_all_accounts()
            elif admin_option == "4":
                Admin.check_total_balance()
            elif admin_option == "5":
                Admin.check_total_loan_amount()
            elif admin_option == "6":
                Admin.enable_disable_loan_feature()
            elif admin_option == "7":
                current_user = None
            else:
                print("Invalid Admin option.")

    else:
        print(f"\nWelcome {current_user.name}!\n")

        if current_user.account_type=="savings":

            print("1. Withdraw\n2. Deposit\n3. Check Balance\n4. Transaction History\n5. Apply Interest\n"
                  "6. Take Loan\n7. Transfer Amount\n8. Logout\n")

            op = input("Choose Option: ")

            if op == "1":
                amount = float(input("Enter withdrawal amount: "))
                current_user.withdraw(amount)

            elif op == "2":
                amount = float(input("Enter deposit amount: "))
                current_user.deposit(amount)

            elif op == "3":
                current_user.check_balance()

            elif op == "4":
                current_user.check_transaction_history()

            elif op == "5":
                current_user.apply_interest()

            elif op == "6":
                loan_amount = float(input("Enter loan amount: "))
                current_user.take_loan(loan_amount)

            elif op == "7":
                target_account_number = int(input("Enter target account number: "))
                target_account = None
                for acc in Account.accounts:
                    if acc.account_number == target_account_number:
                        target_account = acc
                        break
                
                if target_account:
                    transfer_amount = float(input("Enter transfer amount: "))
                    current_user.transfer(target_account, transfer_amount)
                else:
                    print("Error: Target account does not exist.")

            elif op == "8":
                current_user = None

            else:
                print("Invalid Option")

        elif current_user.account_type=="current":

            print("1. Withdraw\n2. Deposit\n3. Check Balance\n4. Transaction History\n5. Take Loan\n"
                  "6. Transfer Amount\n7. Logout\n")

            op = input("Choose Option: ")

            if op == "1":
                amount = float(input("Enter withdrawal amount: "))
                current_user.withdraw(amount)

            elif op == "2":
                amount = float(input("Enter deposit amount: "))
                current_user.deposit(amount)

            elif op == "3":
                current_user.check_balance()

            elif op == "4":
                current_user.check_transaction_history()

            elif op == "5":
                loan_amount = float(input("Enter loan amount: "))
                current_user.take_loan(loan_amount)

            elif op == "6":
                target_account_number = int(input("Enter target account number: "))
                target_account = None
                for acc in Account.accounts:
                    if acc.account_number == target_account_number:
                        target_account = acc
                        break
                if target_account:
                    transfer_amount = float(input("Enter transfer amount: "))
                    current_user.transfer(target_account, transfer_amount)
                else:
                    print("Error: Target account does not exist.")

            elif op == "7":
                current_user = None

            else:
                print("Invalid Option")