class Course:
    def __init__(self,name,credits):
        self.name=name
        self.credits=credits
        
        
    @classmethod
    def with_default_credits(cls,name):
        return cls(name,4)
    def display(self):
        print(f"Course Name: {self.name},Credits:{self.credits}")
        
c1=Course.with_default_credits("Data Structures")
c2=Course.with_default_credits("Operating systems")
c3=Course.with_default_credits("DBMS")
c1.display()
c2.display()
c3.display()
