# while  loop  : 
"""
syntax : 

i =intial  value  

while  con : 
    print()
    i+=1
"""
# 1-100 : 

"""
i=1 
while i<=100:
    print(i,end=" ")
    i+=1
"""

# break continue pass : 

# break : 
"""
for i in range(1,10):
    if i==5 :
        break 
    print(i,end=" ")
"""
# contunie : 
"""
for i in range(1,10):
    if i==5 :
        continue
    print(i,end=" ")
"""

# pass : 
"""for i in range(1,10):
    if i==5 :
        pass 
    print(i,end=" ")
"""
# match  : 

a= int(int(input("enter a : ")))
b= int(int(input("enter b : ")))

print("1.addition ")
print("2.subtraction ")
print("3.multiplication ")
print("4.division ")
print("5.modulus ")
print("6.add new  number  ")
print("7.exit ")
choice = int(input("enter choice : "))
match choice :
    case 1 :
        print(a+b)
    case 2 :
        print(a-b)
    case 3 :
        print(a*b)
    case 4 :
        print(a/b)
    case 5:
        print(a%b)
"""
1. exit 
2. add new number :  
"""        
# while True : 
"""
syntax :
i=intial  value  
while True :
    print()
    i+=1 
    if  con : 
        break

"""    
# 1-10 : 
"""i=1 
while True :
    print(i,end=" ")
    i+=1
    if i==10 :
        break
"""
        
