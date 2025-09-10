"""
task : 3 take list from user append all element in list and remove duplicate element in the list.
         input : [1,2,3,4,4,5,5,6,7,8,9,9,10]
         output : [1,2,3,4,5,6,7,8,9,10]   

"""
"""
n=int(input("enter the number of elements in the list : "))
l1=[]
for i in range(n):
    element =int(input("enter the element : "))
    l1.append(element)
print(l1)   # [1,2,3,4,4,5,5,6,7,8,9,9,10]
l2=[]
for i in  l1 : 
    if i  not in l2 : 
        l2.append(i)
print(l2)
"""
# odd even  : 

"""
n=int(input("enter the number of elements in the list : "))
l1=[] 
odd=[]
even=[] 

for i in range(n):
    element =int(input("enter the element : "))
    l1.append(element)
print(l1)
# l1 =[1,2,3 ]
for i in l1 : 
    if  i% 2==0 :
        even.append(i)
    else :
        odd.append(i)
print("even :",even)
print("odd :",odd)
"""

# slicing  : 
l1=[10,20,30,40,50,60,900 ,800,1234,789]

# index start : 0 1 2  ===> pos  ==>  l to r 
# neg index start :-1   ==> r ot  l 
"""
print(l1[3])
print(l1[ 2 :7])   # 2 start  index ,  7 ending  index 
print(l1[  :7])   
print(l1[1  :])   
print(l1[  :])   
"""
"""
print(l1[-3])
print(l1[-7 :-3])
print(l1[ 2 :8 : 2])  # 2 start  index , 8 ending  index step 2 

print(l1[ 1 :-2 : 3])  # 2 start  index , 8 ending  index step 2 
print(l1[ : : -2])
print(l1[ : : -1])
print(l1[ : : 2])
"""

"""
take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131]

"""


