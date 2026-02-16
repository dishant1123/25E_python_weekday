import  numpy as np

# reshape : 
"""a=np.arange(1,21) 
print(a)

b=np.arange(1,21).reshape(5,4)
print(b) 

c=np.arange(1,33).reshape(2,2,2,4)
print(c)
"""
# using random  module  : 
import  random    # random  ==> 0-1  value  , randint  ==> 0,10 

"""a=np.random.random(size=(2,4))
a=np.random.random(size=8).reshape(4,2)
print(a)

b=np.random.randint(low=-10,high=10,size=9).reshape(3,3)
print(b)

c=np.random.sample(size=10)
print(c)

d=np.random.sample(size=10).reshape(2,5)
print(d)
"""

#np.ones , np.zeros, np.full , np.full_like : 
"""
a=np.arange(1,10).reshape(3,3)
print(a)

b= np.ones(shape=(3,3),dtype=complex)
print(b)

c=np.zeros(shape=(3,3),dtype=int)
print(c)

d=np.full(shape=(3,3),fill_value=10,dtype=int)
print(d)

e= np.full_like(a,fill_value=100,dtype=int)
print(e)
"""

# diagonal  :
"""
a=np.diag([1,3,6,2,9])
print(a)
"""
# identity  :
"""
b=np.eye(4,4)
print(b)
"""

# flatten :   convert array  to 1d array . (2d array  to  1d array) it create momery. 

"""
flatten and ravel are dimension. 
its is  reduction technique  which  convert  any dimension to one dimension
"""

"""
a=np.arange(1,10).reshape(3,3)
print(a)
a1=a.flatten()
print(a1)
a[0,0] =100 
print(a)
print(a1)
"""
# ravel :  replace memory 

"""a= np.arange(1,10).reshape(3,3)
print(a)

a1=a.ravel()
print(a1)
a[0,0] =100 
print(a)
print(a1)
"""

# tranpose :

"""a=np.arange(1,10).reshape(3,3)
print(a)
print(a.T)
print(a.transpose())
"""

# maths opreation  : 

"""a= np.arange(11,20).reshape(3,3)
b= np.arange(1,10).reshape(3,3)
print(a)
print(b)

print(a+b)
print(a-b)
print(a*b)  # its  not  matrix  multiplication
print(a/b)
print(np.add(a,b))  # np.subtract , npo.mulitply, np.divide

print(np.matmul(a,b))  # matrix  multiplication
print(np.dot(a,b))     # matrix  multiplication
"""

# statistics  :

"""
b= np.arange(1,10).reshape(3,3)

print(b)
print(np.mean(b))
print(np.median(b))
print(np.std(b))
print(np.var(b))
"""

# sum  of  matrix  row wise  and column wise  :
"""
axis =0  ==> col wise 
axis =1  ==> row wise
"""

"""
b= np.arange(1,10).reshape(3,3)
print(b)

print(np.sum(b))
print(np.sum(b,axis=0))
print(np.sum(b,axis=1))
"""
