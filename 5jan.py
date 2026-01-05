"""
bank using  class object : 
"""

class bank  : 
    def __init__(self,name,acnumber):
        self.balance =25000 
        self.name = name
        self.acnumber =acnumber 
        
    def deposit(self,amt):
        self.balance +=amt 
        print(f"Deposited {amt} to {self.name}") 
        
    def withdraw(self,amt):   # bal =28000   with  ==>23000 
        if(self.balance -amt >= 10000 ) : #   28000 - 23000 >= 10000
            self.balance -=amt 
            print(f"Withdrawed {amt} from {self.name}")
        else:
            print("min balance is 10000")
    
    def check_balance (self):
        print("final  balance  is  : ",self.balance) 

b=bank("raj",1234567890)
b.deposit(10000)
b.withdraw(2500)
b.check_balance() 

"""
task  :1  pin generated   
    enter your pin  : 
    wrong  min   ==> max attempt   ==> 3   exit  
task  :2   menu driven  
    choice  : 
        1. deposit  
        2. withdraw
        3. check balance
        4. exit
"""