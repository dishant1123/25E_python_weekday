# emp management  :
"""
1.add 
2.delete 
3.update 
4.search 
5.display
"""
class employess : 
    def __init__(self):
        self.emp=[] 
    
    def add_emp(self):
        id=int(input("enter the id :"))
        name =input("enter the name :")
        age=int(input("enter the age  : "))
        salary =int(input("enter the salary  :"))
        e={"id":id,"name":name,"age":age,"salary":salary}
        self.emp.append(e)
        print("emp added successfully")
    
    def delete_emp(self):   # del 
        emp_id =int(input("enter the id you  want to delete : "))
        for i in self.emp:
            if i['id'] ==emp_id:
                self.emp.remove(i)  # list method 
                print("emp deleted successfully")
                break
        else :
            print("emp not found")
    
    def update_emp(self):   # update
        emp_id =int(input("enter the id you  want to update : "))
        for i in self.emp:
            if i['id'] ==emp_id:
                print("enter the new details")
                i['name'] =input("enter the name :")
                i['age']=int(input("enter the age  : "))
                i['salary']=int(input("enter the salary  :"))
                break
        else :
            print("emp not found")
            
    def display_emp(self):
        if not  self.emp:
            print("emp not found")
        else :
            print("EMP list : \n")
            for i in self.emp :
                print(f"id : {i['id']} name : {i['name']} age : {i['age']} salary : {i['salary']}")
            print("\n")

    def menu(self):
        while True: 
            print("1.add \n2.delete \n3.update \n4.search \n5.display \n6.exit")
            choice =int(input("enter the choice :"))
            if choice ==1 :
                self.add_emp()
            elif choice ==2 :
                self.delete_emp()
            elif choice ==3 :
                self.update_emp()
            elif choice ==4 :
                self.display_emp() 
            elif choice ==5 :
                print("exit program")
                break 
            else :
                print("invalid choice")

em =employess()
em.menu()
#   
"""

# search  : 
id  name  age  salary  
1    ram    55   9000
2    sita   53    8000

key = [name  age  salary ]   ==>del decorator  
[1 name age salary  ]
"""
