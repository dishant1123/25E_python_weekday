# class object : 

"""
1. public  
2. private 
3. protected
"""

# public : 
"""
class person :   # person class name 
    name ="krish"  # name age  -==> public  member  / data member  
    age =21 
    
    def show(self):  # self ==> keyword ==> current object + member access ==>self 
        print("name is :",self.name)
        print("age is :",self.age)
        
p=person()   # p object 
print("before  change :")
p.show()
# print("name is  :",p.name)  
# print("age is  :",p.age)
print("after  change :")
p.name ="harpal"
p.age=22 
p.show()
"""

# private :

"""class student :
    __name ="krish"  # __name,__age ==> private member
    __age =21       
    
    def show(self):
        print("name is :",self.__name)
        print("age is :",self.__age)
s=student()
s.show()
print("name is  : ",s.__name)
print("age is  : ",s.__age) # not accessible bcz of private member
s.__name ="harpal"
s.__age=22
s.show()  # note : not change  in original values and also  not give error print only static value. 
"""

# protected :

"""class person : 
    _name ="krish"  # _name,__age ==> protected member
    _age=21

class student(person):
    def show(self):
        print("name is :",self._name)
        print("age is :",self._age)

s=student()
s.show()
"""

# constructor : automatically called when object is created

"""
1.default constructor
2.non parameter constructor
3.parameter constructor
4.constructor overloading
"""

#1 :default constructor

"""
class student :
    def __init__(self):  #__init__ ==> special method / constructor 
        print("my name is krish.")
        print("live in ahm.")
s=student()
"""

#2 : non parameter constructor

"""class student :
    def __init__(self):
        self.name ="krish"
        self.age =21
        print("my hobby is  playing cricket.")
    def show(self):
        print("name is :",self.name)
        print("age is :",self.age)
s=student()
print("name is :",s.name)
print("age is :",s.age)
s.show()
"""

# 3 : parameter constructor

"""class person : 
    def __init__(self,name,age):
        self.name =name 
        self.age =age

    def show(self):
        print("name is :",self.name)
        print("age is :",self.age)

p=person("krish",21)
p1=person("harpal",22)
p.show()
p1.show()
"""

# 4 : constructor overloading

class person : 
    def __init__(self):
        print("my name is krish.")
        print("live in ahm.")
    
    def __init__(self):
        self.name ="krish"
        self.age =21
        print("my hobby is  playing cricket.")
        
    def show(self):
        print("name is :",self.name)
        print("age is :",self.age)

p=person()
p.show()
    