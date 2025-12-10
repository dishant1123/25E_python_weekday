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

"""class person : 
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
"""

# oop 4 pillar :
"""
1. inheritance
2. encapsulation
3. polymorphism
4. abstraction
"""

# inheritance : to inherit from a another class property and method. 
"""
1.single inheritance
2.multiple inheritance
3.multi level inheritance
4.hierarchical inheritance
5.hybrid inheritance
"""

#1 : single inheritance

"""class vehicle :
    def __init__(self):
        self.type ="four wheeler"
        self.seating_cap=5

class car(vehicle):
    def __init__(self,model,color):
        # super().__init__()  # base class constructor called 
        vehicle.__init__(self)  # 
        self.model=model
        self.color=color
    
    def show(self):
        print("vehicle type is :",self.type)
        print("seating cap is :",self.seating_cap)
        print("model is :",self.model)
        print("color is :",self.color)
        
c=car("Audi-A4","red")
c.show()
"""

# 2 : multiple inheritance

"""
class a : 
class b :
class c(a,b)
"""

"""class father:
    def __init__(self,f_name):
        self.f_name=f_name

class mother :
    def __init__(self,m_name):
        self.m_name=m_name

class child(father,mother):  #MRO : method resolution order
    def __init__(self, c_name,f_name,m_name):
        father.__init__(self,f_name)
        mother.__init__(self,m_name)
        self.c_name=c_name
        
    def show(self):
        print("family info :")
        print("father name :",self.f_name)
        print("mother name :",self.m_name)
        print("child name :",self.c_name)

c=child("harpal","ramesh","ramila")
c.show()
"""

# 3 : multi level inheritance
"""
class a:
class b (a) :
class c(b):
"""
class vehicle :
    def __init__(self,type,seating_cap):
        self._type =type
        self._seating_cap=seating_cap
    def show(self):
        print("vehicle type is :",self._type)
        print("seating cap is :",self._seating_cap)

class car(vehicle):
    def __init__(self,model,type,seating_cap,color):
        super().__init__(type,seating_cap)
        self.model=model
        self.color=color
    def show_1(self):
        self.show()
        print("model is :",self.model)
        print("color is :",self.color)

class car_2(car):
    def __init__(self, model, color,speed,type,seating_cap):
        super().__init__(model, color,type,seating_cap)
        self.speed =speed 
    
    def display(self):
        self.show_1()
        print("speed is :",self.speed)
    
c=car_2("Audi-A6","red","fast","four wheeler",5)
c.display()        
        
        
c1=car("Audi-A4","four wheeler",5,"red")
c1.show_1()