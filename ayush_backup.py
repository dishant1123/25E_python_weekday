"""
print("ayush")
print('study in GLS')
print('ram')
print('sita')
print('ravan')
print('laxman')
"""
# comment  in python : 
"""
1. single line comment : # 
2. multi line comment :""" """ or ''' ''' 
"""

# escape squence  character in python  : 
"""
1. \n : new line  
2. \t : tab
3.\b :backspace 
4.end = remove the white space 
"""
# ayush navlani
"""
print("ayush",end="ram")
print("navlani")
"""

# comma  create space in python : 

# print("my name is  ayush","live in ahmedabad")

# my name is  ayush . "love to play cricket".

# print("my name is  ayush.""'live in ahmedabad'")

# hey i am ayush , i need some help can you help me ?? ye's . 

# data type : 
"""
1. int  : positive  or  negative number 
2. float : decimal values pos  or  neg 
3.string  : name  , special character :# $ % ^ & *
4.boolean : true or false
5.complex number  : number  i or j   
"""

"""a = 10  # a variable   name ==> value ==>10 
print(a)
print(type(a))

b=123456789012345678234567823456789345678
print(b)
print(type(b))

c =12.45 
print(c)
print(type(c))

d="12ayush @ # $ ^ ^ & *"
print(d)
print(type(d))

e = True
print(e)
print(type(e))

f=23 +3j  # 2 part : real part :23  imaginary part :3j
g=40 +10j
print(f)
print(type(f))
print(f+g)
"""

"""
a=25
b=3 
print("divison :",a/b)
print(" floor divison :",a//b)
"""

#user input  number : 

"""a=int(input("enter the  number 1: "))
b=int(input("enter the  number 2: "))
print("sum :",a+b)
print("sub :",a-b)
print("mul :",a*b)
print("div :",a/b)
print("floor div :",a//b)
print("modular :",a%b)
"""

"""
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

l1 = ['Red', 'pink', 'brown', 'Black', 'white', 'blue',"navy blue","lite pink","dark green"]

result=[] 

for i in range(len(l1)):
    if i !=0 and i!=4 and i!=5:
        result.append(l1[i])
print(result)