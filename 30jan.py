"""
1.r+  : read +write   + exiting  file  
2.w+  : new  file create  +  write  + exiting  file   ==> overwrite 
3.a+  : new  file create  +  write  + append  + exiting  file   ==> append

seek() ==> cursor move  
"""

# r + : 

"""with open("krishna.txt","r+") as f:
    f.write("my name is krish")
    f.seek(0)
    context =f.read()
    print(context)
    f.close()
"""

# w+ : 

"""
with  open("aashta.txt","w+") as f:
    f.write("my name is krish.\n")
    f.write("study in ROYAL.\n")
    f.write("study in gandhinagar university.\n")
    f.seek(0)
    context =f.read()
    print(context)
    f.close()
"""

# a+ : 
"""with  open("aashta.txt","a+") as f:
    # f.write("my name is krishna.\n")
    # f.write("live in ahmedabad.\n")
    # f.write("study in NFSU.\n")
    f.seek(0)
    context =f.read()
    print(context)
    f.close()
"""


#task :1 
"""
Write a Python program to read a text file and do following: 
1. Print no. of words 
2. Print no. statements    ==> friend.txt 

Friends are crazy, Friends are naughty !
Friends are honest, Friends are  best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !
"""

# task :2 
"""
Write a Python program to reverse the content of a one file and store it in second file and also convert content of second 
file into uppercase and store it in third file and also count number of Vowels in third file and also print only 2nd line from 
the content of third file.

Examples:
If data file one contains the following data:
Friends are crazy, Friends are naughty !
Friends are honest, Friends are  best !
Output 1:
! tseb  era sdneirF ,tsenoh era sdneirF
! ythguan era sdneirF ,yzarc era sdneirF

Output 2:
! TSEB  ERA SDNEIRF ,TSENOH ERA SDNEIRF
! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF

Output 3:
Vowels = 22

Output 4:
! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF
"""

