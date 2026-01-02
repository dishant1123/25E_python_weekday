"""
class object : 

type  : 
1.public  : accessible from anywhere
2.private : witin the class
3. protected : accessible from the class and its subclasses(inheritance)
"""
# public : 
"""
class person :  # person  ==>class name 
    name ="krishna"
    age =21       # name  age  ==> data members   ==> public 

    def show(self):  # self ==> key word ==> current object  ==> member access 
        print("name is  : ",self.name)
        print("age is  : ",self.age)
    
p=person()  # p ==> object 
# print("name is  : ",p.name)  # object though  ==> print 
# print("age is  : ",p.age)
p.show()
p.name ='krish'
p.age=20 
# print("name is  : ",p.name)
# print("age is  : ",p.age)
p.show()
"""

# private  : 
"""class employees : 
    __name="aashta"
    __age=19 

    def show(self):
        print("name is  : ",self.__name)
        print("age is  : ",self.__age)
e=employees()
# print("name is  : ",e.__name)
# print("age is  : ",e.__age)  # __name  __age  ==> private   not  poss bcz of  private . 
e.show()
e.__name="krishna"
e.__age=21
e.show()
"""

# protected : 
"""
class employees :
    _name ="aashta"
    _salary=90000 
    
class manger(employees):
    def show(self):
        print("name is  : ",self._name)
        print("salary is  : ",self._salary)
    
m=manger()
m.show()
"""
# constructor  : 
"""
1. automatically called when an object is created
2. can be called explicitly
3. can be overloaded
4. no return value 

types : 
1. default constructor
2. non  parameterized constructor
3. parameterized constructor
4. overloaded constructor
"""
# default constructor :
"""
class person : 
    def __init__(self):  #__init__ ==> constructor / special  method 
        print("my  name is krishna")
        print("live in ahm.")
p=person()    
"""

# non parameterized constructor :

"""class person : 
    def __init__(self):
        self.name ="krishna"
        self.city ="ahm"
        print("non parameterized constructor")
        
    def show(self):
        print("name is  : ",self.name)
        print("city is  : ",self.city)
p=person()
p.show()
print("name is  : ",p.name)
print("city is  : ",p.city)
"""

# parameterized constructor :

"""
class person : 
    def __init__(self,name, city):
        self.name =name 
        self.city =city
    def show(self):
        print("name is  : ",self.name)
        print("city is  : ",self.city)
p=person("krishna","ahm")
p.show()
print("name is  : ",p.name)
print("city is  : ",p.city)
"""