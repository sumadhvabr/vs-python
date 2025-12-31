def outer():
    print("inside outer")
    def inner():
        print("inside inner")
    inner()
outer()    







#local variables in nested functions


def outer():
    x=10
    print(f"memoory location pf x is {id(x)}")
    print(f"x in outer=(x)")
    def inner():
        x=10
    print(f"memoory location pf x is {id(x)}")
    print(f"x in inner=(x)")
    inner()
    print(f"memory location of x in inner is id(x)")
    print(f"x in outer =(x)")
outer()    






#passing arguements to nested functions


def outer(n):
    print(f"The value of n in outer is {n}")
    def inner():
        print(f"The value of n in inner is {n}")
    inner()

n=input("enter the value:")
outer(n)        




def outer(n):
    print(f"The value of n in outer is {n}")
    def inner():
        n=int(input("entter th number:"))
        print(f"The value of n in inner is {n}")
    inner()

n=input("enter the value:")
outer(n)        