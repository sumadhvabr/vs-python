class Employee:
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    def show(self):
        print(f'I am {self.name} working in {self.dept} for RS .{self.salary}')




e1=Employee('ABC','PQR,', 150000)
e1.show()




#access Modifiers
class Employee:
    def __init__(self,name,dept,salary):
        self.name=name #public access
        self.dept=dept #protected access
        self.salary=salary #private access

    #public maehod to access the data members
    def show(self):
        print(f'I am {self.name} working in {self.dept} for RS .{self.salary}')


e1=Employee('ABC','HR', 1500000)

#accessing the data members from outside the class

#use the object and the data member
e1.show()

class Employee:
    def __init__(self,name,dept,salary):
        self.name=name #public access
        self.dept=dept #protected access
        self.salary=salary #private access

    #public maehod to access the data members
    def show(self):
        print(f'I am {self.name} working in {self.dept} for RS .{self.salary}')
    #protected
    def _display(self):
        print(f'I am {self.name} working in {self.dept} for RS .{self.salary}')
        #private
    def __see(self):
        print(f'I am {self.name} working in {self.dept} for RS .{self.salary}')

e1=Employee('XYZ','HR', 1500000)
e1.show()
e1._display()
e1.__Employee__see()