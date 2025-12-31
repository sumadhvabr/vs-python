class Coding:
    def __init__(self):
        print("The object has been initilized")
    def show(self):
        print("The object has been shown")
Coding()
Coding().show()
#this is the new object that got initilized and the show method is executed


#parameterized constructors

class Addition:
    def __init__(self,f,s):
        self.f=f
        self.s=s
    def calculate(self):
        self.ans=self.f+self.s 
    def display(self):
        print(f"The addition of {self.f} and {self.s} results in {self.ans}")
a=Addition(10,20)
a.calculate()
a.display()


#destructor

class A:
    def __init__(self):
        print("The object is initilized")
    def __del__(self):
        print("The object is destroyed")
a=A()
del a

a=A().__init__()



#static and class methods

#static methode

class NewClass:
    val=10
    def __init__(self,value):
        self.ivalue=value
    @staticmethod
    def count():
        NewClass.val+=1
    def show(self):
        print(f"The number of object created is {NewClass.val}")
o=NewClass(10)
o.count()
o.show()
NewClass(10).count()
NewClass(10).show()
print(o)



#class Methods

class NewClass:
    val=10
    def __init__(self,a,b):
        self.a=a
        self.b=b 
    @classmethod
    def incr(cls,x):
        cls.val+=1
    def show(self):
        print(f"The attribute is {self.a},{self.b},the val is {NewClass.val}")
o=NewClass(10,3)
o.incr(10)
o1=NewClass(10,3)
o.show()
o1.incr(25)
o1.show()


#new()
class NewClass:
    def __new__(cls,a):
        print("Inside new method")
        i=super().__new__(cls)
        # super refers to the parent class which is the built in object class
        return i
    def __init__(self,b):
        print("Inside init method")
        self.b=b  
    def show(self):
        print(f"The stored value is {self.b}")
o=NewClass(10)
o.show()







