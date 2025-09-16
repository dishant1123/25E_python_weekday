# tuple  :immutable    ==>  no changes in tuple .

"""
t1 =(1,2,3,4,5,6,7,89.78,True,8j)

print(t1)
print(type(t1))
 
t2=1,2,3,4,5,6,89.78,True,8j
print(t2)
print(type(t2))

"""
# built in function  : len  min max sorted sum 

"""
t1 =(10,2,3,4,5,6,7,89.78)

print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to desc
print(sum(t1))

print(sorted(t1,reverse=True))  # desc to asc
"""
# slicing  : 

"""
t1 =(10,2,3,4,5,6,7,89.78)

print(t1[2])
print(t1[2 :5])
print(t1[-2])

print(t1[1 :5 :2])
print(t1[ : :2])
print(t1[ : :-1])
"""

"""
t1[2] ="aashta"
print(t1)   # error  :  bcz of  tuple is  immutable . 
"""

# method  :  count  , index 

"""
t1 =(10,2,3,4,5,6,7,89.78,10)

print(t1.count(10))
print(t1.index(10))
print(t1.index(10,1,20))
"""

# convert  : 
"""
task  :1 

input  : t1=(10,2,3,4,5,6,7,89.78,10)
output  : t1=(10,2,3,4,5,6,7,89.78,10,"ved")

task  :2 

MCQ : 

t1=(1,2,3,4, [89 ,90,"aashta"],78 ,45 )
t1[4].append("ved")
print(t1)

a. error   # ved ,aashta
b. t1=(1,2,3,4, [89 ,90,"aashta","ved"],78 ,45 )  # meet 
c. t1=(1,2,3,4, [89 ,90,"aashta"],"ved",78 ,45 )
d. tupel is immutable 
ans : B
"""


