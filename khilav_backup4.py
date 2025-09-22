# prime  : 
"""
2 factors  : prime == > 1 , number  it self   

3 factors  : 1,3  == > prime  
4 factors : 1,2,4 ==> not  prime  
"""

"""n=int(input("enter the  number  : "))  # 6   
count =0 
for i in range(1, n+1 ):   #6  7 
    if n % i ==0 :   # 6 % 6 ==0 
        count +=1   # cnt =4  
if count ==2 :
    print("prime")

"""

# perfect number  : 
"""
6 factors :  1 2 3 6  sum  = => 1+2+3 = 6  perfect 
28 factors : 1 2 4 7 14  28 sum => 1+2+4+7+14 =28 perfect 

"""
# amg number : 
"""
153 :  3 digit  

1 **3  5**3  3**3 
1      125    27 
sum = 1+125 +27 =153   ==>amg  

1634 : 4 digit 

1**4  6**4  3**4 4**4 
1     1296  81   256 
sum = 1+1296 +81 +256 =1634 ==>amg 
"""
"""
n =int(input("enter the  number  : "))    # 153 
digit = len (str(n))  # 3 
sum =0 
temp =n   # temp =153 
for i in range(digit):  # 2 ,3 
    r =temp %10   # r =  1 % 10 =1  
    sum =sum + pow(r,digit)  # sum =153    
    temp = temp //10   # temp  =0  
    
if sum ==n : # 
    print("amg")
"""

# rev :  input : 123  output  : 321 