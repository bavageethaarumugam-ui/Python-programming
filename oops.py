class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.name=b
        self.age=c
    def disp(self):
        print(self.sno)
        print(self.name)
        print(self.age)
ob=stud(123,'abc',17)
ob.disp()
