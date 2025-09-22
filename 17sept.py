# dict : mutable   ==>  key and value   == > changes in dict . 

"""
d1={"phy":90 , "math":78}

# phy ==> key  90 value   , math ==> key 78 value 
print(d1)
print(type(d1))
"""
"""d2={90 : 89 , "maths":56}
print(d2)
print(type(d2))
"""
# add in dict : 

"""
d1={"phy":90 , "math":78}
d1["s.s"]=99
d1["phy"] =89
print(d1)
"""

#slicing  : 

"""
d1={"phy":90 , "math":78}
print(d1[0])  # dict slicing  not possible .
"""

# built in function  : len min amx  sorted sum 

"""
d1={"phy":90 ,"math":78}
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))  # asc to desc
print(sum(d1))
"""

# method  : 

# d1={"phy":90 ,"maths" :78}

"""d1.clear()
print(d1)"""

"""print(d1.keys())
print(d1.values())
print(d1.items())
"""

# print(d1.get("phy"))
"""
d2= d1.copy()
print(d2)
"""

# l1=["ved","aashta","ved","pratham"]

# {"ved":100,"aashta":100,"pratham":100}
# d2= dict.fromkeys(l1,100)
"""d2["ved"]=200
d2["ashta"]=300
d2["pratham"]=400
"""
"""print(d2)
d1.update(d2)
print(d1)
"""

# d1={"phy":90 ,"maths" :78,"che":88}

"""d1.pop("maths")  # key  remove  
print(d1)
"""

"""d1.popitem()  # last key value pair remove
print(d1)
"""

"""d1.setdefault("phy",99)
print(d1)
"""

# dict in  list  : 

d1={"phy" :[90,89,88],
    "maths":[78,67,34],
    "che":[88,89,78]}
"""print(d1)
print(d1.keys())
print(d1.values())
"""
# print(d1[1][1])
d1={"phy" :[90,89,88],
    "maths":[78,67,34],
    "che":[88,89,78]}

"""for i , j in d1. items():
    if j[0]>=89:
        print(j)
"""

# task  : 1 
"""
ask  user to enter the 3 student  name  and  marks  and store  in  the dict . 

input  :  pratham 90  aashta 91  ved 99 
output  : {"pratham" : 90 , "aashta" : 91 ," ved ": 99}

"""

"""d1={}
for i in range(3):
    name =input("enter the name  : ")
    marks =int(input("enter the  marks  : "))
    d1[name]=marks
print(d1)  # {'yash': 90, 'pratham': 45, 'krishna': 99} 
"""
# above  dict  sorted though  marks  : 
"""
output  : {"pratham" : 45 , " yash ": 90, krishna" : 99}
"""
"""sorted_value  =sorted(d1.values())
print(sorted_value)  # [45, 90, 99] 
d2={}
for k in sorted_value: # [45, 90, 99]
    for i ,j in d1.items(): # {'yash': 90, 'pratham': 45, 'krishna': 99} 
        if k ==j : 
            d2[i]=k
print(d2)
"""
# task  :3 

"""n=input("enter the  string  : ")
d1={}

for i in n:   # pratham 
    if i in d1:
        d1[i]+=1   # d1[p] =1  
    else :
        d1[i]=1
print(d1)
"""
# n=int(input("enter the number  : "))
# l2=[]
# for i in range(n):
#     element =int(input("enter the  element  : "))
#     l2.append(element)
# print(l2)
"""
oddsum=0 
evensum =0 
for i in l2 : # [1,2,4]
    if i %  2 ==0 :
        evensum +=i 
    else :
        oddsum +=i
print("evensum : ",evensum)
print("oddsum :",oddsum)
"""

n=int(input("enter the number  : "))
l2=[]
for i in range(n):
    element =int(input("enter the  element  : "))
    l2.append(element)
print(l2)
l3=[] 
for i in l2 : # [1,2,2,3,3,4,4,5,6] 
    if i not in l3 :
        l3.append(i)# l3 =[1]
print(l3)
