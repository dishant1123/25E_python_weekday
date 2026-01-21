#polimorphism : 
"""
many  forms

its is  one function or method  name behaves differently  based on the type of the object on which it is invoked.

python support  polymorphism  :
1. duck typing
2. operator  overloading
3. method overriding
4. method overloading
"""
"""
not  support  :  like  python  does not support method  overloading in traditional way (same name different parameters)

it is  achieved using default arguments or varibale arguments. 
"""

# ex : 1 method  overloading  using default  arguments : 

"""
class calculator : 
    def add(self, a,b=0,c=0):
        return a+b+c
    
c=calculator()
print(c.add(12))  # only given a arg  then  b and  c value  is  0 bcz  default  value  set is  0. 
print(c.add(12,13)) # a and  b arg is  given but c arg is  default so it take 0 . 
print(c.add(12,15,18))
"""

# ex :2 method  overloading using *args :  ==> *args  only take numberic args.

"""class calculator :
    def add(self,*args):
        sum =0 
        for i in args : 
            sum =sum +i 
        return sum
    
c=calculator()
print(c.add(12))
print(c.add(12,13,56))
print(c.add(12,14,78,90))
"""

# ex :3 method  overriding : 
"""
it happens when base class provides its own implementation of a method already in the  
derived class.
"""

"""class vehicle :
    def speed(self):
        print("max speed of the vehicle is  : 180")
        
class car(vehicle):
    def speed(self):
        # super().speed()
        print("max speed of the car is  : 300")
   
c=car()
c.speed()
"""
"""
c++ java  : 

class vehicle :
    vehicle()
    {
        cout<<"max speed of the vehicle is  : 180"<<endl;
    }
    vehicle()
    {
        string  name  = "car"
        int  speed ; 
    }
    vehicle(string n , int s )
    {
        name =n;
        speed =s; 
    }
int main() 
{
    vehicle v1;
    vehicle v2("car",300);
    vehicle v3(300);
    
}
"""

# method  overloading : 

"""class payment : 
    def pay(self,amount,method ="cash" ):
        if method =="cash" :
            print("cash  payment  :  ",amount)
        elif method =="card" :
            print("card  payment  :  ",amount)
        else :
            print("UPI  payment  :  ",amount)
            
p=payment()
p.pay(1000)
p.pay(10000,"card")
p.pay(100000,"UPI")
"""
# same method  ==> pay  , diff arg  ==> behavior changes based on input 

# method  overriding : 

"""
all banks are give interest. 
but  each bank  has  different  interest rate.
"""
class bank :
    def interest(self):
        print("interest  :  5% ")

class SBI(bank):
    def interest(self):
        print("SBI interest  :  7% ")

class HDFC(bank):
    def interest(self):
        print("HDFC interest  :  10% ")
 
b1= SBI()
b2= HDFC()

b1.interest()
b2.interest()


# method  same  , base class give its  own implementation  , derived class override it.

# conculsion  : 
"""
overloading : same work  different inputs 
overriding  :  same work  different objects 
"""

"""
Write a Python program to find the Net Salary of an Employee using Inheritance, Encapsulation, and Polymorphism.

Create three classes: Employee, Perks, and NetSalary.

Requirements
🔹 Employee Class

Use encapsulation (private data members).

Data members: employee id, name, basic salary.

Methods:

To get employee details from the user.

To display employee details.

To return basic salary.

Create a method calculate_salary() that will be overridden (polymorphism).

🔹 Perks Class (inherits Employee)

Calculate:

DA = 35% of basic salary
HRA = 17% of basic salary
PF = 12% of basic salary

Method to display DA, HRA, PF.

Override calculate_salary() method.

🔹 NetSalary Class (inherits Perks)

Calculate total salary:

Net Salary = Basic Salary + DA + HRA − PF

Display employee details, perks, and net salary.

Demonstrate method overriding (runtime polymorphism).

📌 It is compulsory to create objects and demonstrate the methods with correct output
"""