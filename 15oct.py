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
"""l1=[1,5,7,9,2]

x =tuple(map(lambda y : y **3 ,l1)) 
print(x)
"""

"""l1 =['Red', 'Green', 'Blue', 'White', 'Black']

a =list(map(lambda x :x [ : : -1],l1))
print(a)
"""

# hw : 
"""
2. Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

3. Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.

Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height> 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}

"""

# module  : random , math cmath date time  timedelta calendar 

import random as r 

# print(r.random())  # 0-1 float value  
# print(r.randrange(1,10,2))  # 10 excluded 
# print(r.randint(1,10) )# both  values are included 

# print(r.choice([1,2,3,4,"krishna","aashta"]))
# print(r.choices([1,2,3,4,"krishna","aashta"],k=3))

"""l1=[1,2,3,4,"krishna","aashta"]
print(l1)
r.shuffle(l1)
print(l1)
"""

# game  : 
"""
rock paper scissor 

user  vs com 

randint (1,3)  randrange(1,4)

10 : for  loop  ,  while 10  : 

case : user win  

if user ==rock and computer ==rock or  user ==paper and computer ==paper or user ==scissor and computer ==scissor  :
    tie ==> use score = 0  com score =0 
    
elif u =r and  c =s  or u = s  and c =p  or u=p and c=r
    print("user wins")  use score =+1 
else :
    print("computer wins")  com score =+1
"""
