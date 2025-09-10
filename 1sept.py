"""
take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131]
"""
n=int(input("enter the number of elements in the list : "))
l1=[]
for i in range(n):
    ele = int(input("enter the element : "))
    l1.append(ele)
print(l1)  # [121, 111, 456]
l2=[]
for i in  l1: 
    if str(i) == str(i)[ : : -1]:  # "121"
        l2.append(i)
print(l2)

"""
121 : 

r=  1 %10  =1  
rev = rev *10 +r =1 * 10 +2  =12  *10 +1 =121
n =n //10   1 //10 =0
"""

"""s1="my name is  ved."
print(s1[ : : -1])
"""