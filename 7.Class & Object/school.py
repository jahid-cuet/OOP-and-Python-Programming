class Student:
    def __init__(self,name,Class,id) :
        self.name=name
        self.Class=Class
        self.id=id      
    def __repr__(self) -> str:
        return  f'My name is: {self.name} & My class:{self.Class} & My Id :{self.id}'

class Teacher:
    def __init__(self,name,Subject,id) :
        self.name=name
        self.Class=Subject
        self.id=id      
    def __repr__(self) -> str:
        return  f'My name is: {self.name} & My class:{self.Class} & My Id :{self.id}'
    

class School:
    def __init__(self,name) :
        self.name=name
        self.teachers=[]
        self.students=[]

    def add_teacher(self,name,subject):
       id=len(self.teachers)+101
       teacher=Teacher(name,subject,id)
       self.teachers.append(teacher)
    def enroll(self,name,fee):
        if fee<6500:
            return 'not enough fee'
        else:
            id=len(self.students)+1
            student=Student(name,'Python',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
       
    def __repr__(self) -> str:
        print('welcome to', self.name)
        print('--------OUR Teachers--------')
        for teacher in self.teachers:
            print(teacher)
        print('--------OUR STUDENTS--------')
        for student in self.students:
            print(student)
        return 'All Done for now'


phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)


# Jahid=Student('jahid','15',1911018)
# print(Jahid)
# Rayhan=Teacher('Rayhan','EEE',100)
# print(Rayhan)