# oop  :  object oriented programming
"""
class :  class is  blue  print  of object.  
object : object is  entity  , real world  , instance of class. 

type of  class : 
1.  public  class ==> data member  /  method  ==>  access any  where outside  and also inside  the class. 

2. private  class ==> data member  /  method  ==>  access only inside  the class.
3. protetced class ==>  inheirtance  data member  access / modify 

"""
#1 : 
"""
class person :
    name ="krish"  # by default  public  ==> name  age clg ==> data member 
    age= 20 
    clg ="Nirma"

p=person()  # p==> obj   ==> person  ==> class name 
print(p.name)
print(p.age)  # object data member  access ==> person class 
print(p.clg)
p.name ="krishna"
p.age =21 
p.clg ="GU"
print(p.name)
print(p.age)
print(p.clg)
"""

#2 : 
"""class employee :
    name ="vatsal"  # public ==> name age  salary 
    age =21 
    salary =80000 
    
    def show(self):  # self  ==>  keyword ==> current  object / member data access self ,  method  ==>  access  
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("salary is  :",self.salary)
        
e=employee()
e.show()  # function  ==> data member print  
print(e.name)

e.name ="krishna"
e.show()
"""

# 3 : private  class  

class vehicle : 
    __name =input("enter the  vehicle  name  : ") # name model yr  ==> private  
    __model=input("enter the  vehicle  model  : ")
    __year=int(input("enter the  manufacure year : "))
    
    def display(self):
        print("vehicle name  :",self.__name)
        print("vehicle model  :",self.__model)
        print("vehicle year  :",self.__year)

v=vehicle()
v.display()  # access  private  data member  ==> print  
# print(v.__name)  # bcz of  private  you can't access the  data member  though object.
 
