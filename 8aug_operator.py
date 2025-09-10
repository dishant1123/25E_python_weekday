# operator  : 
"""
1. airthematic  op :  + - * / % //
2. comparison  op : == != > < >= <=   ==>  bool value  ==> true or false
3. logical  op : and ,or 
4. assignment  op : = += -= *= /= %= //=
5.member ship op : in  ,not in 
"""

# a=10
# b=100
# print(a/b)  # normal  division 
# print(a//b)  # // ==>  floor  division  

# print(a!=b)   

# print(a>b and a!=b)
# print(a>b or a!=b)
# a=a +b 
# a+=b
# print(a)

# l1 =["ram",1,2,3,4,5]
# print(10 in l1)
# print(10 not in l1)


# match : 

"""
a=int(input("enter  the  number 1 : "))
b =int(input("enter the  number 2 :"))
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulor")
print("6.floor division")

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
    case _ :
        print("wrong  choice")
"""

# nested match : 
# fruits : 

print("1. FRUITS")
print("2. VEGETABLES")

choice =int(input("enter the  choice : "))
match choice :
    case 1:
        print("your selected  fruits")
        print("1.apple :RS . 100")
        print("2.banana :RS . 50")
        print("3.orange :RS . 200")
        sub_choice=int(input("enter the  sub-choice : "))
        match sub_choice :
            case 1:
                print("you selected  apple  ")
                qty =int(input("enter the  quantity : "))
                bill =100 *qty 
                print("your  total bill is :",bill)
            case 2:
                print("you selected  banana  ")
                qty =int(input("enter the  quantity : "))
                bill=50 *qty 
                print("your  total bill is :",bill)
            case 3:
                print("you selected  orange  ")
                qty =int(input("enter the  quantity : "))
                bill =200 *qty 
                print("your  total bill is :", bill)
    case 2 :
        print("your selected  vegetables")
        print("1.potato :RS . 100")
        print("2.tomato :RS . 50")
        print("3.onion :RS . 200")
        sub_choice=int(input("enter the  sub-choice : "))
        match sub_choice :
            case 1:
                print("you selected  potato  ")
                qty =int(input("enter the  quantity : "))
                bill =100 *qty 
                print("your  total bill is :",bill)
            case 2:
                print("you selected  tomato ")
                qty =int(input("enter the  quantity : "))
                bill =50 *qty 
                print("your  total bill is :",bill)
            case 3:
                print("you selected  onion")
                qty =int(input("enter the  quantity : "))
                bill =200 *qty 
                print("your  total bill is :",bill)
    case _:
        print("wrong  choice")

"""
hotel menu : 


1.breakfast :  2 item  
2.lunch  : 2 item  
3.dinner :  2 item  
"""

# conditional statement  : 

"""
if else : 

syntax : 

if condition :
    print
else :
    print

"""
# a=int(input("enter the  number 1 : "))
# b=int(input("enter the  number 2 : "))

"""if a>b:
    print("a is big")
else:
    print("b is big")
"""

"""if a>b :
    print("a is big")
if b>a:
    print("b is big")
"""

# ladder if : 

"""
synatx : 

if con : 
    print
elif con :
    print
else   :
    print
"""

"""
a=int(input("enter the  number 1 : "))
b=int(input("enter the  number 2 : "))
c=int(input("enter the  number 3 : "))

if a>b and a>c :
    print("a is big")
elif b>a and  b>c :
    print("b is big")
elif c>a and c>b:
    print("c is big")
else :
    print("all are same")
"""

# nested : 
"""
if con : 
    if con : 
        print
    else :
        print
elif con : 
    if con :
        print
    else :
        print
else :
    print
"""

"""a=int(input("enter the  number 1 : "))
b=int(input("enter the  number 2 : "))
c=int(input("enter the  number 3 : "))

if a>b : 
    if a>c :
        print("a is big")
    else : 
        print("c is big")
elif b>a :
    if b>c :
        print("b is big")
    else :
        print("c is big")
else :
    print("all are same")
"""

"""
task :1 ask user to enter the 3 number  and  print small big and middle number.

intput  a=10  b =20  c=30
output  : a is small b  is  middle  c is big 

task 2 aks user to enter the character  and print the character in upper case and lower case and vice versa.
hint  : ascci value 

input  :a  output  :A 
input : B   output  :b 

"""

# manav  shrey :  opoerator  ,  user input  , match ,if else :  