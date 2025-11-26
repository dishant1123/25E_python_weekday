# encapsulation : single  unit  , private member direct access 
"""
1. get method  :  data  print 
2. set method :   set a new value 
"""

"""class person : 
    def __init__(self,name,age):
        self.__name =name
        self.__age =age   # name , age  ==> private member
        
    def show(self):
        print("name :",self.__name)
        print("age :",self.__age)
        
p=person("harpal",21)
p.show()
p__name ="smit"
p.__age =23
p.show()  # not  change bcz  of  private member 

"""

# encap : 

class person : 
    def __init__(self,name,age):
        self.__name =name
        self.__age=age  
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def set_new_age(self,new_age):
        self.__age = new_age 
    
    def set_name(self,new_name):
        self.__name = new_name
        
p=person("rishi",21)
print("without using  set method : ")
print(p.get_name())
print(p.get_age())

print("using set method : ")
p.set_name("yash patel")
p.set_new_age(22)
print(p.get_age())
print(p.get_name())
