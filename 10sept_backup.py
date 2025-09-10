# list : mutable   ==> you can changes  in list. 

"""
l1=[1,2,3,4,5,6,7,90.90,8j,True]
print(l1)
print(type(l1))
"""
# list  access index : 
"""
start  : 0 1 2 3 4 .....   
neg : -1 -2 -3
"""
"""
l1=[1,2,3,4,5,6,7,90.90,8j,True]
l1[2] ="aashta"
print(l1)
"""

# built in function  : len  min max  sorted sum 

"""
l1=[100,2,3,4,5,6,7,90.90,900]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  # asc to desc 
print(sum(l1))
"""

# method  : 
# l1=[100,2,3,4,5,6,7,90.90,900]

"""
l1.append(456)  # add element list in last 
print(l1)
"""
"""l1.insert(4,456)
print(l1)
"""
"""l1.remove(90.90)
print(l1)
"""
"""
l1.pop(2)  # arg  ==> index number 
print(l1)
"""

"""l2=["aashta","saiyali"]
l1.extend(l2)
print(l1)
"""
"""l1.clear()
print(l1)"""

"""l2 =l1.copy()
print(l2)
"""
l1=[100,1,2,3,4,100,6,7,90.90,900,100]

"""print(l1.count(2))

print(l1.index(100))
print(l1.index(100,1,20))# start 1 index number  20 index number 
print(l1.index(100,6,20))
"""
"""l1.reverse()
print(l1)
"""

"""l1.sort()
print(l1)  # asc to desc 
"""
"""l1.sort(reverse=True)  # desc to asc 
print(l1)
"""

# slicing  : 
l1=[100,10,20,30,40,1000,60,70,90,900,110]
# index : start : 0 1 2  ==> pos  ==> l to r 
# neg index : -1 -2  == > r to l 
print(l1[3])
print(l1[ 2 :5])  # 2 starting  index  5 ending index 
print(l1[  :8])  
print(l1[2  :])  
print(l1[  : ])  
print(l1[-3])
print(l1[-3 : -9])
print(l1[-9 : -3])

print(l1[2: 8 :2])   # 2 start  index , 8 ending  index step 2
print(l1[ : : 2])
print(l1[ : : -2])
print(l1[ : : -1])



