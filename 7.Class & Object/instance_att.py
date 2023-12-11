class Phone():
   

    def __init__(self,buyer) :
        self.buyer=buyer
        self.cart=[] # This is called instance Attribute
    
    def add_to_cart(self,car,phone):
        self.cart.append(car)
        self.cart.append(phone)

jahid=Phone('jahid')
print(jahid.buyer)
jahid.add_to_cart('BMW','oppo')
print(jahid.cart)


Tajul=Phone('tajul')
print(Tajul.buyer)
Tajul.add_to_cart('Marcedes','iPhone')
print(Tajul.cart)

# Here instance attribute cart=[] access instance value thats why print all of the value differently