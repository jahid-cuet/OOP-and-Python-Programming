class Exam:
    def __init__(self,marks):
        self.marks=marks
        self.below_marks=33
        # self.above_marks=100
    
    def mark(self,mrk):
        if mrk<self.below_marks:
            print("you are Fail")
        elif mrk>self.marks:
            print( 'Its Not possible')
        else:
            print(f'You are Pass and your marks is {mrk}')

physics=Exam(100)
physics.mark(70)
        