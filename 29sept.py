# count  : 

s1="my name is ved patel."

"""print(s1.count("e"))
print(s1.count("e",10,20))

print(s1.startswith("my"))
print(s1.endswith("."))
print(s1.endswith("patel."))

"""
"""l1=["my","name","is","ved","patel","."]
# my name is ved patel. 
s2 =" ".join(l1)
print(s2)
"""
s2="happydiwalI20oct"

"""print(s2.isalpha())
print(s2.isalnum())
"""
"""s3="1234"
print(s3.isdigit())
"""
"""s4="٠١٢٣٤٥" 
print(s4.isdecimal())
"""
"""s5="MY NAME IS VED PATEL."
print(s5.islower())
print(s5.isupper())
"""

# task  : 1 
"""
Write a python program that take one input string and in output count the no of words,
Find No of letters in String,Find the longest word in the String.
For Example:-
Input:-This is the python program
Output:-No of Words=5
	    No of letters=26(including whitespace)
	    Longest Word=program
"""

s1="This is the python program"

count_words = len(s1.split())  # ["This", "is", "the", "python", "program"]
print("No of Words=",count_words)

number_of_letters = len(s1)  # 26
print("No of letters=",number_of_letters)

longest_word = max(s1.split(),key=len)
print("Longest Word=",longest_word)

# in KEY  you have to any built-in function or method ==> key =sorted ,key =sum 

# task  :2 
"""
Write a Python program to reverse words in a string. 
iniput  : "The quick brown fox jumps over the lazy dog." 
ouput  : "dog  lazy the over jumps fox brown quick The"
"""