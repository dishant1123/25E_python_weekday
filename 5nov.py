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