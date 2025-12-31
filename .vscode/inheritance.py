#parent class


class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.battery_level = 100

    def turn_on(self):
        print(f'{self.model} of {self.brand} is now turned on')

    def turn_of(self):
        print(f'{self.model} of {self.brand} is now turned OFF')

    def check_battery(self):
        print(f'The laptop has {self.battery_level}%battery remaining')
        
    def dec_battery(self,usage):
        if usage<0:
            print('usuage amount cannot be negative')
        elif self.battery_level < 0:
            print("Battery too Low.please charge the laptop")
        else:
            self.battery_level=usage
            print(f'Battery decreased by {usage}% Current Level: {self.battery_level}')




#child class

class GamingLaptop(Laptop):
#inherits the attributes from the parent class Laptop
    def __init__(self,brand,model,price,gpu,ram):
        #initialize the attributes of the parent class
        super().__init__(brand,model,price)
        #this is a call and not a definition 
        #self is taken from the child object that wants to be initilized
        self.gpu=gpu
        self.ram=ram

    def boost_model(self):
        print(f'{self.model} of {self.brand} is running in boost mode with {self.gpu} and {self.ram}')

    

    def turn_on(self):
        return f'{self.model} of {self.brand} is starting in high performance gaming mode with {self.gpu}'
    

    #object initilization


l1=Laptop("apple","m2",1000000)
gl1=GamingLaptop("Asus","Rog",55000,'nvidia rtx 4050',6)


l1.turn_on()
l1.check_battery()
l1.dec_battery(10)
l1.check_battery()

gl1.turn_on()



#method resoultion order


# base class


class Root:
    def do(self):
        print("Root.do (completed)")



#inherited classes


class A(Root):
    def do(self):
        print('A.do')
        super().do()




class B(A):
    def do(self):
        print('B.do')
        super().do()


class C(A):
    def do(self):
        print('C.do')
        super().do()


class D(B,C):
    pass

class E(C,B):
    pass



D().do()
E().do()
# class F(D,E,B,C):
#     pass
print('MRO of Class D:',[cls.__name__ for cls in D.mro()])  
print('MRO of Class E:',[cls.__name__ for cls in E.mro()])  
print(E.__mro__)
print(D.__mro__)


#define a class car with parameter of model and year and has method read and update create an electric car that has  attribute battery and has the methods read battery and check battery and also displays how much time before the recharge.

#base class person child class teacher and student teaching assistant inherit both teacher and student..each class defines method called as role.



#duck typing


class Dog:
    def walk(self):
        print("I have 2 legs and can walk")
class Emu:
    def walk(self):
        print("I have 2 legs and can walk")

class Parrot:
    def fly(self):
        print("I have wings and can fly")
Dog().walk()
Parrot().fly()
Emu().walk()


# create a base class called as shape with a method area drive the classes circle and rectangle tat override area that revelant formula.call area for different object
    
    