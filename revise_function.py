# function  : 
"""
type  : 

1. no arg  no return
2. no arg  with return
3. with arg  no return
4. with arg  with return
"""
# 1. no arg  no return
"""
def add():  # def ==> define   add ==> function name
    a=int(input("enter a number 1:"))
    b=int(input("enter b number 2:"))     # function ==> function intialization
    c=a+b
    print(c)
add()
print("meet")
add()
"""
#2. with arg  no return  

"""def add(a,b):  # def ==> define   add ==> function name
    c=a+b
    print(c)
# add("meet","patel")
# add("vatsal","joshi")
a=int(input("enter a number 1:"))
b=int(input("enter b number 2:"))
add(a,b)
"""

# 3. no arg  with return

"""
def add():  # def ==> define   add ==> function name
    a=int(input("enter a number 1:"))
    b=int(input("enter b number 2:"))     # function ==> function intialization
    c=a+b
    return c 
print(add())
"""

# 4. with arg  with return

"""def add(a,b):  # def ==> define   add ==> function name
    
    c=a+b
    return c 
a=int(input("enter a number 1:"))
b=int(input("enter b number 2:"))     
print(add(a,b))
"""

# *args  : only take a number of arguments 

"""
def add(*args):
    return sum(args)  # sum ==> built in function  
print(add(1,2,22,344,55,6,78,899,90,89.90,-90))
"""

# without using built  in function : 

"""def add(*x):
    sum =0 
    for i in x:
        sum =sum +i 
    print(sum)
add(1,2,22,344,55,6,78,899,90,89.90,-90)
"""

# **kwargs  :  take any number of keyword arguments

"""def d1(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} : {j}")
        
d1(name="vatsal",age=20,clg="LJ",city="amreli")
"""

# local variable  : 

"""
def local():
    x=100 
    print(x)  # local variable
local()
# print(x) # you can't access local variable outside the function
"""

# global variable  :
"""x=100
def g1():
    print(x)
    print("krishna")
g1()
print(x)  # global variable  ==> access outside the function  also inside the function
"""

# global  variable  modify :

"""x=100
def g2():
    global x  # you can modify global varibale  using  global  keyword
    x=900 
    print(x)
g2()
print(x)  
"""

# employess management system :
"""
1. add employee
2. delete employee
3. update employee
4. view employee / display
"""

d1={}

def add_emp():
    id =int(input("enter employee id:"))
    name =input("enter employee name:")
    salary=int(input("enter employee salary:"))
    # id =[name , salary]
    d1[id] =[name,salary]

def update_emp():
    id =int(input("enter the  id you want to update :"))
    if id in d1:
        name =input("enter employee name:")
        salary=int(input("enter employee salary:"))
        d1[id]=[name,salary]
    else :
        print("id not found")

def delete_emp():
    id =int(input("enter the  id you want to delete :"))
    if id in d1:
        del d1[id]
    else :
        print("id not found")

add_emp()
add_emp()
print("before update : ")
print(d1)

update_emp()
print("after update : ")
print(d1)

delete_emp()
print("after delete : ")
print(d1)
"""
id   name       salary 
1    krishna    90000
2    vatsal     99999

display()

menu driven  :
1.add
2.delete
3.update
4.display
5.exit

"""