# lambda function  : one  liner  function  

"""
syntax : 

lambda arg : expression  
"""  
# normal  function  : 

"""
def add(a,b):
    c=a+b
    return c 
print(add(12,14))
"""
# using lambda function  : 

"""x =lambda a,b : a+b
a=int(input("enter a number:"))
b=int(input("enter b number:"))
print(x(a,b))
"""

# built in function  : len min max sorted 

"""
a= lambda c : sorted(c,reverse=True)
print(a((12,2,3,4,5,6)))
"""

# conditional statement  : 

"""
def add(a,b):
    if a>b :
        print("a is big")
    else :
        print("b is big")
add(12,14)
"""

"""
x =lambda a,b : ("a is big")if a>b  else b("b is big") 
print(x(34,1))
"""

# task  :1 
"""
input  : [[2,1],[3,0],[4,5]]
sorted second  value  

output  : [[3,0],[2,1],[4,5]]

"""
# l1=["harix","ved","krishna","aashta","meet","krish","vatsal"]

# a=sorted(l1)
# print(a)

# len sorted  : asc to desc : key 
"""l1=["harix","ved","krishna","aashta","meet","krish","vatsal"]
b =sorted(l1,key=len)  # key  special  method  ==> len max min sorted 
print(b)
"""

"""
def sorted_second(l1):
    return l1[0]
l1= [[2,1],[0,0],[4,5]]
a =sorted(l1,key=sorted_second)
print(a)
"""
#
"""
(0,0)2   (0,1)1     [2,1]  ==> index 0  ==> 2 ==> 1 ==> 1 
(1,0)3   (1,1)0     [3,0] ==> index 1  ==>3 ==>0 0==>1 
(2,0)4   (2,1)5     [4,5] ==> index 2  ==> 4 ==>0  5 ==> 1 
"""
"""print(l1[0]) 
print(l1[1][1])
"""
"""
for i in l1 :
    print(i)
"""

"""
l1= [[2,1],[0,0],[-4,5]]
a= sorted(l1,key=lambda x : x[0])
print(a)
"""