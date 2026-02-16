# pip install  numpy   

import  numpy as np 

"""
use : 
1. easily manupulations of array  , also  convert to array 
2. statistics functions 
3. mathematical functions 
4. linear algebra
"""

"""
a=np.array([1,2,3,4,5,6,7,8,9],dtype=int)
print(a)
print(a.ndim)  # number  of dimension
print(type(a))
"""

# slicing  : 
a=np.array([10,22,63,74,35,69,17,18,49],dtype=int)

"""print(a[2])
print(a[2:5])
print(a[2:5:2])
"""
# update  : 
"""a[2] =900
print(a)
"""
"""print(a.size)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(np.sort(a))
"""

# 2d array , size , reshape  : 

"""a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)
print(a)
print(a.shape)
print(a.size)
"""

"""
b=np.arange(1,21).reshape(5,4)
print(b)
"""

"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]]
"""

c=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16],
            [17,18,19,20]],dtype=int)


print(c[[0,1,2,3],[0,1,2,3]])
# print(c)
# print(c[0])
# print(c[2:4])   # row  slicing 
# print(c[1:3,2:4])  # 1:3  row  slicing  , 2:4 col  slicing 

# print(c[0 :4 :2,1:4 :2 ])
# print(c[:,1:4])
# print(c[::-1,])

"""
task  :1 print  corners : 

output : [[1,4],
         [17,20]]

task :2 

output  : [1,6,11,16]
         
"""

