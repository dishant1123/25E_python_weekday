# list comprehension : 

"""l1=[1,2,3,4,5,66]
print(l1)
"""

# list  in list : 

l1=[[1,2,3],
    [4,5,66],
    [7,8,9]]
"""
[1,2,3]  ==> 0   
[4,5,66] ==> 1
[7,8,9]  ==> 2

components : 
 r c   
(0,0) 1   (0,1) 2   (0,2) 3
(1,0) 4   (1,1) 5   (1,2) 66 
(2,0) 7   (2,1) 8   (2,2) 9

"""
"""print(l1)
for i in l1:
    print(i)
"""
# slicing :
"""
l1=[[1,2,3,56,89],
    [4,5,66,45,77],
    [7,8,9,99,11],
    [22,33,44,55,60]]   # 4*5   matrix : 
"""
# print(l1[0])
# print(l1[0][2])
# print(l1[1][2:4])
# print(l1[2][1 :-1])
# print(l1[3][1 :4 :2])
# print(l1[1][  : :-2])
# print(l1[2][  : :-1])

l1 =[[1,2,3],
     [4,5,6],
     [7,8,9]]
# transpose matrix : 
"""
l1=[[1,4,7],
    [2,5,8],
    [3,6,9]]
"""
"""for i in range (len(l1[0])) : # 1,2,3  
    l2=[]
    for j in range(len(l1)):  # 3 
        l2.append(l1[j][i])
    print(l2)
"""

# print  row  wise  col  wise  sum  : 
"""
1 row sum  : 6 
2 row sum  : 15
3 row sum  : 24 
1 col sum : 12 
2 col sum : 15 
3 col sum : 18
"""