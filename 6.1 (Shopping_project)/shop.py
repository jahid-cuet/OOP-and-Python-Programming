class Product:
    def __init__(self,name,price) -> None:
        self.name=name
        # self.quanrity=quantity
        self.price=price
    def __repr__(self) -> str:
        return (f'name is: {self.name} and price is {self.price}')


class Shop(Product):
    # cart=[]
    def __init__(self,name,price,quantity):
        self.cart=[]
        self.quantity=quantity
        super().__init__(name,price)
        p={'name':name,'quantity':quantity,'price':price}
        self.cart.append(p)
        

    def add_product(self,name,price,color):
        self.color=color
        super().__init__(name,price)
        a={'name':name,'price':price,'color':color}
        self.cart.append(a)
        return f'name:{self.name} price:{self.price} quantit:{self.color}'

    
    def buy_product(self,name,given_price):
        super().__init__(name,given_price)
        
        for i in self.cart:
            if name == i['name'] and i['price'] <= given_price:
                return f'Congratulations ,You have got the {name}'
            
        return f'Sorry {name} is not Available'
        
pro=Shop('Mango',50,10)

pro.add_product('Banana',100,'yellow')
pro.add_product('Apple',150,'white')
pro.add_product('Licchi',100,'red')
pro.add_product('Orange',100,'yellow')
pro.add_product('jack fruit',170,'brown')
pro.add_product('Lemon',15,'green')
pro.add_product('graps',100,'yellow')
pro.add_product('black Berry',90,'Black')
pro.add_product('Avocado',500,'blue')
pro.add_product('green Coconut',90,'green')


b_pro=pro.buy_product((input()),int(input()))
# b_pro=pro.buy_product((input()),int(input()))
# b_pro=pro.buy_product((input()),int(input()))
print(b_pro)