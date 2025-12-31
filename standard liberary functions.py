#functions

#functions defintion


def add(a,b):
    'the function add a to b'
    return a+b

c=add(10,30)
print(c)



c=add(23+9j,78-34j)
print(c)



d=add(34.0,32)
print(d)



f=(90-89j)
print(f)



g=add('apple','banana')
print(g)



h=add([1,2,3],[5,6,7])
print(h)



#required parameter
# add(10)(error ll cm)


#keyword arguement

i=add(b=89,a=90)
print(i)

#default arguement

f=add(40,50)
print(f)


#variable length arguement

def add(*n, a=10,b=30):
    sum=0
    for i in n:
        sum=sum+i
    sum=sum+a
    sum=sum+b
    return sum
print(add(a=10,b=30))
print(add(10,20,30)) 



#_________________________________________


# from collections import Counter


# input_string=input("Enter the string:")

# freq=Counter(input_string)
# for char,count in freq.items():
#     if count>2:
#         print(f"Character: '{char}' occurs {count} times")


#________________________________
# from collections import Counter

# items=[]
# for i in range(10):
#     item=input(f"Enter item{i+1}:")
#     item.append(item)
    
    
# count=Counter(items)

# max_count=max(count.values())

# most_common_items=items=[item for item,cnt in count.items() if cnt==max_count]

# if len(most_common_items)==1:
#     print("The most common item is:",most_common_item)
# else:
#     print("The most common item are(tie):")

#     for item in most_common_items:
#         print(items)
    #_____________________________________________

# from collections import OrderedDict

# n=int(input("Enter number of integers:"))

# print("Enter the integers")
# numbers=[]

# for i in range(n):
#     num=int(input(f"Number{i+1}:"))  
#     numbers.append(num)



# unique_numbers=OrderedDict()

# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers[num]=True


# print("\nUnique numbers in the same order:")

# for num in unique_numbers.keys():
#     print(num,end="")



#____________________________________
n=int(input("Enter number of items:"))


items=[]
print("Enter item details(code,quantity,price):")
for i in range(n):
    code=input(f"item{i+1}code:").strip()
    qty=int(input("Quantity:"))
    price=float(input("price:"))
    items.append((code,qty,price))
    print()
threshold=float(input("Enter threshold amount:"))

total_bill=0
print("\nitem where qty*price>threshold:")
for code,qty,price in items:
    total=qty*price
    total_bill+=total
    if total>threshold:
        print(f"Code:{code},Quantity:{qty},Price:{price},Total{total:.2f}")
print(f"\nTotal Bill Amount={total_bill:.2f}")



    