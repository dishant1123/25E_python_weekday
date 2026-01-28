# file  handling in  python  :  txt file   
"""
1. read  : r  : exiting  open in read mode  only  
2. write :w : new file  create  + write  + exiting  open  in write   ==> overwrite
3. append :a :  new file  create  + write  + exiting  open  in write   ==> last add. 

function  : 

1.with open/ fopen : file  open  
2. close : fclose 
3. write  : f.write()
4. seek : f.seek() ==> cursor move 
"""

# write  :  new file create  + write  

"""
with open("krishna.txt","w") as f : 
    f.write("my name is  krishna.\n")
    f.write("my age is  20.\n")
    f.write("my hobby is  reading.\n")
    f.write("my dream is  to meet narendra modi.\n")
    f.close()

"""

# w mode : exiting file  + overwrite 

"""
with open("krishna.txt","w") as f :
    f.write("live in ahmedabad.")
    f.write("study  in ROYAL.\n")
    f.write("study in gandhinagar university.\n")
"""

# append  :  new file create  + write .

"""
with open("aashta.txt","a") as f : 
    f.write("my name is  aashta.\n")
    f.write("my age is  20.\n")
    f.write("my hobby is  cricket.\n")
    f.write("my dream is  to meet narendra modi.\n")
    f.close()
"""

# append  :  exiting  file + add in last.
"""with open("aashta.txt","a") as f : 
    f.write("live in ahmedabad.")
    f.write("study  in ROYAL.\n")
    f.write("study in gandhinagar university.\n")
    f.close()
"""

# read : exiting file   ==>read only  

"""with open("krishna.txt","r") as f :
    # context =f.read()  # read all content
    # context =f.readline() # read only one line.
    context =f.readlines() # read all lines list 
    print(context)
"""

# task  :1  
"""
ask user  to enter the string  and  seprate  vowel and consonant in seprate file like vowel.txt and consonant.txt

input : my name is ram.
 
"""