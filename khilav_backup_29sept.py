# tuple  :  immutable sequence of any data type

"""t1=(1,2,3,4,5,6,45.78,8j,True)
print(t1)
print(type(t1))

t2 =1,2,3,4,5,6,45.78,8j,True
print(t2)
print(type(t2))
"""

# built in function  :  len min max sorted sum 

t1=(100,20,30,40,50,60,45.78)

"""
t1[2] ="khilav"
print(t1)  # error : tupe is immutable
"""
"""print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))# asc to desc order
print(sorted(t1,reverse=True))# desc to asc order
print(sum(t1))
"""

# slicing :
t1=(100,20,30,40,50,60,45.78)

"""print(t1[4])
print(t1[2 :5])
print(t1[-5])
print(t1[ :5])
print(t1[2 :])

print(t1[1 :8 :2])  # 1 start  index  8  index  2 step 
print(t1[  : :2])  
print(t1[  : : -2])  
print(t1[  : : -1])
"""  

# method : 
"""
t1=(40,100,20,30,40,50,60,45.78,40)


print(t1.count(30))
print(t1.index(40))
print(t1.index(40,1,9))
print(t1.index(40,5,9))

"""

# convert in to the list  : 

t1=(40,100,20,30,40,50,60,45.78,40)
# output  : (40,100,20,30,40,50,60,45.78,40,"khilav")

l1 =list(t1)
l1.append("khilav")
print(tuple(l1))