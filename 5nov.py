# constructor  : called when the object is created
"""
1. default constructor  : 
2. parameterized constructor :
3. non-parameterized constructor :
"""
 
# 1 . default  constructor  : 

"""
class person : 
    def __init__(self): # special  method , constructor  
        print("default constructor")
        
p=person()  # when object is  created , constructor  is called
 
"""

#2 : non-parameterized constructor
"""
class employees :
    def __init__(self):   # name  salary  ==> function  
        self.name = "vatsal"
        self.salary = 100000 
        print("non-parameterized constructor")
    
    def display(self):  # display  name  salary
        print(f"name  : {self.name} , salary  : {self.salary}")
e=employees()
print(e.name)
e.display()
"""

# 3 : parameterized constructor

"""class employees :
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def show(self):
        print(f"name  : {self.name} , age  : {self.age} , salary  : {self.salary}")

e=employees("vatsal",25,100000)
e2=employees("krish",24,1000000)
print("name is  :",e.name)
print("age is  :",e.age)
print("salary is  :",e.salary)
e.show()  # function  show  is called
e2.show()
"""

# 4 :

"""class person : 
    def __init__(self):
        print("default constructor")
    
    def __init__(self):
        print("parameterized constructor")
        self.name="vatsal"
        self.age=25

    def display(self):
        print(f"name is  : {self.name} , age is  : {self.age}")
    
    def display(self):
        print("default const. function call")
p=person()
p.display()
"""

# bank  : 

"""class bank : 
    def __init__(self,name,bank_name,account_number):
        self.name=name
        self.bank_name=bank_name
        self.account_number=account_number
        self.balance=25000
    
    def deposit(self,amount):  # deposit ==>5K  ==bal =30000
        self.balance =  self.balance +amount 
        print(f"deposit :{amount}, balance is :{self.balance}")
    
    def withdraw(self,amount):  # min ==>10000 
        if self.balance -amount >=10000 :   # 30000 -2500 >=10000 
            self.balance = self.balance -amount
            print(f"withdraw :{amount}, balance is :{self.balance}")
        else :
            print("Insufficient funds and also maintaining the minimum requirement")
            
    def check_balance(self):
        print(f"final balance is :{self.balance}")
        
b=bank("krish","HDFC",7801200014352)
print("Your balance is :",b.balance)
b.deposit(5000)
b.withdraw(2500)
b.check_balance()
"""
# atm  :  acc num   ==>pin 
"""
1. pin  user  ==> ask user to enter the  pin  ==> create 1211 accnumber create  

option 1 verfiy re enter  your pin  ==> 1211  accnumber  ==>   match  ==> exit 
option 2 : pin accnumber  ==> fix  

menu  driven : 

1. create  user name  , password    ==> 25000 balance 

login  : username  password   ==> deposit with check  
"""
