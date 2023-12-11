class Phone():
    cart=[] # This is called Class Attribute

    def __init__(self,buyer) :
        self.buyer=buyer
    
    def add_to_cart(self,car,phone):
        self.cart.append('car')
        self.cart.append('phone')

jahid=Phone('jahid')
print(jahid.buyer)
jahid.add_to_cart('BMW','oppo')
print(jahid.cart)


Tajul=Phone('tajul')
print(Tajul.buyer)
Tajul.add_to_cart('Marcedes','iPhone')
print(Tajul.cart)

# Here class attribute cart=[] access all given value thats why print all of the value