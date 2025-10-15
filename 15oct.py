# filter : no changes  in  original list . 
"""
jan  -  dec  ==> fin trasaction  ==> june trac . 

l1 =["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
"""

"""
l1=[1,2,3,4,5,6,7,8,9,10,11,12]
even=[] 
odd=[] 
for i in l1 : 
    if i % 2==0 :
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)
"""
"""l1=[1,2,3,4,5,6,7,8,9,10,11,12]

a=list(filter(lambda x : x %2==0,l1))
b=tuple(filter(lambda x : x %2==1,l1))

print(a)
print(b)
"""

# map  :  given new  list 

"""l1=[1,5,8,3,9,90] 
# [5,25,40,15,45,450]

a=list(map(lambda x : x *5,l1))
print(a)
"""

#task  : 1  seperate  pelindrome  string and  store  into the  another list.using lambda function filter  or map 
"""
input : ["1221", "maam","php","java","python"] 
output  : ["1221", "maam","php"]
"""

# task :2 
"""
Write a Python program to reverse strings in a given list of string values using lambda.

Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""

# map : 

"""
l1=[1,5,7,9,2]
l2=[]
for i in l1: 
    result = i**3 
    l2.append(result)
print(l2)
"""
l1=[1,5,7,9,2]

x =tuple(map(lambda y : y **3 ,l1)) 
print(x)