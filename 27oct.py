import  random  as  r 
"""
ch = ["rock","paper","scissor"]

user_score = 0
computer_score = 0 

print("welcome to rock paper scissor game")
print("type exit to quit  the game")

while  True :
    user=input("enter your choice : (rock,paper,scissor)").lower()
    if user =="exit" :
        print("thanks for playing")
        print(f"your score is {user_score} and computer score is {computer_score}")
        break 
    if user not in  ch : 
        print("invalid choice")
        continue 
    computer =r.choice(ch)
    if user ==computer :
        print("tie")
    elif (user =="rock" and computer =="scissor" )or (user =="paper" and computer =="rock") or (user =="scissor" and computer =="paper") :
        print("user wins")
        user_score +=1
    else :
        print("computer wins")
        computer_score +=1 
        
    print("SCORE BOARD")
    print(f"your score is {user_score} and computer score is {computer_score}")
    
"""

# number  guessing game  : 
"""
computer  ==>  range  ==>  1-20   com  guess ==>18 

total_ attempt  ==>5 

1. attempt  ==>5   ==> low  
2. attempt  ==>20   ==> high 
3. attempt  ==>16   ==> low 
4. attempt  ==>12   ==> low 
5. attempt  ==>11   ==> low

you  loss  computer  guess number  is  : 18

function  : random . range(1,20 )  ==> computer   randint(1,20) 

while  /  while  true  : 
"""

print("welcome to number guessing game")
print("aapko number  guess krna he  1-20  mese")

secret_number = r.randint(1,20)  # 
attempts =0 
max_attempts = 5

while attempts < max_attempts :   # 0 < 5 
    print("attempt  ==>",attempts+1)
    guess = int(input("enter your guess  number: ")) 
    attempts +=1
    if guess <secret_number :
        print("low")
    elif guess > secret_number:
        print("high")
    else :
        print("correct .....huuhhuhh ... you win")
        break 
else :
    print("sorry you lost  not  guessing correct number.")
    print(f"the secret number is {secret_number}")
    
# word  gueesing  game  : 
"""
com_choice = ["python","java","c++","c","c#","java script","ruby","php","sql","html","css"]

user_attempts  max =5 
"""

# coin toss  : head or tail 
"""
1. head  2. tail 
t   user  loss   == > user h  ==> h  win 

"""

