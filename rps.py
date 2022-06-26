# rock, paper, scissors game
#including score

import random
from tkinter import scrolledtext

cases = ['rock', 'paper', 'scissors']
scrores={"user":0,"computer":0}



user_case=input("Please enter your choice: R for Rock, P for Paper, S for Scissors: ")


if user_case == 'R' or user_case=='r':
    user_case = 'rock'
elif user_case == 'P' or user_case=='p':
    user_case = 'paper'
elif user_case == 'S' or user_case=='s':
    user_case = 'scissors'
else:
    print("Invalid input")
    
computer_case = random.choice(cases)

print("You chose: " + user_case)
print("Computer chose: " + computer_case)

if user_case == computer_case:
    print("It's a tie!")
elif user_case == 'rock':
    if computer_case == 'paper':
        print("You lose!")
    else:
        print("You win!")
elif user_case == 'paper':
    if computer_case == 'scissors':
        print("You lose!")
    else:
        print("You win!")
elif user_case == 'scissors':
    if computer_case == 'rock':
        print("You lose!")
    else:
        print("You win!")

#print (" You won " +)