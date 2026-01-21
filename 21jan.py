# abstraction  : 
"""
means  hiding implementation details and showing only essential  detalis and  features to user.
in python abstraction mainly achieved by using  class and  function.
    1. class : from abc import  ABC  == > ABC ==> abstract base class
    2. method/ function  : @abstractmethod  == > abstract method
    
==> abstract class can't be instantiated.
==> you can't create an object of an abstract class.
    
"""

from abc import ABC, abstractmethod
"""
class vehicle(ABC):   # abstract  base class 
    
    def __init__(self,brand,fuel):
        self.brand=brand 
        self._fuel = fuel  # protected 
        self.__engine= "END123"  # private 
        
    @abstractmethod
    def mileage(self):
        pass 
    def get_engine_no(self):
        return self.__engine
    
class car(vehicle):
    def __init__(self, brand, fuel):
        super().__init__(brand, fuel)  # calling abstract class constructor  
        
    def mileage(self):
        return "15 km/l"
    
c=car("BMW","petrol")
print("brand of car name is  : ",c.brand)
print("fuel of car is : ",c._fuel)
print("engine no of car is : ",c.get_engine_no())
print("mileage of car is : ",c.mileage())
"""
# print(c.__engine)  # it given error . 

"""
pure virtuall function  = 0 
"""

# combine  example  of  abstraction , encapsulation , inheritance  and  polymorphism : 

class bankaccount(ABC) :
    def __init__(self,name,balance):
        self.name =name 
        self._balance =balance 
        self.__pin =1234
        
    @abstractmethod
    def calculation_interest(self):
        pass 
    
    def get_balance(self):
        return self._balance

    def deposit(self,amt):
        self._balance+=amt

    def get_pin(self):
        return self.__pin

class savingaccount(bankaccount):
    
    def calculation_interest(self):
        return self._balance * 0.05
    
class currentaccount(bankaccount):
    
    def calculation_interest(self):
        return self._balance * 0.02 
    
saving = savingaccount("krishna",60000)
current = currentaccount("aashta",90000)

accounts = [saving,current]

for i in accounts :
    print("name of account is : ",i.name)
    print("balance of account is : ",i.get_balance())
    print("interest of account is : ",i.calculation_interest())
    print("pin of account is : ",i.get_pin())
    
# task  :1 
"""
1. menu  : 
    a. current  
    b. saving  
    
2. create pin  : 
    pin : 9000 
    verify  the pin when  you choose  current  or saving  
"""