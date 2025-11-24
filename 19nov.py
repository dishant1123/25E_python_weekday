# inheritance : to inherit  another  class propertries  . 
"""
1. single level inheritance
2. multi level inheritance
3. multiple inheritance
4. hierarchical inheritance
5.hybrid inheritance
"""

# single  level  inheritance  :

"""class a :  # base class 
    def show(self):
        print("class ==> a")

class b(a):  # derived class   ==> 
    def display(self): 
        print("class ==> b")

B =b()
B.show()   # a method 
B.display() # b method
"""

# constructor  : 
"""class person :
    def __init__(self):
        self.name ="krish"
        self.age =20
    def show(self):
        print("name  is  :",self.name)
        print("age  is  :",self.age)
       
class student(person):
    def __init__(self):
        # person.__init__(self)  # calling parent class constructor
        super().__init__()  # calling parent class constructor
        self.city ="ahmedabad"
    def show(self):
        super().show()# self.show()
        print("city  is  :",self.city)

s=student()
s.show()
# print("name  is  : ",s.name)
# print("age  is  : ",s.age)
# print("city  is  : ",s.city)
s.name ="vatsal"
s.age =19 
s.city ="amreli"
print("after  updat values :\n")
s.show()
"""

# multiple inheritance  : 
"""
a class can inherit from  more than one parent class 

class a : 
class b: 
class c(a,b):
"""

class grandparent :
    def __init__(self):
        self.name = "suresh"
        self.age = 70 
class parent :
    def __init__(self):
        self.father = "mahesh"
        self.mother ="meena"
class child(grandparent,parent):
    def __init__(self,child_name):
        grandparent.__init__(self)  # gp const call 
        parent.__init__(self)  # p const call
        self.child_name = child_name
    
    def show(self):
        print("FAMILY DETAILS")
        print("grandparent name  is  :",self.name)
        print("grandparent age  is  :",self.age)
        print("parent father  is  :",self.father)
        print("parent mother  is  :",self.mother)
        print("child name  is  :",self.child_name)

c=child("vedika")
c.show()

# MRO  :  method resolution order
