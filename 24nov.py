# multi level  inheritance  : 
"""
class a : 
class b (a) :
class c (b):
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