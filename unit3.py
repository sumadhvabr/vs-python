#syntax error

# x=10
# if x==10:
# print(x)




#logical error

# def fact_cal(n):
#     r=1
#     for i in range(n):
#         r=r*i#it starts with a zero by default
#         print(r)


# fact_cal(4)

# def fact_cal(n):
#     r=1
#     for i in range(1,n):#it goes upto n
#         r=r*i
#         print(r)


# fact_cal(4)

# def fact_cal(n):
#     r=1
#     for i in range(1,n+1):
#         r=r*i#it starts with a zero by default
#         print(r)


# fact_cal(4)



#runtime errors or exceptions


#list of exception handeled in python


# import builtins
# l=[name for name in dir(builtins)
#    if isinstance(getattr(builtins,name),type)
#    and
#    issubclass(getattr(builtins,name),BaseException)]
# print("List of Excepttion in python")
# for i in l:
#     print(i)


#arithmetic error
#1.a floating point error

# 1.2-1.0

# if 1.2-1.0==0.2:
#     print("true")
# else:
#     print("false")


# 1.b overflow error

# import math
# math.exp(100000)
# pow(3.14,10000)

#1.c zero divison error

# 10.0/0.0
# 10/0


# 2.attribute error
# s="hello"
# s.reverse()



# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print(f"hello,my name is {self.name}")


# print(p=person("ironman",40))



#3.assertion error


# def division(a,b):
#     assert b!=0
#     return a/b
# print(division(10,2))
# print(division(10,0.0))



# 4 file exists error

# def create_file(filepath):
#     open(filepath,'x')#creates a file if it doesnt exist
#     print(f'{filepath} created successfully')
# create_file('new_file1.text')



# 5.filenotfounderror

# f=open('new.txt','r')#r opens the file if it exists in read mode
# print("file opened")

# 5.a.ioerror

# try:
#     f=open('new.txt','r')
#     print("file Opened")
# except IOError as e:
#     print(f'IOError:{e}')




 # 6.KeyError

# d={'name':'Alpha','age':20,'city':'manglore'}
# d['address']


# 6.a.lookuperror

# try:
#     d={'name':'alpha','age':30,'city':'manglore'}
#     d['address']
# except LookupError as e:
#     print(f"LOokupError:{e}")


# 7.NameError
# x=10
# z=x+y


#8.typeerror


# x='10'
# y=10
# z=x+y


# 9.index error

# l=[1,2,3,4,5,6]
# l[6]

# 10.ValueError

# v=int("hello")


# 11.KeyboardInterrupt erroe
# name=input("enter the value")

# 12.UnboundLocalError

# def fact_cal(n):
#     for i in range(1,n+i):
#         r=r*i
#     return r


# fact_cal(5)


# Exception handling

# 1.try and except block

# n=int(input("enter the numerator"))
# try:
#     d=int(input("Enter the denominator"))
#     print(n/d)
# except ZeroDivisionError as e:
#     print(f'ZeroDivisionError:{e}')


# n=int(input("enter the numerator"))

# d=int(input("Enter the denominator"))
# print(n/d)
# print(f'ZeroDivisionError:{e}')



#multiple exception handling


# try:
#     l=[0,2,4,5,6,8,10]
#     i1=int(input("enter the first index"))
#     i2=int(input("enter the second index"))
#     print(l[i1]/l[i2])

# except IndexError as e:
#     print(f'IndexError:{e}.check the index number')
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError:{e}.The index is pointing at a 0 value")




# try:
#     l=[0,2,4,5,6,8,10]
#     i1=int(input("enter the first index"))
#     i2=int(input("enter the second index"))
#     print(l[i1]/l[i2])

# except IndexError as e:
#     print(f'IndexError:{e}.check the index number')
# except:
#     print(f"Division not possible")

# try:
#     l=[0,2,4,5,6,8,10]
#     i1=int(input("enter the first index"))
#     i2=int(input("enter the second index"))
#     print(l[i1]/l[i2])

# except:
#     print(f'IndexError:{e}.check the index number')
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError:{e}.The index is pointing at a 0 value")

