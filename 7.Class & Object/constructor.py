class Phone():
    # name='iphone14'

    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price
    def add(self,a,b):
        return a+b

my_phone=Phone('jahid','Redmi',10000)
print(my_phone.owner,my_phone.brand)
her_phone=Phone('She','Oppo',1000)
print(her_phone.owner,her_phone.brand,her_phone.price)

