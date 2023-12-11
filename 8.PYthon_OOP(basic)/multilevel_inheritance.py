class Vehicle:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price

    def __repr__(self) -> str:
        return f'{self.name} {self.price}'


class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat=seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price,weight) -> None:
        self.weight=weight
        super().__init__(name, price)


class Pick_up(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

    def __repr__(self) -> str:
        print(f)
        return super().__repr__()

class AC_Bus(Bus) :
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature=temperature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        # print(f'{self.seat}')
        return super().__repr__()


Green_line=AC_Bus('green',2000000,40,15)
print(Green_line)