# try:
#     l=[0,2,4,5,6,8,10]
#     i1=int(input("enter the first index"))
#     i2=int(input("enter the second index"))
#     print(l[i1]/l[i2])

# except IndexError as e:
#     print(f'IndexError:{e}.check the index number')
# except:
#     print(f"ZeroDivisionError:The index is pointing at a 0 value")


# 2.try and except and else block


# try:
#     n=int(input("enter a number"))
#     assert n%2==0
# except:
#     print("not an even number")
# else:
#     print(n/4)

# try-code where the error might occur
# except-what should be done if the error occurs
# else-what else should be done if the error doesnt occur



# 3.try and except and finally block
# n=int(input("enter the numerator"))
# try:
#     d=int(input("enter the denominator"))
#     print(n/d)
# except:
#     print("error:denominator cannot be a zero")
# finally:
#     print("division may have occured")
#finally block is executed if the exception is identified and handled
# finally block is executed if the exception doesnt occur also



#a program converts user input into an integer handle invalid inputs such as alphebitics or special characters
# a function compute a sqrt of a number handles negative inputs 
#a program performs arithmetics op on mixed types handle the type errors that are cost by incompactiable operations 



#custom exceptions

# class CustomException(Exception):
#     #raised when the value is less than 18
#     pass
# try:
#     n=int(input("enter the number"))
#     if n<18:
#         raise CustomException
#     else:
#         print("successful")
# except CustomException:
#     print("unsuccessful execution")


# n=int(input("enter the number"))
# if n<18:
#     raise CustomException
# else:
#     print("successful")




# class SalaryNotInRange(Exception):
#     #exception raised when salary is not in the range
#     def __init__(self,sal,msg="salary not in (5000,20000)"):
#         self.sal=sal
#         self.msg=msg
#         super().__init__(self.msg)

# try:
#     s=int(input("enter the salary"))
#     if not 5000<s<20000:
#         raise SalaryNotInRange(5)
#     else:
#         print("successfully added the details")
# except SalaryNotInRange as e:
#     print(f"SalaryNotInRange Error:{e}")



#raising built in exceptions


# try:
#     x=int(input("enter the numerator"))
#     y=int(input("enter the denominator"))
#     z=x/y
#     if z>10:
#         raise ValueError(z)
# except ValueError:
#     print(f"{z} is outside the given range")
# else:
#     print(f"{z} is within the given range")


# try:
#     x=int(input("enter the numerator"))
#     y=int(input("enter the denominator"))
    
#     if y==0:
#         raise Exception("cannot divide by zero")
# except Exception as e:
#     print(f"an error occured:{e}")

# try:
#     x="Hello"
#     y=int(x)
#     raise Exception("only numbers are allowed")
# except Exception as e:
#     print(f"value error:{e}")


#text file handling

#open the file
# f=open('file 1.txt','r')
# # Attributes of the file object
# print(type(f))
# print(f.mode)
# print(f.closed)
# print(f.name)


# #read a line of the file


# s=f.readline(10)
# print(s)
# s=f.readline()
# print(s)
# f.close()


# f=open('file 1.txt','r')
# #read multiple lines
# # s=f.readlines()
# print(s)
# print(type(s))
# # f.close()

# s1=f.readlines(5)
# print(s1)
# f.close()



# write a file

# with open('file2.txt','w') as f1:
#     c=f1.write("Hello,Welcome to the second File")
#     print(f"the file is written {c} number of characters")



#write multiple lines in the file

# lines=['First Line\n','Second Line\n','Third Line\n']
# f=open('File3.txt','w')
# f.writelines(lines)
# f.close()

# lines=['First Line','Second Line','Third Line']
# f=open('File4.txt','w')
# f.writelines(lines)
# f.close()


#append to a file
# f=open("File4.txt","a")
# f.write("\nThis is the new text added.\nThis will be written after")
# f.close()


#file pointer movement


# f=open('file 1.txt','r')
# # f.seek(10,0)##first parameter is the offset.second parameter is position from where the offset is calculated.it can be 0-begining of the file,1-current position and 2-end of the file
# # s=f.readline()
# # print(s)
# f.seek(5,0)
# s=f.readline()
# print(s)


