class Company:
    def __init__(self,name) -> None:
        self.cmpname=name
        

    def Company_detail(self):
        print(f'MY Company Name is: {self.cmpname}')

class Person(Company):
    def __init__(self,age,name) -> None:
        self.age=age
        self.name=name
        # Company.__init__(self,name)
    def Person_detail(self):
        print(f' My name is {self.name} my age {self.age}')


class Employee(Person,Company):
    def __init__(self, cmpname,name,age,Salary) -> None:
        self.Salary=Salary
        Person.__init__(self,age,name)
        Company.__init__(self,cmpname)
    def detail(self):
        print(f'MY Salary is {self.Salary}')



Jahid=Employee('Google','Jahid Hasan',23,50000)
Jahid.Person_detail()
Jahid.detail()
Jahid.Company_detail()


#Attribute is Far more Important always Focus on Attribue(Form: self.Attribute)