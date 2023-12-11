class Person:
    def __init__(self,name,weight,height) -> None:
        self.name=name
        self.weight=weight
        self.height=height

    def eat(self):
        print('vat')

class Cricketer(Person):
    def __init__(self,name,weight,height,team):
        self.team=team

        super().__init__(name,weight,height)

       #OVerride

    def eat(self):
        print('Vegetables')
s=Cricketer('jahif',34,56,'BD')
s.eat()