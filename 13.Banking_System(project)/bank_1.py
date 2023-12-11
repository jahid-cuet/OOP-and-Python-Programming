from abc import ABC,abstractmethod
class Account(ABC):
    accounts=[]

    def __init__(self,name,accNumber,password,type) -> None:
        self.name=name
        self.accNumber=accNumber
        self.password=password
        self.type=type
        self.balance=0

        Account.accounts.append(self)

    def Deposit(self,amount):
        
        if amount>=0:
            self.balance +=amount
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
        else:
            print('\n Invalid  Deposit Amount --!!!\n')

    def Withdraw(self,amount):
      
        if amount>=0 and amount<=self.balance:
            self.balance -=amount
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
        else:
            print('\n Invalid Withdrawal Amount --!!!\n')

#Overloading means same Method but parameter change
    def change_info(self,name):
        self.name=name

#Overloading of Change_info :hote pare nam change korte hobe othoba nam anfd password o change kora lagte pare
    def change_info(self,name,password):
        self.name=name
        self.password=password

    @abstractmethod
    def show_info(self):
        pass




class Savings_Account(Account):
    def __init__(self, name, accNumber, password, interestRate) -> None:
        super().__init__(name, accNumber, password, 'savings')
        self.iRate=interestRate



    def show_info(self):
        print(f'Information of {self.type} Account -->\n')
        print(f'Account Name:{self.name}')
        print(f'Account Number:{self.accNumber}')
        print(f'Balance:{self.balance}')
 

    def ApplyInterest(self):
        interest=self.balance*(self.iRate/100)
        print(f' Applied Interest of:{interest}')
        self.Deposit(interest)

class Special_Account(Account):
    def __init__(self, name, accNumber, password,limit) -> None:
        super().__init__(name, accNumber, password, 'special')
        self.limit=limit

    # Over rides the method inside parent(Acount)
    def Withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.limit:
            self.balance -= amount
            print(f"\n--> Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid withdrawal amount or overdraft limit reached")



    def show_info(self):
        print(f'Information of {self.type} Account -->\n')
        print(f'Account Name:{self.name}')
        print(f'Account Number:{self.accNumber}')
        print(f'Balance:{self.balance}')
    



current_account=None

while(True):
    if current_account==None:
        print('No Logging User!!')
        ch=input('Register or Login(R/L):')
        if ch=='R':
            name=input('Enter Account name:')
            accNumber=int(input('Enter Account Number:'))
            password=int(input('Enter Password:'))
            acc=input('Account Savings or Special(sv/sp):')
            if acc=='sv':
                interest=int(input('Enter Interest:'))
                current_account=Savings_Account(name,accNumber,password,interest)
                # current_account.show_info()

            elif acc=='sp':
                lim=int(input('Overdraft limit:'))
                current_account=Special_Account(name,accNumber,password,lim)
            else:
                print('\n Invalid Choice \n')

        else:
            accNumber=int(input("Enter accNumber:"))
            for account in Account.accounts:
                if accNumber==account:
                    current_account=account
                    break


    else:
        print(f'\n Welcome {current_account.name}!\n')
        if current_account.type=='savings':

            print('1.Show_Info')
            print('2.Deposit')
            print('3.Withdraw')
            print('4.Apply Interest')
            print('5.Homework')
            print('6.Logout')
            
            op=int(input("Enter Option:"))
            if(op==1):
                current_account.show_info()

            elif op==2:
                am=int(input('Enter Amount:'))
                current_account.Deposit(am)

            elif op==3:
                am=int(input('Enter Amount:'))
                current_account.Withdraw(am)

            elif op==4:
                current_account.ApplyInterest()

            elif op==5:
                print('Homework')
            elif op==6:
                current_account=None

        else:

            print('1.Show_Info')
            print('2.Deposit')
            print('3.Withdraw')
            print('4.Change_Info')
            print('5.Logout')
            
            op=int(input("Enter Option:"))
            if op==1:
                current_account.show_info()

            elif op==2:
                am=int(input('Enter Amount:'))
                current_account.Deposit(am)

            elif op==3:
                am=int(input('Enter Amount:'))
                current_account.Withdraw(am)

            elif op==4:
                print('Homework')
            elif op==5:
                current_account=None

            
            


    



    