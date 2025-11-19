#constrcutor  :  called when the object is created

"""
type  of constructor  :

1. default  constructor  
2. parameterized constructor
3. non-parameterized constructor

"""

# 1. default  constructor  :

"""
class person :
    def __init__(self):  # __init__ ==> constructor , special  method 
        print("default constructor")
        print("my name is  krish.")  # self ==> keyword  ==>current object 
        
p=person() # p object ==> person 
"""

# 2. non-parameterized constructor


"""class person : 
    def __init__(self):
        self.name ="krish"
        self.age =21

    def show(self):
        print(f"name is  :{self.name} , age is  :{self.age}")
p=person()
p.show()  # func 
print(p.name)  # access data member though object (p)   ==> person class
print(p.age)
"""

# 3. parameterized constructor

"""class person : 
    def __init__(self,name,age):
        self.name =name 
        self.age =age 
    
    def show(self):
        print(f"name is  :{self.name} , age is  :{self.age}")

p=person("krish",21)
p1=person("krishna",34)
p.show()
p1.show()

"""

#

class person : 
    def __init__(self,name,age):
        self.name =name
        self.age =age
    
    def __init__(self):
        self.name ="krish"
        self.age =21
        
    def show(self):
        print(f"name is  :{self.name} , age is  :{self.age}")
        
    def show(self):
        print("person information")
        print("name is  :",self.name)
        print("age is  :",self.age)
        
p=person()
p.show()

        