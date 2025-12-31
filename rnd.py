import random as r
r.seed(10)
print(f"random integer value in a given range is:{(r.randint(10,100000))}")


c=['apple','banana','mango','guava']
print(f"Random choices of 4 from the list is: {r.choice(c)}")
#____________________________________________________________________



from datetime import date,time,datetime,timedelta
print(f"The current date and time is ({datetime.now()})")

print(f"Future date after '7' days is {datetime.now()+timedelta(days=7)}")

print(f"The current date and time is {datetime.now().strftime('%Y-%m-%d:%H-%M-%S')}")
