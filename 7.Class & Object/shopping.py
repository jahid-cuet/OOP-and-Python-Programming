class Shopping:
    def __init__(self,name) :
        self.name=name
        self.cart=[]

    def add_to_cart(self,item,price,quantity):
        product={'Item': item,'price':price, 'quantity':quantity}
        self.cart.append(product)
        # print(self.cart)

    def checkout(self,amount):
        total=0
        for i in self.cart:
            total+=i['price']*i['quantity']
        if total>amount:
            print(f'You give {total-amount} more money')
        elif total<amount:
            print(f'You will get {amount-total} money')


Jahid_shopping=Shopping('Jahid')
Jahid_shopping.add_to_cart('Alu',25,2)
Jahid_shopping.add_to_cart('dim', 5, 10)
Jahid_shopping.add_to_cart('rice', 50, 2)

Jahid_shopping.checkout(300)