#assume that u have a text file and do the following analysis.find out number of words in an even length,number of words that contain more than 2 vowels,number of words that start with ac capital letter.


# import json
# p='{"name":"Alpha","age":30}'
# p_dict=json.loads(p)

# print(type(p),type(p_dict))
# print(p_dict)
# print(p_dict["name"])

# with open('d1.json','r') as f:
#     p_json=json.load(f)
#     print(type(p_json))
#     print(p_json)
#assuming that u have a file called as emp.json that has name,dept,salary,display the highest salary and lowest salary.display the name of the employee that gets the lowest salary.display the avg salary per department





#xml files

# import statement

# import xml.etree.ElementTree as xml


# # Create the data 


# books=[
#     {'Title':"Pride",
#      'Author':'jane austen',
#      'Price':240,
#      'Category':'Fictional'},

#     {'Title':"The diary young girl",
#      'Author':'anne',
#      'Price':250,
#      'Category':'Non Fictional'},
#      {'Title':"XYZ",
#      'Author':'jane ',
#      'Price':222,
#      'Category':'Fictional'}
#     ]



# root=xml.Element("Books")

# type(root),print(root)
# for book in books:
#     book_ele=xml.Element("book")



# for book in books:
#     b_elements=xml.Element("Book")
#     root.append(b_elements)
#     b_elements.set('Category',book['Category'])
#     Title=xml.SubElement(b_elements,"Title")
#     Title.text=book['Title']
#     author=xml.SubElement(b_elements,"Author")
#     author.text=book['Author']
#     Price=xml.SubElement(b_elements,"Price")
#     Price.text=str(book['Price'])
# tree=xml.ElementTree(root)


# with open ("Books.xml","wb") as fh:
#     tree.write(fh)
# print("Books.xml file has been created")


# print(type(b_elements))
# print(type(Title))
# print(type(author))

# #read from xml file

# tree=xml.ElementTree(file="Books.xml")
# root=tree.getroot()
# books=[]

# print(type(tree))
# print(type(root))
# print(type(books))


# for book in root.findall('Book'):
#     book_data={}
#     book_data['Category']=book.get('Category')
#     for d in book:
#         book_data[d.tag]=d.text
#     books.append(book_data)
# print(type(book_data))
# print(type(d))
# print(type(book))
# print(books)


# # modification of an xml file 
# tree=xml.ElementTree(file='Books.xml')
# root=tree.getroot()
# #iterate over price
# for p_ele in root.iter('Price'):
#     p=int(p_ele.text)
#     p+=20
#     p_ele.text=str(p)

# # write the new data back into an xml file 
# with open('Books.xml','wb') as f:
#     tree.write(f)
# print("Price updated")

# write an xml file called as employees.xml it contains name age and salary of every employee once the xml file is created modify the exsisting salary by increasing by 5% update the file and show the changed salary


# import the module 

# import pandas as pd

# df=pd.read_csv('/Users/sumadhvabr/Documents/sales_r_csv.py')

# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.dtypes)
# print(df.head(2))
# print(df.tail(3))

# #CHeck for NAN values
# print(df.isna())
# print(df.isna().sum())

# #Check NAN in rows
# print(df.isna().any(axis=1))
# print(df.isna().any(axis=1).sum())

# #Check for not NAN values in columns
# print(df.notna())
# print(df.notna().sum())

# #Check for not NAN values in ROws

# print(df.notna().any(axis=1))
# print(df.notna().any(axis=1).sum())

# print(df.columns)

# #Clean the column names.
# df.columns=df.columns.str.strip()
# print(df.columns)

# print(df.head)
# print(df.tail)

# #Remove a quotes, commas from a particular column.


# #Convert column amount to str
# #Replace quotes
# #Replace comma
# #Extract the numeric digits.

# df['Amount']=(
#     df['Amount'].astype(str)
#     .str.replace('"','',regex=False)
#     .str.replace(',','',regex=False)
#     .str.extract(r'(\d+)',expand=False)
# )

# print(df.dtypes)

