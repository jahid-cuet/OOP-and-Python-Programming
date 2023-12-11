from menu import Burger,Pizza,Drinks,Menu
from restaurant import Restaurant
from user import Chef, Customer, Server, Manager
from Order import Order

def main():
    menuu=Menu()
    Pizza_1=Pizza('Fish pizza',500,'large',['fish','Onion','Oil'])
    menuu.add_menu_item('pizza',Pizza_1)

    Pizza_2=Pizza('Chicken pizza',550,'large',['Chicken','Onion','Oil'])
    menuu.add_menu_item('pizza',Pizza_2)
    Pizza_3=Pizza('Meat pizza',600,'large',['Meet','Onion','Oil'])
    menuu.add_menu_item('pizza',Pizza_3)

    
    # add burger to the menu
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menuu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menuu.add_menu_item('burger', burger_2)

    # add drinks to the menu
    coke = Drinks('Coke', 50, True)
    menuu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha Coffee', 300, False)
    menuu.add_menu_item('drinks', coffee)

    # menuu.show_menu()

    restaurant=Restaurant('Dibanishi',2000,menuu)
    jahid=Manager('jahid',18,'jahid@gmail.com','Satbila',10000,'january 20','core')
    restaurant.add_employee('Manager',jahid)
    chef = Chef('Rustom Baburchi', 6, 'chupa@rustom.com', 'rustomNagar', 3500, 'Feb 1, 2020', 'Chef', 'everything')
    restaurant.add_employee('chef', chef)
    server = Server('Chotu server', 6, 'nai@jai.com', 'restaurant', 200, 'March 1, 2020', 'server')
    restaurant.add_employee('server', server)

    # show employees
    # restaurant.show_employees()

    #Customer 1 placing an order

    customer_1 = Customer('Sakib Khan', 6, 'king@khan.com', "banani", 100000)
    order_1=Order(customer_1,[Pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    #customer one paying for order_1
    restaurant.receive_payment(order_1,2000,customer_1)
    print('revenue and Balance After 1st Customer',restaurant.revenue,restaurant.balance)

 #Customer 2 placing an order
    customer_2 = Customer('jayed Khan', 9, 'soleman@khan.com', "banani", 200000)
    order_2=Order(customer_2,[Pizza_2,burger_2,coffee])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

    #customer one paying for order_2
    restaurant.receive_payment(order_2,5000,customer_2)
    print('revenue and Balance After 1st Customer',restaurant.revenue,restaurant.balance)

#Pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('after rent', restaurant.revenue, restaurant.balance, restaurant.expense)


    restaurant.pay_salary(chef)
    print('after salary', restaurant.revenue, restaurant.balance, restaurant.expense)





# call the main 
if __name__ == '__main__':
    main()