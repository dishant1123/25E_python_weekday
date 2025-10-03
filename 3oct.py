# function  : 
"""
1. no arg  no return  
2. no arg  with return
3. with arg  no return
4. with arg  with return
"""
# 1. no arg  no return

"""def addition():  # def ==> define   addition ==> function name
    a=int(input("enter a number:"))
    b=int(input("enter b number  :"))     # function ==> function intialization
    c=a+b
    print(c)
addition()
addition()
print("meet")
addition()
"""

# 2. with arg  no  return

"""def addition(a,b): 
    c =a+b 
    print(c)

a=int(input("enter a number:"))
b=int(input("enter b number  :"))     
addition(a,b)
"""

# 3. no arg  with return

"""
def add():
    a=int(input("enter a number:"))
    b=int(input("enter b number  :"))     
    c=a+b 
    return c 
print(add())
"""
# 4. with arg  with return

"""
def add(a,b):
    c=a+b
    return c 
print(add(12,15))
"""

# *args  : only take a number of arguments

"""def add(*args):
    return sum(args)  # sum ==> built in function  

print(add(1,3,5,12,45,67,88,55,12,89.78))
"""

# using  loop  :
"""def d(*x):
    sum =0
    for i in x:
        sum +=i 
    print(sum)
# d(1,3,5,12,45,67,88,55,12,89.78)

n=int(input("enter number:"))
l2=[]   
for i in range(n):
    ele=int(input("enter number:"))
    l2.append(ele)
d(*l2)
"""

# **kwargs  :  take any number of keyword arguments

"""
def d(**kwargs):
    for i , j in kwargs.items():
        print(f"{i} : {j}")

d(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10)
"""

# local variable  : 

"""def local():
    a=10 
    print(a)
local()
print(a)  # you can't access local variable outside the function
"""
# global variable  :

"""a=10 
def global_var():
    print(a)
global_var()
print(a)  # you can access global variable outside the function alsp inside function 
"""
# modify global variable  :

"""a=100 
def global_var():
    global a   # modify ==> global 
    a=200 
    print(a)
global_var()
print(a)
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
    name=input("enter employee name:")
    salary=int(input("enter employee salary:")) 
    d1[id]=[name,salary]

def emp_update():
    id=int(input("enter id you want  to update : "))
    if id in d1:
        name=input("enter new name:")
        salary=int(input("enter new salary:"))
        d1[id]=[name,salary]
    else :
        print("id not found")

def delete_emp():
    id=int(input("enter id you want  to update : "))
    if id in d1:
        del d1[id]
    else :
        print("id not found")

add_emp()
add_emp()
print("before  update : ")
print(d1)

emp_update()
print("after update : ")
print(d1)

delete_emp()
print("after delete : ")
print(d1)
"""
key  [name , salary]
id   name  salary 
1    ved    99000 
2    harix  98000 

display () 

menu driven  : 

1. add
2. delete
3. update
4. display
5. exit 
user choice :  
"""
