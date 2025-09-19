# ch =input("enter the  character : ")

# A ==>a k ==> K  == >ascci value  : A => 65 a ==>97  diff =32 
# ord ==> ascci value  print  

"""
if ch >= "A" and  ch <='Z': 
    ch = ord(ch) +32 
    print(chr(ch)) 
else : 
    ch =ord(ch) -32 
    print(chr(ch))
"""

# loop  : 
"""
1. for  loop : entry control  
2. while loop : exit 
3. while True : exit 
"""

# for  loop syntax :
"""
for (variable name)  in range(start, stop,step):
    print(variable name)

""" 

# 1-100 : 

"""
for i in range(1,101):
    print(i,end=" ")
"""

# 100-1 : 
"""for x in range(100,1,-1):
    print(x,end=" ")
"""

# for i in range(1,101,2):
#     print(i,end=" ")

"""for i in range(100,0,-2):
    print(i,end=" ")
"""

# user  number  : 

"""n=int(input("enter the number : "))
for i in range(n+1):
    print(i,end=" ")
"""

"""start =int(input("enter the start number : "))
end =int(input("enter the end number : "))

for i in range(start,end+1,2):
    print(i,end=" ")
"""

# n-natural  number  sum  : 
"""
n=int(input("enter the number : "))
sum =0 
for i in range(1,n+1):
    sum =sum +i 
print("sum  : ",sum)
"""