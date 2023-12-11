class Animal:
    def __init__(self,name) -> None:
        self.name=name
        
    def eat(self):
        print('I can eat')

    
class Cat(Animal):
    def __init__(self,name) -> None:
        # self.name=name         # Type->1
        # super().__init__(name) # Type->2
        Animal.__init__(self,name)


Jerry=Cat('jerry')
Jerry.eat()