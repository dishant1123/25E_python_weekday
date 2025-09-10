# prime  , perfect , twin  , armstrong , reverse  , palindrome : 

# prime  : 2 factors  ==> 1 , num it self 

"""
n=int(input("enter the  number  : ")) 
count =0
for i in range(1,n+1):
    if n % i== 0 :
        count +=1

if count ==2 :
    print(n,"is  a  prime  number")
"""

"""
for i in range(1,10) :
    print(i)
print("hello") 
"""

"""for i in range(1,10) :
    if i==5 :
        break
    print(i)
else :
    print("hello") 
"""    

# k  S   V  V   K  M  H  Har 
# 1-5 hello next line  ==>k s v 
# 1-4 hello ==> v k m h h  
#  
# k s k  h  m  a =>1-4  v ==> 1-4 hello  

"""
armstrong  number  : 

153 : 3 digit 

1**3  5**3  3**3 
1      125   27
sum = 1+125 +27 =153 amg 

1634   4 digit 

1**4  6**4  3**4  4**4 
1    1296   81     256 
sum = 1+1296+81+256 =1634 amg

"""

# built in function  : len  min max sorted sum .. 

"""n =int(input("enter the number:")) # "153 
digits =len(str(n))  # 3 
print(digits)  # 3 
temp = n   # temp =153 
sum =0
for i in range(digits):   #2,3 
    r= temp %10     # r =1 %10 =1 
    sum =sum + pow(r,digits) # sum =153
    temp = temp //10   # temp = 1 //10 =0 

if sum ==n : #153 == 153 
    print(n,"is  an  armstrong  number")

"""

# twin number  : 
"""
123 ,22: 

mul =1*2*3=6
sum =1+2+3 =6 

if sum ==mul : twin 
"""