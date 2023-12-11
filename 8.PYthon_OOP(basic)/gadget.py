class Laptop:
    def __init__(self,brand,price,memory,color):
       self.brand=brand

       self.brand=brand
       self.price=price
       self.color=color
       self.memory=memory
    def run(self):
        return f'Running laptop:{self.brand}'
    def coding(self):
        return f'learning Python and practicing'


class Phone:
    def __init__(self,brand,price,color,dual_sim):
        self.brand=brand
        self.price=price
        self.color=color
        self.dual_sim=dual_sim

    def run(self):
        return f'Running Phone:{self.brand}'
    def phone_call(self,number,text):
        return f'sending SMS to:{number} with:{text}'
    

class camera:
    def __init__(self,brand,price,color,pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel

    def run(self):
        pass
    def change_lens(self):
        pass