# #NAN values can be replaced with
# # 1. mean-mid value
# # 2. median- avg value
# # 3. mode- value with hightest freq

# #Convert column to Numeric

# df['Amount']=pd.to_numeric(df['Amount'],errors='coerce')
#     #first parameter - column that has to be converted
#     #errors = coerce -all non numeric chars will be converted as NAN
# print(df.dtypes)

# #Fill NaN Values with median

# df['Amount']=df['Amount'].fillna(df["Amount"].median())
# print(df['Amount'])

# print(df['Qty'])

# #Replace in Qty with mean
# df['Qty']=pd.to_numeric(df['Qty'],errors='coerce')

# print(df.dtypes)
# print(df['Qty'])

# #Fill Qty's NaN valuess with mean
# df['Qty']=df['Qty'].fillna(df['Qty'].mean())
# print(df['Qty'])

# print(df.head)

# #Drop Columns
# # 1. If the column contains too many NAN
# # 2. it is unwanted column


# df=df.dropna(axis=1, how='all')
# print(df.columns)

# df=df.dropna(axis=1, how='any')
# print(df.columns)

# # df=df.drop(columns=['Unnamed: 6'])

# df=df.iloc[:,:-1] #This works only for last columns.
# df=df.loc[:,~df.columns.str.contains('^Unnamed')] #works when the exact column name is not known
# print(df)



# print(df['Region'])


# #standardize text columns
# df['Region']=df['Region'].str.strip().str.lower()

# print(df['Region'])

# #Remove quotes in all cols
# df=df.apply(lambda c: c.astype(str).str.replace('"','',regex=False))
# print(df)

# #Convert the Region to numeric. All no numeric becpomes NAN
# #Create boolean mask. It is true when Region is 500 or 800. Replace all such rows as north
# df.loc[pd.to_numeric(df['Region'],errors='coerce').isin([500,800]),'Region']='north'
# print(df)


# df['Amount']=pd.to_numeric(df['Amount'],errors='coerce')
# hsales=df['Amount']>2000
# print(type(hsales))
# print(hsales)

# df_high=df[hsales]
# type(df_high)
# print(df_high)

# #to count number of records or rows in a dataframe
# print(len(df))
# print(len(df_high))

# # filtering based on multiple conditions
# c_amt=df['Amount']>2000
# c_reg=df['Region']=='south'
# print(type(c_amt))
# print(type(c_reg))

# df_t1=df[c_amt&c_reg]
# df_t2=df[c_amt|c_reg]
# df_t3=df[c_reg&c_amt]
# df_t4=df[c_reg&c_amt]
# print(len(df_t1)),print(len(df_t2))
# print(df_t1)

# df_sort=df.sort_values('Amount')
# print(df_sort)

# df_sort_desc=df.sort_values('Amount',ascending=False)
# print(df_sort_desc)

# df_s1=df.sort_values(['Region','Amount'])
# print(df_s1)


# df_s2=df.sort_values(["Region","Amount"],ascending=[True,False])
# # print(df_s2)create new. columns based n existing columns
# df['Tax']=df['Amount']*0.18
# print(df.columns)
# print(df)

# df["Total_Tax"]=df['Amount']+df["Tax"]
# print(df.columns)
# print(df)


# # count te value 
# print(df['Region'].value_counts())
# print(df['Amount'].value_counts())

# # summerize the data frame
# print(df['Amount'].describe())


# print(df['Region'].describe())
# print(df['Qty'].describe())
# print(df['Tax'].describe())
# print(df['Total_Tax'].describe())

# #grouping the data
# grp_reg=df.groupby('Region')
# print(type(grp_reg))
# print(len(grp_reg))
# print(grp_reg)


# # view the group data 

# print(grp_reg.groups.keys())

# # view the row index that belongs to each group
# print(grp_reg.groups)

# #view specific group

# print(grp_reg.get_group('north'))

# #loop through all the groups 
# for n,g in grp_reg:
#     print(f'Group:(n)')
#     print(g)


# #grouping based on multiple columns

# grp_mul=df.groupby(['Region','Product'])
# print(grp_mul.groups)

