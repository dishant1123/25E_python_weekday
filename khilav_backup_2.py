# data type  : 
"""
1. int  : pos  or neg  store  ==> no limit
2. float  :  decimal  value store  
3. string  /  chr :  name  , a to z  character . 
4. bool   :  true  or  false  store
5. complex :  2 part ==>  1 . real  2. immaginary
"""
"""a=10
print(a)
print(type(a)) 

b =1234512342345234545634563456345623453452345634567
print(b)
print(type(b)) 

c =12.34 
print(c)
print(type(c))

d =123456.23456784567567789
print(d)
print(type(d))

e ="khilav"
print(e)
print(type(e))

f= True
print(f)
print(type(f))

g = 89 + 5j   # real part : 89  ,  immaginary part : 5j 
print(g)
print(type(g))
h= 90 +10j 
print(g+h)
"""

# user input  string  : 

"""a=str(input("enter the string ==> name   : "))
b =input("enter the string ==> surname  :")
print(a,end=" ")
print(b)
# print(a+" "+b)
"""

# user  input number  : 

"""
a= int(input("enter the  number  1:"))
b= int(input("enter the  number  2:"))
print(a)
print(b)
"""

"""a= float(input("enter the  number  1:"))
b= float(input("enter the  number  2:"))
print(a)
print(b)
"""

# task  1 : 
"""
ask user  to enter the  int  type  number  and concate  them. 

input  a =10 
input  b =20
output  : 1020
"""
"""a= int(input("enter the  number  1:"))
b= int(input("enter the  number  2:"))
print(a,end="")
print(b)
"""

# operator  : 
"""
1. airthematic : + - * / % // 
2. comaprison  : < > <= >= == !=
3. logic : and or not 
4. assignment : = += -= *= /= %= //=
5. member : in ,not in

"""
a=1093 
b=1000 
# print(a/b)  # div 
# print(a//b)  # floor  div 
# print(a%b)
# print(a!=b)
# print(a>b and a!=b)
# print(a>b or a!=b)
# print(a>b is not a!=b)

# a= a+b 
"""a+=b   # += , -= , *= , //= , %=   ==> assign 
print(a)
"""
"""
l1=[1,2,3,4,"khilav"]
print(20 in l1)
print(2  not in l1)
"""

# conditional statement  :
"""
syntax : 

if condition : 
    print 
else :
    print 
""" 

# a=int(input("enter the  number  1:"))
# b=int(input("enter the  number  2:"))

"""if a>b :
    print("a is  big")
else :
    print("b is  big")
"""
# print("a is  big ")if a>b else print("b is  big")

"""
nested if : 

if con :
    print 
elif con :
    print
else :
    print
"""
a=int(input("enter the  number  1:"))
b=int(input("enter the  number  2:"))
c=int(input("enter the  number  3:"))

if a>b and a>c :
    print("a is  big")
elif b>a and b>c :
    print("b is  big")
elif c>a and c>b:
    print("c is  big")
else: 
    print("all are  equal")