# multi level  inheritance  : 
"""
class a : 
class b (a) :
class c (b):
"""
"""
class vehicle  :
    def __init__(self,name,model):
        self.name=name
        self.model =model 
    
    def show(self):
        print("name  is  :",self.name)
        print("model  is  :",self.model)

class car(vehicle):
    def __init__(self, name, model,color):
        super().__init__(name, model)  # base class constructor call
        self.color = color 
    
    def show(self):
        super().show()  # base class method  call 
        print("color  is  :",self.color)
        
class bike(car):
    def __init__(self, name, model, color,seat):
        super().__init__(name, model,color)  # base class constructor call
        self.seat = seat
    
    def show(self):
        car.show(self)
        print("seat  is  :",self.seat)
        
b=bike("honda","shine","black",2)
b.show()

c=car("toyota","corolla","white")
c.show()
"""
#4. hierarchical inheritance : multiple  derived class inherit  from  same base class. 

"""
class a : 
class b(a) :
class c (a) :
"""

"""class vehicle :
    def __init__(self,name,model):
        self.name=name
        self.model =model
        
    def display(self):
        print("name  is  :",self.name)
        print("model  is  :",self.model)

class car(vehicle):
    def __init__(self, name, model,color,seat):
        super().__init__(name, model)  # base class constructor call
        self.color = color
        self.seat=seat 
        
    def drive(self):
        print(f"car is driving with {self.color} and {self.model} . seating capacity is  {self.seat} and car name is {self.name}")

class bike(vehicle):
    def __init__(self, name, model,speed,seat):
        super().__init__(name, model)  # base class constructor call
        self.speed = speed
        self.seat=seat
    
    def ride(self):
        print(f"bike is riding with {self.speed} and {self.model} . seating capacity is  {self.seat} and bike name is {self.name}")
        
c=car("toyota","corolla","white",2)
print("car information : \n")
c.drive()
c.display()

b=bike("honda","shine",180,2)
print("bike information : \n")
b.ride()
b.display()
"""
# 5 : hybrid inheritance : it is  combination of one or  more of the  inheritance .
"""
class a : 
class b(a) :
class c: 
class d(b,c):
"""


        