# #sum of the amount of each region 
# #aggregation

# sales_reg=grp_reg['Amount'].sum()
# print(sales_reg)
# #multiple aggregration

# region_summary=grp_reg['Amount'].agg(['sum','mean','count'])
# print(region_summary)

# #custom aggregration 

# summary=df.groupby('Region').agg(
#     Total_Amt=('Amount','sum'),
#     Avg_Amt=('Amount','mean'),
#     Avg_tax=('Tax','mean'),
#     unique_Product=('Product','nunique')    
# )
# print(type(summary))
# print(summary)




# import csv

# with open("sales_r_csv.py", "r") as f:
#     reader = csv.DictReader(f)
#     data = list(reader)

# with open("student_summary.csv", "w", newline="") as f:
#     fieldnames = ["RollNo", "Name", "AverageMarks", "Result"]
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()

#     for row in data:
#         avg = float(row["Marks"])
#         result = "Pass" if avg >= 40 else "Fail"
#         writer.writerow({
#             "RollNo": row["RollNo"],
#             "Name": row["Name"],
#             "AverageMarks": avg,
#             "Result": result
#         })





# import csv

# sales = {}

# with open("daily_sales.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         region = row["Region"]
#         amount = float(row["Amount"])
#         sales[region] = sales.get(region, 0) + amount

# with open("region_sales.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Region", "TotalSales"])
#     for r, t in sales.items():
#         if t >= 50000:
#             writer.writerow([r, t])




# import pandas as pd

# df = pd.read_excel("attendance.xlsx")

# df["AttendancePercentage"] = (df["DaysPresent"] / df["TotalDays"]) * 100
# df["AttendanceStatus"] = df["AttendancePercentage"].apply(
#     lambda x: "Shortage" if x < 75 else "OK"
# )

# df.to_excel("attendance_report.xlsx", index=False)








# import pandas as pd

# df = pd.read_excel("emp_data.xlsx")

# df["HRA"] = df["BasicSalary"] * 0.10
# df["DA"] = df["BasicSalary"] * 0.18
# df["GrossSalary"] = df["BasicSalary"] + df["HRA"] + df["DA"]

# df[["EmpID", "Name", "GrossSalary"]].to_excel("emp_salary.xlsx", index=False)










# import csv

# with open("inventory.csv", "r") as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# with open("reorder_list.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["ProductID", "ProductName", "Stock"])

#     for r in rows:
#         if int(r["Stock"]) < int(r["ReorderLevel"]):
#             writer.writerow([r["ProductID"], r["ProductName"], r["Stock"]])










# import csv

# marks = {}

# for file in ["theory_marks.csv", "lab_marks.csv"]:
#     with open(file, "r") as f:
#         reader = csv.DictReader(f)
#         for r in reader:
#             roll = r["RollNo"]
#             marks[roll] = marks.get(roll, 0) + int(r["Marks"])

# with open("final_result.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["RollNo", "TotalMarks", "Result"])
#     for r, t in marks.items():
#         writer.writerow([r, t, "Pass" if t >= 40 else "Fail"])





# import pandas as pd

# df = pd.read_excel("expenses.xlsx")

# summary = df.groupby("Category")["Amount"].sum().reset_index()
# summary.to_excel("monthly_summary.xlsx", index=False)




# import pandas as pd

# df = pd.read_csv("bus_pass_requests.csv")

# def fare(km):
#     if km <= 5:
#         return 400
#     elif km <= 10:
#         return 650
#     else:
#         return 900

# df["Fare"] = df["DistanceKm"].apply(fare)
# df["Status"] = "Pending"

# df.to_excel("bus_pass_status.xlsx", index=False)
# df[["ReqID", "StudentID", "Fare"]].to_csv("bus_pass_fare_list.csv", index=False)



# import pandas as pd

# df = pd.read_excel("returns.xlsx")

# valid = df[
#     (df["RefundMode"].isin(["UPI", "CARD", "WALLET"])) &
#     (df["Amount"] > 0)
# ]

# invalid = df.drop(valid.index)
# invalid["ErrorReason"] = "Invalid refund mode or amount"

