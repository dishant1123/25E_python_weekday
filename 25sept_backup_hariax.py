# tuple  :  immutable  ==>  no changes in tuple .

"""t1=(1,2,3,4,5,6,7,89.78,True,8j)
print(t1)
print(type(t1))

t2=1,2,3,4,5,6,89.78,True,8j
print(t2)
print(type(t2))

"""

# built in function  : len  min max sorted sum

"""
t1=(10,2,3,4,5,6,7,89.78)

print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to desc
print(sorted(t1,reverse=True))  # desc to asc
print(sum(t1))
"""

# update  : 
"""l1=[1,2,3,4]

l1[2]="hariax"
print(l1)
"""
"""
t1=(1,2,3,4)
t1[2]="hariax"
print(t1)  # not possible bcz tuple is immutable
"""

# slicing : 
"""
t1=(10,2,3,4,5,6,7,89.78)

print(t1[2])
print(t1[2 : 5])
print(t1[ : 9])
print(t1[1 : ])
print(t1[-2])

print(t1[2 : 8 :2])
print(t1[ :  :2])
print(t1[ :  :-2])
print(t1[ :  :-1])
"""

# method  : 

"""t1=(10,2,3,4,5,6,7,89.78,10,1,10)

print(t1.count(10))
print(t1.index(10))
print(t1.index(10,1,10))
print(t1.index(10,9,11))
"""

"""
t1=(1,2,3,4, [89 ,90,"aashta"],78 ,45 )
t1[4].append("ved")
print(t1)
"""

# dict :mutable key value   pair  ==>  changes in dict .

"""
d1={"phy" :90 , "maths":78}
# phy key value  90   maths key value 78
print(d1)
print(type(d1))

d2={90:67 , 56:"maths"}
print(d2)
"""
"""
d3= {"phy":[89,78,56,34] , "maths":[78,67,34] , "che":[88,89,78]}
print(d3)
"""

# update  , add:
"""
d1={"phy" :90 , "maths":78}
d1["che"] =88
d1["phy"] =77
print(d1)
"""
# method : 

d1={"phy" :90 , "maths":78}

"""
d1.clear()
print(d1)
"""
"""
print(d1.keys())
print(d1.values())
print(d1.items())
"""
d1={"phy" :90 , "maths":78}

# print(d1.get("phy"))
"""l1=["het","vyom","hariax"]
# {"het":100,"vyom":100,"hariax":100}

d2 =dict.fromkeys(l1,100)
print(d2)
d2["het"]=90 
d2["vyom"]=89
d2["hariax"]=88
print(d2)

d1.update(d2)
print(d1)
"""

# d1.pop("phy")
# print(d1)
d1={"phy" :90 , "maths":78,"ss" :99}

# d1.popitem()
# print(d1)
"""
d1.setdefault("che",90)
print(d1)
"""

# slicing  : 

print(d1[0])  # dict slicing  not possible .