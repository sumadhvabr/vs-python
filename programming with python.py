l=[1,2,3,4,5,6]
l.append(7)
print(l)

#extend
l.extend([8,9,10])
print(l)


#pop
l.pop(4)
print(l)


#remove

l.remove(2)
print(l)


#reverse

l.reverse()
print(l)

#sort

l.sort()
print(l)


l3=['a','apple','Apple']
l3.sort()
print(l3)



#tupple
t=(1,2,3)
print(type(t))
print(id(t))

t1=(1)
print(type(t1))

t2=tuple('a')
print(type(t2),type(t1))


t3=('a')
print(type(t3))


t4=('a',)
print(type(t4))

t5=((1,2,3),['a','b'],(1,2,3),'str')
print(type(t5))
print(type(t5[1]))


#count
print(t.count(1))


#index
print(t.index(2))




#_____________________________
#sets


s={1,2,3}
print(type(s))
print(id(s))


s1={1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,5,6}
print(s1)
s1.add(1)




print(s.intersection(s1))
print(s)

print(s1.union(s))


print(s1&s)
print(s1|s)


print(s1-s)
print(s-s1)


print(s.symmetric_difference(s1))
print(s1.symmetric_difference(s))



##frozen set


l=[1,2,3]
s={1,2,3}
t=(1,2,3)
print(id(l),id(s),id(t))


fl=frozenset(l)
fs=frozenset(s)
ft=frozenset(t)
print(fl,fs,ft)

f_s=frozenset({1,2,3})
print(f_s)

print(f_s.union(fl))




#______________________________________________________________________________________________________________
# import os
# print("The current working directory.",os.getcwd())

# new="Directory"
# os.mkdir(new)
# # os.rmdir("Directory")

# if os.path.exists(new):
#     print(f'Directory{new} is created successfully.')
# else:
#     print("error in creation.")

# os.chdir(new)
# print("current dir",os.getcwd())

# os.mkdir("dir1")
# os.mkdir("dir2")

# path1="D:\Github\Python Exp Lear"
# path2="D:\Github\Python Exp Lear\Directory"

# pth=os.path.join(path1,path2)

# print("Path is:",pth)

# if os.path.exists(pth):
#     print(f'{pth}is correct')


#______________________________________________________
import sys
# print(f"The python version is{sys.version}")



# import sys 
# print('enter the user name')
# u_name=sys.stdin.readline().rstrip('\n')
# sys.stdout.write(u_name+'\n\n')
# sys.stderr.write('this is a error message')




#_______________________________________________-
n=1234567890
l=[1,2,3,4,5,6,7,8,9,0]
l1=['1','2','3','4','5','6','7','8','9','0']
s={1,2,3,4,5,6,7,8,9,0}
s1={'1','2','3','4','5','6','7','8','9','0'}
t=(1,2,3,4,5,6,7,8,9,0)
t1=('1','2','3','4','5','6','7','8','9','0')
d={1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:0}
d1={1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'0'}
print(f'the size of {n} is {sys.getsizeof(n)} bytes')
print(f'the size of {l} is {sys.getsizeof(l)} bytes')
print(f'the size of {s} is {sys.getsizeof(s)} bytes')
print(f'the size of {s1} is {sys.getsizeof(s1)} bytes')
print(f'the size of {t} is {sys.getsizeof(t)} bytes')
print(f'the size of {t1} is {sys.getsizeof(t1)} bytes')
print(f'the size of {d} is {sys.getsizeof(d)} bytes')
print(f'the size of {d1} is {sys.getsizeof(d1)} bytes')

# sys.exit(0)

#__________________________________________________________--
#counter counts the occurrences in an itera


from collections import Counter 
l=[1,2,3,4]
print(Counter(l))



s="this is ithe statement"
print(Counter(s))



#deque


from collections import deque
d=deque([10,20,30,40])
print(type(d))





#rear
d.append(60)
print(d)



#front

d.appendleft(70)
print(d)



#deletion
#rear
d.pop()
print(d)

#front
d.popleft()
print(d)


#chainmap



from collections import ChainMap as cm

d={1:'a',2:'b'}
d1={2:'c',3:'d'}
d2={4:'e',5:'f'}

c=cm(d,d2,d2)
print(c)
print(type(c))


#accessing values of a chainmap


print(c[1])
print(c[4])
print(c[5])



#adding a new chain at the front of a chainmap


id(c)
print(id(c))


c.new_child({4:'g',6:'h',7:'i'})
print(c)
print(id(c))


#view all maps expect the first map


print(c.parents)

print(c.items)
print(c.keys)
print(c.values)



#ordered dictionary


from collections import OrderedDict as od

#create



o_d=od({1:'a',2:'b',3:'c',4:'d'})
type(o_d)
print(type(o_d))

o_d1=od({(1,'a'),(2,'b'),(3,'c')})
type(o_d1)
print(type(o_d1))



#move values
o_d.move_to_end(1)
print(o_d)



for k in o_d:
    print(k)

#display it in reverse order 
for k in reversed(o_d):
    print(k)



d={1:'a',2:'b'}
print(type(d))
print(d[1],d[2])


#integer default dictionary


from collections import defaultdict as dd


id=dd(int)
id['a']=1
id['b']+=1
print(id,type(id),id['c'])


#complex default dictionary


id=dd(float)
id['a']=1
id['b']+=1
print(id,type(id),id['c'])

# id=dd(dict)
# id['a']=1
# id['b']+=1
# print(id,type(id),id['c'])


id=dd(complex)
id['a']=1
id['b']+=1
print(id,type(id),id['c'])




#function default dictionary

def valuenotpresent():
    return 'value has not been created'


id=dd(valuenotpresent)
id['a']=1
id['b']=1
print(id,type(id),id['c'])




students=[{'name':'sumadhva','score':100},
          {'name':'virat','score':90},
          {'name':'sachin','score':70}
          ]
print(students)

#named tuple


from collections import namedtuple
person=namedtuple('person',['name','age'])
p1=person(name='albus',age=120)
p2=person('sachin',70)
p3=person(age=11,name='harry')
print(p1)
print(p3.name)
print(p2)




#user list 

from collections import UserList


#craete a custom list of the type userlist

class customList(UserList):
    def addtwice(self,value):
        self.data.append(value)
        self.data.append(value)
    def remtwice(self,pos):
        self.data.pop(pos)
        self.data.pop(pos)




 #craete instance of custom list


c1=customList([1,2,3,4,5,6,7])
c1.append(8)
print(c1)  


c1.insert(0,10)
print(c1)


c1.remove(4)
print(c1)



c1.reverse()
print(c1)



c1.sort()
print(c1)


c1.addtwice(12)
print(c1)

c1.remtwice(5)
print(c1)




#user string

from collections import UserString


#create custom string


class MyString(UserString):
    def uppercon(self):
        return self.upper()
    def add_exclamation(self):
        return self.data+'!!!'
    


    #create an instance of custom string



cs=MyString("Hello,how r u")
print(cs)


print(cs.uppercon())
# print(id(cs))
print(cs.add_exclamation())





#__________________________________
def is_even(n):
    if n%2==0:
        return n
    l=list(filter(is_even,range(20)))
    print(l)