# valid.to_csv("returns_clean.csv", index=False)
# invalid.to_excel("returns_error_log.xlsx", index=False)



# import csv

# def calc(units):
#     if units <= 100:
#         return units * 4
#     elif units <= 200:
#         return 100*4 + (units-100)*6
#     else:
#         return 100*4 + 100*6 + (units-200)*8

# with open("meter_readings.csv") as f:
#     r = csv.reader(f)
#     next(r)

#     bills = open("bills.csv", "w", newline="")
#     errors = open("billing_errors.csv", "w", newline="")

#     bw = csv.writer(bills)
#     ew = csv.writer(errors)

#     bw.writerow(["ConsumerID", "Name", "Units", "Bill"])
#     ew.writerow(["ConsumerID", "Error"])

#     for row in r:
#         units = int(row[3]) - int(row[2])
#         if units < 0:
#             ew.writerow([row[0], "Invalid reading"])
#         else:
#             bw.writerow([row[0], row[1], units, calc(units)])

#     bills.close()
#     errors.close()

#pd dataframe

# import pandas as pd

# sd=pd.read_csv('sales_demo.csv')
# pr=pd.read_csv('products_demo.csv')

# print(type(sd), type(pr))

# print(sd.shape)

# print(pr.shape)

# print(sd.columns)

# print(pr.columns)

# print(pr['ProductID'].nunique())
# print(len(pr))

# #merge using inner join
# df=pd.merge(sd,pr, on='ProductID', how='inner')
# print(df.shape)

# m_inner1=pd.merge(sd,pr, on='ProductID', how='inner')
# print(m_inner1.shape)
# m_left=pd.merge(sd,pr,on="ProductID",how="left")
# m_left1=pd.merge(pr,sd,on="ProductID",how="left")
# print(m_left)
# m_right=pd.merge(sd,pr,on="ProductID",how="right")
# m_right1=pd.merge(pr,sd,on="ProductID",how="right")
# print(m_right.shape,m_right.shape)
# print(m_right.shape,m_right1.shape)
# print(m_right)
# m_outer=pd.merge(sd,pr,on="ProductID",how="outer")
# m_outer1=pd.merge(pr,sd,on="ProductID",how="outer")
# print(m_outer.shape,m_outer1.shape) 
# print(m_outer)

#combine two df vertically
# import pandas as pd
# s1=pd.read_csv('sales.csv')
# s2=pd.read_csv('sales_q2.csv')

# print(s1.shape,s2.shape)
# print(s1.columns)
# print(s2.columns)
# s_all=pd.concat([s1,s2],ignore_index=True)
# s_all1=pd.concat([s1,s2])
# print(s1.shape,s2.shape,s_all.shape,s_all1.shape)
# print(s_all.head)
# print(s_all1.head)
# # ignor_index=True sets the index numbers from 0 continously

# #export the data frame
# s_all.to_csv('sales_all.csv',index=False)
# s_all.to_csv('sales_all_1.csv',index=True)
# s_all1.to_excel('sales_all_1.xlsx',index=False)
# # s_all1.to_json('sales_all_1.json')
# s_all.to_html('sales_all.html')
# s_all.to_excel('sales_all_1.xlsx')

#simulation of sensor data

# import random
# import time
# for i in range(10):

#     t_c=25+random.uniform(-2,2)
#     print(f'reading {i+1}:{t_c:2f} C')
#     time.sleep(1)
#     #pause the data for 1sec


#simulate a virtual sensor
# import random as r
# import time
# import csv


# with open('sensor_read.csv','w',newline='') as f:
#     writer=csv.writer(f)
#     writer.writerow(['Timestamp','Temperature'])
#     for i in range(10):
#         ts=time.time()
#         #current time is captured in sec from unix epoch time
#         #float value
#         t_c=25+r.uniform(2,-2)
#         #random temperature is generated
#         #random uniform number. b/w -2 and 2 is generated
#         #and gets added to 25
#         writer.writerow([ts,f'{t_c:2f}'])
#         print(ts,t_c)
#         time.sleep(0.1)




