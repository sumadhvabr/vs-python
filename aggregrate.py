class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def teach(self):
        print(f'{self.name} teaches {self.subject}')

class School:
    def __init__(self,name):
        self.name=name
        self.teachers=[]
    def add_teacher(self,t):#t is the object of the teacher clsss
        self.teachers.append(t)
    def show_teachers(self):
        print(f'Teachers in {self.name}:')
        for t in self.teachers:
             print(f'{t.name} for {t.subject}')
s1=School('ABC School')
s2=School('PQR School')
t1=Teacher('Mr XYZ','Maths')
t2=Teacher('Mr LMN','Science')
t3=Teacher('Ms ABC','CS')
t4=Teacher('Mr XYL','PT')
s1.show_teachers()
s1.add_teacher(t1)
s1.add_teacher(t3)
s1.add_teacher(t4)
s2.add_teacher(t2)
s2.add_teacher(t3)
s2.add_teacher(t4)
s1.show_teachers()
s2.show_teachers()

#a user creates folders folders has files files have paragraphs paragraphs has words each word is made up of characters 
           

#a liberary has books users use liberary a smartphone has a camera and a display user uses the smartphone