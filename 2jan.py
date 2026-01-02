"""
class object : 

type  : 
1.public  : accessible from anywhere
2.private : witin the class
3. protected : accessible from the class and its subclasses(inheritance)
"""
# public : 
"""
class person :  # person  ==>class name 
    name ="krishna"
    age =21       # name  age  ==> data members   ==> public 

    def show(self):  # self ==> key word ==> current object  ==> member access 
        print("name is  : ",self.name)
        print("age is  : ",self.age)
    
p=person()  # p ==> object 
# print("name is  : ",p.name)  # object though  ==> print 
# print("age is  : ",p.age)
p.show()
p.name ='krish'
p.age=20 
# print("name is  : ",p.name)
# print("age is  : ",p.age)
p.show()
"""

# private  : 
class employees : 
    __name="aashta"
    __age=19 

    def show(self):
        print("name is  : ",self.__name)
        print("age is  : ",self.__age)
e=employees()
# print("name is  : ",e.__name)
# print("age is  : ",e.__age)  # __name  __age  ==> private   not  poss bcz of  private . 
e.show()
e.__name="krishna"
e.__age=21
e.show()