# Visulaizarion of the readings
# interpret the data and visualize
# import pandas as pd
# import matplotlib.pyplot as plt

# #create the dataframe from the readings
# df=pd.read_csv('sensor_read.csv')
# print(df.shape)


# #convert the string to a numeric data
# df['Timestamp']=pd.to_numeric(df['Timestamp'], errors='coerce')
# df['Temperature']=pd.to_numeric(df['Temperature'], errors='coerce')
# print(df.dtypes)
# print(df.head)
# print(plt.figure)
# plt.plot(df['Timestamp'],df['Temperature'])
# plt.xlabel('Time')
# plt.ylabel('Temperature (c)')
# plt.title('Raw sensor data')
# plt.show()
# plt.xticks(rotation=45)
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import csv

# df = pd.read_csv('sensor_read.csv')
# print(df.shape)

# # Convert Timestamp
# df['Timestamp'] = pd.to_numeric(df['Timestamp'], errors='coerce')
# df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

# # Convert Temperature values
# df['Value'] = pd.to_numeric(df['Temperature'], errors='coerce')

# # Smooth data
# df['value_Smooth'] = df['Value'].rolling(window=5, min_periods=1).mean()

# print(df.head())


# # #plotting of smoothened values 
# # import matplotlib.pyplot as plt
# # plt.figure()
# # plt.plot(df['Timestamp'],df['Value'],label='Raw',alpha=0.5)
# # plt.plot(df['Timestamp'],df['value_Smooth'], label='Smoothened')
# # plt.xlabel=('Time')
# # plt.ylabel=('Temperature (c)')
# # plt.title('Raw vs Smoothened Sensor Data')
# # plt.legend()
# # plt.xticks(rotation=45)
# # plt.tight_layout()
# # plt.show()

# #mean of temperature Readings
# mid_index=len(df)//2

# first_half_mean=df['value_Smooth'].iloc[:mid_index].mean()
# second_half_mean=df['value_Smooth'].iloc[mid_index:].mean()
# print(f'Mean of first half:{first_half_mean}')
# print(f'Mean of second half:{second_half_mean}')


#pickling and unpickling
# import pickle as p
# # numberic data type 
# a=10;b=10.5;c=10-9j
# with open('numeric.pkl','wb')as f:
#     #use wb since the data has to be written in byte stream
#     p.dump(a,f)
#     p.dump(b,f)
#     p.dump(c,f)


# with open('numeric.pkl','rb')as f:
#     data=p.load(f)
# print(f'unpickled data is {data}')

# # list 
# l1=['apple',23,56.78,'Banana',89-9j,['a','b','c']]
# with open('list.pkl','wb')as f:
#     p.dump(l1,f)
# with open('list.pkl','rb')as f:
#     p_l1=p.load(f)
# print(f'Unpickled list p{p_l1}')
# print(f'Type of p_l1 is  {type(p_l1)}')



# # dictionary
# import pickle as p
# d1 = {
#     'name': 'Shridhar',
#     'age': 22,
#     'course': 'MCA',
#     'marks': [85, 90, 88],
#     'complex_no': 5 + 7j
# }

# # write (pickle)
# with open('dict1.pkl', 'wb') as f:
#     p.dump(d1, f)

# # read (unpickle)
# with open('dict1.pkl', 'rb') as f:
#     p_d1 = p.load(f)

# print(f'Unpickled dictionary is {p_d1}')

# custom object
# import pickle as p
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __repr__(self):
#         return f'Person(name:{self.name},age:{self.age})'
# p1=Person('alpha',24)
# print(p1)

# with open('obj.pkl','wb')as f:
#     p.dump(p1,f)
# with open('obj.pkl','rb')as f:
#     p_obj=p.load(f)
# print(f'Unpickled object is {p_obj}')


# #multiple objects

# l1=[1,2,3,'apple',[2,3,4],89+9j]
# d1={1:2,3:4}
# s1="Hello"
# with open ('all.pkl','wb')as f:
#     p.dump(l1,f)
#     p.dump(d1,f)
#     p.dump(s1,f)
# print(l1)
# print(d1)
# print(s1)


