# class object : 

"""
1. public  
2. private 
3. protected
"""

# public : 
"""
class person :   # person class name 
    name ="krish"  # name age  -==> public  member  / data member  
    age =21 
    
    def show(self):  # self ==> keyword ==> current object + member access ==>self 
        print("name is :",self.name)
        print("age is :",self.age)
        
p=person()   # p object 
print("before  change :")
p.show()
# print("name is  :",p.name)  
# print("age is  :",p.age)
print("after  change :")
p.name ="harpal"
p.age=22 
p.show()
"""

# private :

"""class student :
    __name ="krish"  # __name,__age ==> private member
    __age =21       
    
    def show(self):
        print("name is :",self.__name)
        print("age is :",self.__age)
s=student()
s.show()
print("name is  : ",s.__name)
print("age is  : ",s.__age) # not accessible bcz of private member
s.__name ="harpal"
s.__age=22
s.show()  # note : not change  in original values and also  not give error print only static value. 
"""

# protected :

class person : 
    _name ="krish"  # _name,__age ==> protected member
    _age=21

class student(person):
    def show(self):
        print("name is :",self._name)
        print("age is :",self._age)

s=student()
s.show()
