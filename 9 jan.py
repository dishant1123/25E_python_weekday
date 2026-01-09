# encapsulation  : 
"""
wrapping data(variable) and  methods in to a single  unit and restrict direct access to the data and methods.  also  protect to misuse of the data and methods.

use for encapsualtion  : 

1.data protection
2.controlled access 
3.data validation
4.better maintainability

2 method : 

1. get / getter 
2. set / setter 

type         syntax     meaning  
1.public    self.name   accessible to all the class  , anywhere  
2.privare  self.__name  accessible to the class  , within the class only  
protected  self._name   accessible inside the class and child class. 

we use private variable with get and set method  for encapsulation.
"""
# ex :1 
"""class bankaccount :
    def __init__(self):
        self.__balance =0   # __balance is private variable  

    def setbalance(self,amt):
        if amt>0 :
            self.__balance =amt 
        else :
            print("invalid amount")
    
    def getbalance (self):
        return self.__balance

b=bankaccount()

# before using  set method  balance :
print("before using set method  balance your balance is   : ")
print(b.getbalance())

# set method balance  : 
b.setbalance(50000)

# get method  balance  : 
print("after using set method  balance your balance is   : ")
print(b.getbalance())
"""
# ex :2 

class bankaccount : 
    def __init__(self):
        self.__balance =25000 
        
    def deposit(self,amt):
        self.__balance +=amt
        print(f"depsoited  : {amt}")
    
    def withdraw(self,amt):
        if self.__balance -amt >= 10000 :
            self.__balance -=amt
            print(f"withdrawed  : {amt}")
        else :
            print("min balance is 10000")
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amt):
        self.__balance=amt 
        print("your new balance is  : ",self.__balance)
        
b=bankaccount()
print("beofore  using  set  balance  method your balance is  : ",b.get_balance()) 

b.deposit(10000)
b.withdraw(2500)
print("after deposit  and withdraw your balance is  : ",b.get_balance()) 

b.set_balance(50000)
print("after using set  balance method your balance is  : ",b.get_balance())
b.deposit(10000)
b.withdraw(25000)
print("after deposit  and withdraw your balance is  : ",b.get_balance())

