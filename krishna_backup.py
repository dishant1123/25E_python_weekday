# pattern  : 

"""
1.          2.          3.          4.          5.          6. 
 
* * * * *   *          * * * * *    1           5 4 3 2 1   1 2 3 4 5 
* * * * *   * *        * * * *      1 2         5 4 3 2     2 3 4 5
* * * * *   * * *      * * *        1 2 3       5 4 3       3 4 5
* * * * *   * * * *    * *          1 2 3 4     5 4         4 5
* * * * *   * * * * *  *            1 2 3 4 5   5           5
"""
# 1: 
"""
for  i in range(1,6): 
    for j in range(1,6):
        print("*",end=" ")
    print()
"""
#2 :
"""for  i in range(1,6): 
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
# 3 : 
"""for  i in range(1,6): 
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""

#6 :
"""for  i in range(1,6): 
    for j in range(i,6):
        print(j,end=" ")
    print()
"""

"""
7.         8.           9.          10. 
  
* * * * *   * * * * *         *      * 
  * * * *    * * * *        * *     * *
    * * *     * * *       * * *    * * * 
      * *      * *      * * * *   * * * *
        *       *     * * * * *  * * * * *
"""
# 7
"""for  i in range(1,6):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""
#8
"""for  i in range(1,6):
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""

#9 :

"""
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

#10 : 
"""
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

"""for i in range(1,5):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for  i in range(1,6):
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""

"""
11.
* * * * *
*       *
*       *
*       *
* * * * *
"""
"""for  i in range(1,6): 
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:    
             print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

# list  :  mutable  ==> changes in list : 

"""
l1 =[1,2,3,4,5,6,7,12.90,True,8j]
print(l1)
print(type(l1))
"""
# list element  access index : 
"""
index num start with  :0 1 2  ...  l to  r  
negative  index num : -1 ,-2     r ot  l 
"""

# built in function  :  len  min max sorted  sum

"""
l1 =[10,2,3,4,5,6,7,12.90,900]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))
print(sum(l1))
"""

# list  element  update  : 
"""
l1 =[10,2,3,4,5,6,7,12.90,900]
l1[3]="krishna"
print(l1)
"""

# method  : 
l1 =[10,2,3,4,5,6,7,12.90,900,10,10]

"""l1.append(456)
print(l1)
"""
"""l1.insert(3,80)
print(l1)
"""
"""l1.remove(12.90)
print(l1)
"""
"""l1.pop(3)
print(l1)
"""
"""l2=l1.copy()
print(l2)
"""
"""l1.clear()
print(l1)
"""

"""l1.sort()
print(l1)
"""
"""l1.reverse()
print(l1)
"""
"""l2= ["apple","banana","cherry"]
l1.extend(l2)
print(l1)
"""

"""print(l1.index(12.90))
print(l1.index(10))
print(l1.index(10,1,20))
"""
# slicing : 
l1 =[10,20,30,40,50,60,70,12.90,900,180,190]

"""print(l1[5])
print(l1[2 :5])  # start  2 , 5 end 
print(l1[ :5])  # start  2 , 5 end 
print(l1[ 1:])  # start  2 , 5 end 
print(l1[  : ])  # start  2 , 5 end 
"""
print(l1[2 :8:2])  # start  2 , 8 end step 2  
print(l1[ : : 2])
print(l1[ ::-2])  # start  2 , 8 end step 2  
print(l1[-1])
print(l1[ ::-1])  # start  2 , 8 end step 2  
