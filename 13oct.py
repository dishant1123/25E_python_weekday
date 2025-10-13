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