# #functions

# def greet(name):
#     return f'Hello {name}'

# with open('func.pkl','wb')as f:
#     p.dump(greet,f)
# with open('func.pkl','rb')as f:
#     p_f=p.load(f)
# print(p_f('Alpha'))
# print(p_f('beta'))


# #data frames

# import pandas as pd

# data={'Name':['Alpha','Beta','Gama'],
#       'Age':[20,30,40],
#       'City':['Banglore','chennai','delhi']}
# df=pd.DataFrame(data)
# print(df)
# print(type(df))

# df.to_pickle('df.pkl')
# p_df=pd.read_pickle('df.pkl')
# print(p_df)
# print(type(p_df))

# # Loads and dumps
# a=10
# p_a=p.dumps(a)
# print(p_a)
# print(type(p_a))
# print(p.loads(p_a))
# b=45.7;c=9+1j;d='hello'
# p_b=p.dumps(b); p_c=p.dumps(c); p_d=p.dumps(d)
# print(f'Deseralised data is {p.loads(p_b)},{p.loads(p_c)},{p.loads(p_d)}')


# ===============================
# IMPORT LIBRARIES
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("\n--- WATER FLOW SENSOR OUTPUT ---\n")

# ===============================
# TIME SERIES CREATION
# ===============================
seconds = 48 * 60 * 60
timestamps = pd.date_range("2025-01-01", periods=seconds, freq="s")

# ===============================
# FLOW INITIALIZATION
# ===============================
flow_values = np.zeros(seconds)

# ===============================
# NORMAL WATER USAGE EVENTS
# ===============================
for i in range(40):
    idx = np.random.randint(0, seconds - 600)
    length = np.random.randint(30, 600)
    flow_values[idx:idx + length] = np.random.uniform(5, 15)

# ===============================
# SLOW LEAK SIMULATION (6 HOURS)
# ===============================
leak_begin = 10 * 60 * 60
leak_end = leak_begin + (6 * 60 * 60)
flow_values[leak_begin:leak_end] += 0.5

# ===============================
# SENSOR NOISE
# ===============================
random_noise = np.random.normal(0, 0.2, seconds)
flow_values = np.where(flow_values > 0, flow_values + random_noise, 0)
flow_values = np.clip(flow_values, 0, None)

# ===============================
# DATAFRAME CREATION
# ===============================
water_df = pd.DataFrame({
    "timestamp": timestamps,
    "flow_lpm": flow_values
})

# ===============================
# EVENT DETECTION
# ===============================
water_df["usage_event"] = water_df["flow_lpm"] > 1

# ===============================
# HOURLY WATER CONSUMPTION (LITERS)
# ===============================
hourly_consumption = (
    water_df
    .resample("h", on="timestamp")["flow_lpm"]
    .sum() / 60
)

# ===============================
# LEAK IDENTIFICATION
# ===============================
water_df["leak_detected"] = (
    (water_df["flow_lpm"] > 0.2) &
    (water_df["flow_lpm"] < 1)
)

# ===============================
# USAGE TYPE CLASSIFICATION
# ===============================
water_df["usage_type"] = "Idle"

water_df.loc[water_df["flow_lpm"] > 10, "usage_type"] = "High"
water_df.loc[water_df["flow_lpm"].between(3, 10), "usage_type"] = "Medium"
water_df.loc[water_df["flow_lpm"].between(0.2, 3), "usage_type"] = "Low"

# ===============================
# LEAKAGE IMPACT REPORT
# ===============================
leak_loss = water_df.loc[
    water_df["leak_detected"], "flow_lpm"
].sum() / 60

print("Total water used per hour (first 5 hours):")
print(hourly_consumption.head())

print("\nTotal water lost due to leakage:", round(leak_loss, 2), "litres")

# ===============================
# VISUALIZATION
# ===============================
plt.figure()
(
    water_df
    .set_index("timestamp")["flow_lpm"]
    .resample("h")
    .mean()
    .plot()
)
plt.title("Hourly Average Water Flow")
plt.xlabel("Time")
plt.ylabel("Flow (LPM)")
plt.show()

