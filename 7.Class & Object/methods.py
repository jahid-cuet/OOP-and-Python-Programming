class person:
    name='Jahid'
    id=1911018
    occu='student'
    skills=['python','c','c++','html','css','bootsrap']

    def info(self):
        print("This is my information")
    def j_info(self,name,id):
         text=f'My name is :{name} and my id is:{id}'
         return text
    def add(self,a,b):
        return a+b

p=person()
p.info()
result=p.j_info('j',3)
print(result)
addition=p.add(2,3)
print('result is:',addition)
