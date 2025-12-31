# recursive function for adding upto n values


# def sumofn(n):
#     if n==0:
#         return 0
#     return + sumofn(n-1)




# n=(input("Enter the numbers"))
# if




#factorial



def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the number:"))
if n<0:
    print('Factorial of negstive numbers do not exist')
else:
    print(f'Factorial of {n} is {factorial(n)}')








    # gcd



    def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    a=int(input("Enter the first number:"))
    b=int(input("enter the second number:"))

    print(f"The GCD of {a},{b} is {gcd(a,b)}")


    #lambda arguments:expression(syntax)