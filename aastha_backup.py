# oops  :  object  oriented  programming
"""
class : bule  print  of  object . 
object : instance of class. 

class fruit : 
      apple kiwi banana  mango   ==> object 
      
type of  class : 
1. public  : data members  access any where . 
2. private  : data members access only in class. 
3. protected : data members access only in class and its derived class.
"""
# ex :1  public 

"""class student : 
    name ="sailee"  # name age   ==> public  data members 
    age =20 

    def show(self) :
        print("name  of  student is :",self.name)
        print("age  of  student is :",self.age)
        
s=student()   # s object   ==> class student 
print("name  of  student is :",s.name)
print("age  of  student is :",s.age)
s.name="aastha"  # change  name
s.age=19 
s.show()
"""
# ex :2  private 

"""class student : 
    __name ="sailee"  # name age   ==> private  data members
    __age =20 
    
    def show(self):
        print("name  of  student is :",self.__name)
        print("age  of  student is :",self.__age)
    
s=student()
# print("name  of  student is :",s.__name)  # error : bcz of  private only access in class .
# print("age  of  student is :",s.__age)
s.show()
s.__name="aastha"  # change  name not possible bcz of  private only access in class .
s.__age=19
s.show()

"""

# ex :3  protected

class student : 
    _name ="sailee"  # name age   ==> protected  data members
    _age =20 
    
class teacher(student): 
    def show(self): 
        print("name  of  student is :",self._name)
        print("age  of  student is :",self._age)

t=teacher()
t.show()
t._name="aastha"  # change  name not possible bcz of  protected only access in class and its derived class .
t._age=19
t.show()

