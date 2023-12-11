class Bank:

    def __init__(self,balance):

        self.balance=balance            # bank e koto taka rakhsi oiita
        self.min_withdraw=100           #bank e minimum koto taka rakha jabe
        self.max_widthdraw=10000        #bank e maximum koto taka rakha jabe

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'Your Present Amount is {self.get_balance()}')

    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print('You are a great Fokir')

        elif amount>self.max_widthdraw:
            print(f' Bank will fokir if you take {amount} ')  
        else:
            self.balance -=amount
            print(f'please take :{amount}')
            print(f'And Your Present Amount is:{self.get_balance()}')


brac=Bank(20000)
# brac.withdraw(30)
# brac.withdraw(300000)
# brac.withdraw(3000)
brac.deposit(10000)