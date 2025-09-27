# python data type  : 
"""
1. string : immutable sequence of characters 
2. list : mutable sequence of any data type
3.tuple : immutable sequence of any data type
4.dict : mutable sequence of key-value pairs
5.set : mutable unordered collection of unique elements
"""

# list : mutable sequence of any data type  ==> can be  changes.

"""
l1=[1,2,3,4,5,6,45.78,8j,True]

print(l1)
print(type(l1))

"""

# list  element  acces though index ,update:
"""
index start : 0 
negative index :-1
"""
"""
l1=[10,20,30,40,50,60,45.78,8j,True]

# print(l1[3])

l1[3]="khilav"
print(l1)
"""

# built in function  : len min max  sorted sum 
"""
l1=[10,20,30,40,50,60,45.78]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))# asc to desc order
print(sorted(l1,reverse=True))# desc to asc order
print(sum(l1))
"""

# slicing : 
"""
index start : 0   ==> l to r 
negative index :-1 ==> r to l 

"""
"""
l1=[10,20,30,40,50,60,45.78]

print(l1[4])
print(l1[2:5])  # 2 start index  5 end index

print(l1[-2])
print(l1[-5 :-2] )
print(l1[ : -2])
print(l1[ 1: ])

print(l1[1:5 :2 ])  # 2 start index  5 end index 2 step 
print(l1[ : : 2])
print(l1[ : : -2])
print(l1[ : : -1])
"""

# method : 
l1=[30,10,20,30,40,50,60,45.78,30]

"""l1.append(123)
print(l1)
"""
"""l1.clear()
print(l1)
"""
"""l2 =l1.copy()
print("l2=",l2)
"""
"""l2=["apple","banana","cherry"]
l1.extend(l2)
print(l1)
"""

"""l1.insert(2,"yug")
print(l1)
"""
"""l1.pop(4)
print(l1)
"""
"""l1.remove(20)
print(l1)
"""
"""print(l1.index(30))
print(l1.index(30,1,10))
print(l1.index(30,4,10))
"""
print(l1.count(30))

"""l1.sort()
print(l1)
"""

"""l1.reverse()
print(l1)
"""
# task  :1 
"""
ask user to enter the number   store  in to the list and print odd even sum . 
5 
1 2 3 4 5 
l1=[1,2,3,4,5]

 
"""
n=int(input("enter the number : "))
l1=[] 
for i in range(n):
    ele =int(input("enter the element : "))
    l1.append(ele)
print(l1)

evensum=0
oddsum=0

for i in l1 :
    if i % 2==0 :
        evensum+=i
    else :
        oddsum+=i
print("even sum : ",evensum)
print("odd sum : ",oddsum)

#task :2 
"""
ask user to enter the number   store  in to the list and seprate pelidrome element into the list. 

l1=[122,121,134,156,141]
output :[121,141]

"""