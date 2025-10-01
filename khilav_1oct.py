# tuple : immutable sequence  ==> not changes in tuple. 

"""t1=(1,2,3,4,5,6,7,8,9,10,True,90.89,8j)
print(t1)
print(type(t1))

t2=10,20,30,40,50,60,70,80,90,100
print(t2)
print(type(t2))
"""
# built in function  : len min max sorted sum 

"""
t1=(100,2,3,4,5,6,7,8,9,10,90.89)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1)) # asc to desc 
print(sorted(t1,reverse=True)) #  desc to asc  
print(sum(t1))
"""
# slicing : 
"""
t1=(100,2,3,4,5,6,7,8,9,10,90.89)

print(t1[4])
print(t1[2 : 4])
print(t1[2 : 8 :2])
print(t1[-4])
print(t1[ : :2])
print(t1[ : :-2])
print(t1[ : :-1])
"""
# method  : 
"""t1=(100,2,3,4,5,6,7,8,9,10,90.89)

print(t1.count(2))
print(t1.index(10))
"""

# tuple to  list : 

"""t1=(1,2,3,4,[45,55,66],90)
print(t1)
t1[4].append("khilav")
print(t1)
"""

# task :1 
"""
input  :(1,2,3,4,5,6,7,8,9,10,True,90.89,8j)
ouput : (1,2,3,4,5,6,7,8,9,10,True,90.89,8j,"khilav")
"""
