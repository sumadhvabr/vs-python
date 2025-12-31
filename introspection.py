l=[1,2,3,4]
str='Hello'
t=(1,2,3)
d={1:2,2:3,3:4}
n=123
print(dir(l))
print(l.__add__([5]))
print(l.__sizeof__())
print(l.__hash__)
print(l.__contains__(1))
print(l.__contains__(5))
print(dir(str))
print(dir(t))
print(dir(n))
print(dir(d))
print(n.numerator)
print(n.bit_length())
#type()
print(type(1),type(True),type([]),type(' '))
class A:
    pass
print(type(A))
class B(A):
    pass
print(type(B()))
class B(A):
    pass
print(type(B()),type(B))
#B() is an object and B is a class 
#objects are instances of class,class is an instance of meta class
import os
def f():
    pass
print(type(os),type(f))
#id

print(id(1),id(True),id([]),id(()),id(''),id(""))
print(id(' ' ' ' ' '))
print(id(A),id(B))
print(id(f),id(os))

