# encapsulation --> hide details
# access modifier: public, protected, private
class Bank:
    def __init__(self,holder_name,balance) -> None:
         self.holder_name=holder_name # public attribute
         self.__branch='Banani 12' # protected 
         self.__balance=balance # private

    def deposit(self,amount):
        self.__balance+=amount
    def get_amount(self):
        return self.__balance

    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=self.__balance-amount
            return amount
        else:
            return ("you are a fokir")
    
Jahid=Bank('jahid',2000)
print(Jahid.get_amount())
Jahid.deposit(1000)
print(Jahid.get_amount())
# print(Jahid.withdraw(1500))
print(Jahid.get_amount())


