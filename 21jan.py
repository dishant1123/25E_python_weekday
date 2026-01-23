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
# task  :2 
"""
Create an abstract class named Shape. 
Create an abstract method named calculate_area for the Shape class.
Create Two Classes named Rectangle and Circle which inherit Shape class.
Create calculate_area method in Rectangle class. It should return the area of the rectangle object. (area of rectangle = 
(length * breadth))
Create calculate_area method in Circle class. It should return the area of the circle object.
(area of circle =πr^2))
Create objects of Rectangle and Circle class.
The python Program Should also check whether the area of one Rectangle object is greater
than another rectangle object by overloading > operator.
"""

# task  :3 
"""
Create a program to simulate a Call Handling System using Object-Oriented Programming (OOP) concepts in Python.
The program must demonstrate the use of the following OOP principles:

1.Abstraction
2.Inheritance
3.Encapsulation
4.Polymorphism

Requirements:
1. Employee Classes
Create three classes named:
	Respondent
	Manager
	Director

Each class should have a constructor that accepts id and name.
The constructor should initialize:

	==>rank
		3 for Respondent
		2 for Manager
		1 for Director

	==>free → a boolean variable initialized to True

2. Common Methods (Demonstrating Abstraction & Inheritance)
Implement the following methods in all three classes:

	receive_call()
	Prints:
	"call received by <employee name>"
	and sets free to False

	end_call()
	Prints:
	"call ended"
	and sets free to True

	is_free()
	Returns the value of free

	get_rank()
	Returns the value of rank

3. Call Class

Create a class Call with a constructor that accepts:
	id
	name of the caller

It should initialize a variable assigned to False.

4. CallHandler Class

Create a class CallHandler with three class variables:
	respondents
	managers
	directors

5. Employee Management (Encapsulation)

Implement an add_employee() method in CallHandler that:
	Accepts an employee object
	Adds it to the appropriate list based on their rank

6. Call Dispatching (Polymorphism)

Implement a dispatch_call() method in CallHandler that:

Accepts a Call object
Assigns the call to the first available employee, checking in the order:

	Respondent → Manager → Director

Calls receive_call() on the assigned employee
Sets the call’s assigned variable to True
If no employee is free, prints:
"Sorry! All employees are currently busy."

7. Object Creation
Create:
	3 Respondent objects
	2 Manager objects
	1 Director object
Add them to the system using add_employee().

8. Call Assignment

Create a Call object and demonstrate how it is assigned to an employee using the dispatch_call() method.
"""
