"""
bank using  class object : 
"""

"""class bank  : 
    def __init__(self,name,acnumber):
        self.balance =25000 
        self.name = name
        self.acnumber =acnumber 
        
    def deposit(self,amt):
        self.balance +=amt 
        print(f"Deposited {amt} to {self.name}") 
        
    def withdraw(self,amt):   # bal =28000   with  ==>23000 
        if(self.balance -amt >= 10000 ) : #   28000 - 23000 >= 10000
            self.balance -=amt 
            print(f"Withdrawed {amt} from {self.name}")
        else:
            print("min balance is 10000")
    
    def check_balance (self):
        print("final  balance  is  : ",self.balance) 

b=bank("raj",1234567890)
b.deposit(10000)
b.withdraw(2500)
b.check_balance() 
"""
"""
task  :1  pin generated   
    enter your pin  : 
    wrong  min   ==> max attempt   ==> 3   exit  
task  :2   menu driven  
    choice  : 
        1. deposit  
        2. withdraw
        3. check balance
        4. exit
"""

# oop : 
"""
1. inheritance  
2. polymorphism  
3. encapsulation  
4. abstraction
"""

# 1. inheritance  : single  inheritance   ==> to  inherit  properties  and  methods  from  a  parent  class.

# ex 1 : 
"""
class student : 
    def __init__(self):
        self.name = "krishna"
        self.age =20 
    
class teacher(student):
    def display(self):
        print(f"name  is  {self.name}  age  is  {self.age}")

t=teacher()
t.display()
"""

# ex :2 

class employee :
    def __init__(self,name,salary):
        self.name =name 
        self.salary =salary

class manager(employee):
    def __init__(self, name, salary,position):
        super().__init__(name,salary)  # base class constuctor
        # employee.__init__(self,name,salary)
        self.position =position
    
    def show(self):
        print("emp  details  :  ")
        print("name is  : ",self.name)
        print("salary is  : ",self.salary)
        print("manager position is  : ",self.position)
        
m=manager("raj",90000,"sr.accontant")
m.show()

"""
Implement the following hierarchy . The Book function has name, n (number of authors), authors (list of authors), publisher, ISBN, and year as its data members and the derived class has course as its data member. The derived class 
method overrides (extends) the methods of the base class. 

hint  : 
book 
    name , n ,publisher , isbn year 
    
    function  ==, show()

textbook(book)
    course 
    function  ==> show ()  class ==> book.show()
    
ex : 
    name = abc 
    n  =3 
    authors = ["raj","krishna","harry"]
     
"""