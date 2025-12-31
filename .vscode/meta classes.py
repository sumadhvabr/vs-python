# # creation of the class using type 

# #define method

# def greet(self):
#     print(f'Hello {self.name}')
# # create the class and attach the method to the class 

# Student=type('Student', (object,), {'greet':greet,'name':'XYZ'})
# # create the object of the class 
# s=Student()
# print(type(s))
# print(type(Student))
# s.greet()

# # creation of custom meta class 

# class RequiredID(type):
#     #to create a meta class it has to inherit from type
#     #type builds classes
#     def __new__(cls,name,bases,attr):
#         #custom new method is defined
#         #parameters are cls-metaclass itself name-name of the class being created basses-tuples of base class attr-dictionary of attributes and methods of the class
#         if 'id' not in attr:
#             attr['id']=100
#             #check whether an attribute called as id exists if the class doesnt define id a default attribute id is added with a value of 100
#         return super().__new__(cls,name,bases,attr)
#         #calling type's new method


# #create a class that uses the custom meta class


# class Student(metaclass=RequiredID):
#     # "metaclaa=RequiredID tells python to use RequiredID as the metaclass and not the default"
#     # "metaclass"
#     # "name-student"
#     # "basses-empty tuple since it does not inherit anyother"
#     # "class except the metaclass"
#     # "attr-should be the dictionary"
#     def __init__(self,name):
#         self.name=name
# s1=Student('Alice')
# print(s1.name)
# print(id(s1))
# print(s1.greet)

# Creation of the class using type
#1. Define Method
# def greet(self):
#     print(f'Hello {self.name}')
    
# #create a class and attach the method to the class
# Student=type('Student', (object,), {'greet': greet, 'name': 'John Doe'})
# #Create an instance of the class
# s1=Student()
# s1.greet()

# print(type(s1))

        
# #2. Using metaclass to create a class
# #Define a metaclass
# class Required_id(type):   
#     def _new_(cls, name, bases, attrs):
#         if 'greet' not in attrs:
#             attrs['greet'] = 100
#         return super()._new_(cls, name, bases, attrs)
    
# #Create a class using the metaclass
# class Student(metaclass=Required_id):
#     def _init_(self, name):
#         self.name = name
        
# s1=Student('Alice')
# print(s1.name)
# print(type(s1))
# print(id(s1))
# print(s1.greet)  # Accessing the greet attribute added by the metaclass

# class Teacher(metaclass=Required_id):
#     id=20
#     def _init_(self, name):
#         self.name = name
        
# t1=Teacher('Bob')
# print(t1.name)
# print(t1.id)
# print(t1.greet)  # Accessing the greet attribute added by the metaclass 


# #metaclass with inheritance
# #create custom metaclass
# class CustomMeta(type):
#     def _new_(cls, name, bases, attrs):
#         print(f'Creating class {name} with CustomMeta')
#         attrs['created_by'] = 'CustomMeta'
#         attrs['created_on'] = '2024-06-01'
#         return super()._new_(cls, name, bases, attrs)
    
# # Use metaclass keyword
# class Example(metaclass=CustomMeta):
#     def greet(self):
#         return 'Hello from Example class'
    
# #inheriting from a class that uses the custom metaclass
# class ExampleB(Example):
#     def greet(self):
#         print('Hello from ExampleB class')
        
# Example().greet()
# ExampleB().greet()

# #check for the attributes added by the metaclass
# print(Example.created_by)
# print(Example.created_on)
# print(ExampleB.created_by)
# print(ExampleB.created_on)


# class ExampleC(ExampleB):
#     def greet(self):
#         print('Hello from ExampleC class')
        
# ExampleC().greet()
# print(ExampleC.created_by)
# print(ExampleC.created_on)
        