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

class vehicle :
    def speed(self):
        print("max speed of the vehicle is  : 180")
        
class car(vehicle):
    def speed(self):
        # super().speed()
        print("max speed of the car is  : 300")
   
c=car()
c.speed()

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