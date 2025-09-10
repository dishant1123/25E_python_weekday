"""
task 2 ask user to enter the character  and print the character in upper case and lower case and vice versa.
hint  : ascci value 

input  :a  output  :A 
input : B   output  :b 

ascci table  : 

# ord : ascci value 
"""
"""ch=input("enter the string  : ")

if ch >='A' and ch <= 'Z' :
    ch =ord(ch) +32 
    print("lower case : ",chr(ch))
else :
    ch =ord(ch) -32
    print("upper case : ",chr(ch))

"""

"""
Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:

For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill

explanation :
units         charge 
0-50           0.50 
51 -150        0.75
151 -250       1.20
251 above      1.50

units : 25   

if units > 50 :

bill = units * 0.50  = 25 * 0.50 =12.5 
surcharge = bill *0.20 =12.5 *0.20 =2.5 
total bill = bill +sur = 12.5 +2.5 =15   ==> final ans 

elif units >51 and units <=150
units   = 125
first  50 units : 50 * 0.50 =25 
75 * .75 =75 +25 = bill = 100 +sur  total bill =

units : 175   : first 50 == > 50 * 0.50 =25  ,100 *0.75 =75 
remain = 25 * 1.20 =30 

units 300   50 * 0.5 =25 , 100 * 0.75 =75 , 100 * 1.20 =120 
50 * 1.50 =75 +25 +100 +120 

"""