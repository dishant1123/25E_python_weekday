# nested  loop  : 
"""
use  user 2 range : 

"""
"""
start =int(input("enter start range : "))
end = int(input("enter end range : "))

for i in range(start,end +1):
    count = 0 
    for j in range(1,i+1):
        if i % j ==0 :
            count +=1 
    if count ==2 :
        print(i,end=" ")
    
"""

# amg : 

"""
start =int(input("enter start range : "))
end = int(input("enter end range : "))

for i in range(start,end +1):
    sum =0 
    digit = len(str(i))
    temp =i 
    for j in range(digit):
        r= temp %10 
        sum = sum + pow(r,digit)
        temp =  temp // 10
    if sum ==i :
        print(i,end=" ")
"""
