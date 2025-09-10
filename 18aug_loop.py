# loop :
"""
1. for loop  
2. while 
3. while  True
""" 
#  in c : 
"""
for(start; condition; inc/dec)
{
    printf();
}

python  : 

for  (variable name)  in range(start , stop , step):
    print()
"""

# 1-100 : 

"""for i in range(1,101):  # start 1  end 100 
    print(i,end=" ")
"""

# 100-1 : 

"""
for x  in range(100,0,-1):
    print(x,end=" ")
"""

"""
for x  in range(1,100,2):
    print(x,end=" ")
"""
"""
for x  in range(1,100,3):
    print(x,end=" ")
"""

#user  input : 

"""n=int(input("enter the  number : "))

for i in range(1,n+1):
    print(i,end=" ")
"""

# user start ,end : 

"""start =int(input("enter the  start number : "))
end=int(input("enter the  end number : "))

for x in range(start,end +1,2):
    print(x,end=" ")
"""

# break ,continue , pass:

"""
for i in range(1,20):
    if i==6:
        break
    print(i,end=" ")
"""

"""for i in range(1,20):
    if i==6:
        continue
    print(i,end=" ")
"""

"""
for i in range(1,20):
    if i==6:
        pass
    print(i,end=" ")
"""

# while  loop :

"""
i =intial value 

while con : 
    print ()
    i+=1
"""
# 1-100 : 

"""i=1 
while i <=100 :
    print(i,end=" ")
    i+=1
"""

# while true  : 

"""i=1 
while True : 
    print(i,end=" ")
    i+=1
    if i==10 :
        break
"""
while True :
    a=int(input("enter  the  number 1 : "))
    b =int(input("enter the  number 2 :"))
    while True :
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.modulor")
        print("6.floor division")
        print("7.add new number ")
        print("8 exit")
        choice = int(input("enter the  choice : "))

        match choice :
            case 1 :
                print(a+b)   
            case 2 :
                print(a-b)
            case 3 :
                print(a*b)
            case 4 :
                print(a/b)
            case 5 :
                print(a%b)
            case 6 :
                print(a//b)
            case 7 : 
                break
            case 8 :
                exit()