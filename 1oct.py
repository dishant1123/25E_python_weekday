# set : mutable ,  no repeation allowed in set. , unordered

"""s1={1,2,3,4,5,6,7,8,8,9,9,10}
print(s1)
"""
# duplicate remove  in list using set : 
"""l1=[1,2,3,4,5,6,7,8,8,9,9,10]
s2 =set(l1)
print(list(s2))
"""

# empty set : 

"""s2=set()
print(s2)
print(type(s2))
"""

# built in function  :   len  min max sorted sum 
"""
s1={100,2,3,4,5000,6,7,8,8,9,9,1000}

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))  # asc to desc 
print(sorted(s1,reverse=True))  # desc to asc 
print(sum(s1))
"""

# slicing :  not  possible in set because set is unordered.
"""
s1={100,2,3,4,5000,6,7,8,8,9,9,1000}
 
print(s1[4])
print(s1[2:6])
"""
# method  : 

# s1={100,2,3,4,5000,6,7,8,8,9,9,1000}

"""s1.add("ved")
print(s1)
"""
"""s1.clear()
print(s1)
"""
"""s2=s1.copy()
print(s2)
"""
"""s1.pop()
print(s1)
"""
"""s1.remove(5000)
print(s1)
"""
"""s2={"ved","harix"}
s1.update(s2)
print(s1)"""

"""
s1={1,2,3,4}
s2={3,4,5,6,7}
s3={1,2,3,4,5,6,7,8,9}
"""
"""print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # s1-s2 
print(s2.difference(s1))  # s2-s1 

print(s1.symmetric_difference(s2))

"""
"""print(s1.intersection(s2))
print(s1)
s1.intersection_update(s2)
print(s1)
"""
"""print(s1.difference(s2))  # s1-s2 
print(s1)
s1.difference_update(s2)
print(s1)
"""
"""s1.symmetric_difference_update(s2)
print(s1)
"""

s1={100,2,3,4,5000,6,7,8,8,9,9,1000}

"""s1.remove(500000)
print(s1)
"""
"""s1.discard(500000)
print(s1)
"""

# frozen set : immutable set , no changes allowed in frozen set
"""
fz =frozenset({1,2,3,4,5,6,7,8,8,9,9,10})
print(fz)
print(type(fz))

"""
s1={1,2,3}
s2={1,2,3,4,5,6,7}
s3={1,2,3,4,5,6,7,8,9}

print(s1.isdisjoint(s2))
print(s1.issubset(s2))

print(s3.issuperset(s1))
print(s3.issuperset(s2))
