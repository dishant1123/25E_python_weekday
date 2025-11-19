# inheritance : to inherit  another  class propertries  . 
"""
1. single level inheritance
2. multiple level inheritance
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
class person :
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
