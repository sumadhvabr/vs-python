class Laptop:
    #__init__()method gets called automatically when the object has been created for this class
    # This function initiliazes the value associated with the object
    # self-represents the object and should be the first parameter
    # self.brand-associating the current objects brand value 
    # =brand-the value passed is assigned to the current objects brand identifier
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price


    def turn_on(self):
        print(f'(self.model) of (self.brand)is now ON')
            # self represents the current object that has called this method
    def specification(self):
        print(f'LAPTOP DETAILS\nBrand:(self.brand)\nModel: (self.model\nPrice:Rs.(self.prive))')
    def turn_off(self):
        print(f'(self.model) of (self.brand) is now OFF')    
print(type(Laptop))
print(id(Laptop))


class Laptop:
    
    def __init__(self,brand,model,price=25000):
        self.brand=brand
        self.model=model
        self.price=price

    def turn_on(self):
        print(f'(self.model) of (self.brand)is now ON')
          
    def specification(self):
        print(f'LAPTOP DETAILS\nBrand:(self.brand)\nModel: (self.model\nPrice:Rs.(self.prive))')
    def turn_off(self):
        print(f'(self.model) of (self.brand) is now OFF')    
print(type(Laptop))
print(id(Laptop))

l5=Laptop('Apple','x')
print(l5.brand,l5.model,l5.price)




class Laptop:
    
    def __init__(self,brand,model,price=25000):
        self.brand=brand
        self.model=model
        self.price=price
        self.battery_level=100
        #every time an object is created for laptop,it has a battery of 100%

    def turn_on(self):
        print(f'(self.model) of (self.brand)is now ON')
          
    def specification(self):
        print(f'LAPTOP DETAILS\nBrand:(self.brand)\nModel: (self.model\nPrice:Rs.(self.prive))')
    def turn_off(self):
        print(f'(self.model) of (self.brand) is now OFF')
    def check_battery(self):
        print(f'this laptop has{self.battery_level}% battery remaining')
print(type(Laptop))
print(id(Laptop))

l5=Laptop('Apple','x')
print(l5.brand,l5.model,l5.price)


l1=Laptop('Aplle','Mac m2',6000)

l1.brand,l1.model,l1.price,l1.battery_level
print(l1.brand,l1.model,l1.price,l1.battery_level)
print(l1.check_battery())



#modification of attributes value once 

#change the value directly using the object

l1.battery_level=90
l1.check_battery()


#use a method that sets a new method each time a method is called

class Laptop:
    
    def __init__(self,brand,model,price=25000):
        self.brand=brand
        self.model=model
        self.price=price
        self.battery_level=100
        #every time an object is created for laptop,it has a battery of 100%

    def turn_on(self):
        print(f'(self.model) of (self.brand)is now ON')
          
    def specification(self):
        print(f'LAPTOP DETAILS\nBrand:(self.brand)\nModel: (self.model\nPrice:Rs.(self.prive))')
    def turn_off(self):
        print(f'(self.model) of (self.brand) is now OFF')
    def check_battery(self):
        print(f'this laptop has{self.battery_level}% battery remaining')
    def update_battery_status(self,val):
        if 0<=val<=100:
            self.battery_level=val
            print(f'battery level of{self.brand},{self.model}')
        else:
            print("Invalid battery level!!! please enter value between 0 and 100 ")



        l1.battery_level=90

                  
