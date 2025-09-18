# break  ,continue ,pass : 

#break  :
"""
for i in range(10):
    if i==5 :
        break
    print(i,end=" ")
"""

# contunie : 
"""for i in range(10):
    if i==5 :
        continue
    print(i,end=" ")

"""
# pass: 
"""
for i in range(10):
    if i==5 :
        pass 
    print(i,end=" ")
"""

#while  syntax : 
"""
i = intial value 
while con : 
    print(i)
    i+=1 
"""
  
# 1-100 : 
"""i=1 
while i <=100 : 
    print(i,end=" ")
    i+=1  
"""

# while true  : 
"""i=1 
while True : 
    print(i,end=" ")
    i+=1 
    if i==10 :
        break 
"""

# calculator : 

"""while True :
    a=int(input("enter the  number 1 :"))
    b=int(input("enter the  number 2 :"))
    while True :
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5. new number")
        print("6.exit")
        c=int(input("enter the operation :"))
        match c :
            case 1 :
                print(a+b)
            case 2 :
                print(a-b)
            case 3 :
                print(a*b)
            case 4 :
                print(a/b)
            case 5 :
                break
            case 6 :
                print("exit byyeess")
                break
            case _ :
                print("invalid operation")
    break 
"""

# list  : mutable  == >  sequence 

"""
l1=[1,2,45,3,4,5,6,90,89.04,9j,True]
print(l1)
print(type(l1))
"""
# element  : index 
"""
l1=[1,2,45,3,4,5,6,90,89.04,9j,True]
print(l1[6])
"""
# update  : 
"""
l1[4] ="pratham"
print(l1)
"""

# built  in function  : len  min max sorted sum 

"""l1=[1,2,45,3,4,5,6,90,89.04]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1)) # asc to desc 
print(sorted(l1,reverse=True)) # desc to asc
print(sum(l1))
"""
# method : 
l1=[1,2,45,3,4,5,6,90,89.04]

"""l1.append(100)
print(l1)

l1.insert(2,"harshil")
print(l1)
"""
"""l1.pop(2) # index number 
print(l1)
"""
"""l1.remove(45)
print(l1)
"""
"""
l2=["aaryan","pratham","ved","ashta"]
l1.extend(l2)
print(l1)
"""
"""l1.clear()
print(l1)"""

"""l2=l1.copy()
print(l2)
"""
l1=[1,2,45,3,4,5,6,90,89.04,45]

"""
print(l1.index(45))
print(l1.index(45,3,20))
"""
"""l1.sort()
print(l1)
"""
"""l1.reverse()
print(l1)
"""
# slicing  :

"""l1=[10,20,45,30,40,50,60,90,89.04,45]

print(l1[3])
print(l1[3 :5])
print(l1[ :5])
print(l1[1 : ])
print(l1[-3])
print(l1[-5 :-3])

print(l1[3 : 8 :2])
print(l1[  :  :2])
print(l1[  :  :-2])
print(l1[  :  :-1])
print(l1[  :  :1])
"""

# tuple  : immutable  == >  sequence

"""
t1=(1,2,45,3,4,5,6,90,89.04)
print(t1)
print(type(t1))

t2=1,2,45,3,4,5,6,90,89.04
print(t2)
print(type(t2))
"""
# built in function  : len  min max sorted sum

"""
t1=(1,2,45,3,4,5,6,90,89.04)

print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1)) # asc to desc
print(sorted(t1,reverse=True)) # desc to asc
print(sum(t1))
"""

# slicing : 
t1=(1,2,45,3,4,5,6,90,89.04)

# method  : 

"""
print(t1.index(45))
print(t1.count(45))
"""
# convert tuple  to  list : 

t1=(1,2,45,3,4,5,6,90,89.04)

l2 =list(t1)
print(l2)
l2.append("pratham")
print(tuple(l2))