# while  : 
"""
syntax : 

i=intial value 
while condition : 
    statement
    i =i+1

"""
# python data type : 
"""
1. string  :  immutable   ==> no changes in string .
2. list  :  mutable       ==> changes in list
3. tuple  :  immutable    ==> no changes in tuple
4. dictionary  :  mutable ==> changes in dictionary
5. set  :  mutable        ==> changes in set
"""

# 2 .  list  :  mutable ==< change in list .

l1=[10,20,30,40,50,60,70,80,90,12.56,8j,True]

"""print(l1)
print(type(l1))
"""
# list access index : 

"""
index number start  : 0,1,2,3 ...   ===> l to r 
neg index number  : -1,-2, -3 ....  ==>  r to  l 

"""
"""
print(l1[0])
print(l1[5])
"""
# change  via update element in list : 

"""l1[5] ="meet"   # 5  index number ==> replace  ==> meet insert 
print(l1)
"""

# built in function  :  len  min max sorted  sum 

"""
l1=[100,20,30,40,50,60,70,80,900,12.56]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  #asc to desc 
print(sum(l1))
"""

# methods : 
# l1=[100,20,30,40,50,60,70,80,900,12.56,100,100]

"""
l1.append(456)  # add element in list  (last)
print(l1)

l1.insert(4,789)  # insert ==> index pos , element 
print(l1)
"""
"""l1.pop(5)  #arg ==>index number  
print(l1)

l1.remove(12.56)  # specific element 
print(l1)
"""

"""l2 =l1.copy()
print(l2)
"""

"""
l1.clear()
print(l1)
"""

"""
l2=["apple","banana","cherry"]
l1.extend(l2)  # 2  list merge 
print(l1)
"""

l1=[100,20,30,40,50,60,70,80,900,12.56,100,100]

"""print(l1.index(12.56))
print(l1.index(100))
print(l1.index(100,1,20))
print(l1.index(100,11,20))
"""
# print(l1.count(100))

"""l1.sort()
print(l1)
"""
"""l1.reverse()
print(l1)
"""
"""
l1.sort(reverse=True)
print(l1)
"""

l1=[1,2,3,4,5,6,7,80,900,12.56,100,100]

for i in l1 :
    print(i,end=" ")
"""
ouptut even =[2,4,6,80,900,100,100,12,56]
        odd=[1,3,5,7]
"""