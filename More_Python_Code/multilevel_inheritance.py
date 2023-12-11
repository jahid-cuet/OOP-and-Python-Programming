class Grandfather:
    def __init__(self,name) -> None:
        self.name=name
    def property(self):
     print('My property"s value is 5 crore')


class Father(Grandfather):
    def __init__(self, name) -> None:
        Grandfather.__init__(self,name)

        
    def property(self):
        print(self.name,'has 1 crore')
    # def property(self):
    #     return super().property()


class Ami(Father):
    def __init__(self, name) -> None:
        Father.__init__(self,name)  #here we also use super() that give 1 argument in this case
    
    def property(self):
        print(self.name,'have 2 crore')
    # def property(self):
    #     return super().property()


ami=Ami('jahid')
ami.property()
father=Father('Monir Hossain')
father.property()