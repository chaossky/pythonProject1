from hmac import compare_digest
import random
from shutil import register_unpack_format

cards=[11,2,3,4,5,6,7,8,9,10,10,10]

def deal_cards():
    chosen_card=random.choice(cards)
    ##print (chosen_card)
    return chosen_card

user_hand=[]
computer_hand=[]

def add_user_card():
    for _ in range(2):
        chose=deal_cards()
        user_hand.append(chose)

def add_computer_card():
    for _ in range(2):
        chose=deal_cards()
        computer_hand.append(chose)
        
def sum_of_card(list):
    sum=0
    for i in list:
        sum+=i
    return sum

def compare_score(a,b):
    if sum_of_card(a)>sum_of_card(b):    
        print("User won")
    elif sum_of_card(a)<=sum_of_card(b):
        print("Computer won")
    else:
        print("Draw")
        
add_computer_card()
add_user_card()

print(user_hand)   
print(sum(user_hand))
print(computer_hand)
print(sum(computer_hand))

if sum(user_hand)<21:
    ans=input("Stop or Hit: ")
    if ans=="Stop":
        compare_score(user_hand, computer_hand)
    elif ans=="Hit":
        add_user_card()
        print(user_hand)
        print(sum(user_hand))
        if sum(user_hand)<21:
            ans=input("Stop or Hit: ")
            if ans=="Stop":
                compare_score(user_hand, computer_hand)
            elif ans=="Hit":
                add_user_card()
                print(user_hand)
                print(sum(user_hand))
                if sum(user_hand)<21:
                    ans=input("Stop or Hit: ")
                    if ans=="Stop":
                        compare_score(user_hand, computer_hand)
                    elif ans=="Hit":
                        add_user_card()
                        print(user_hand)
                        print(sum(user_hand))
                        if sum(user_hand)<21:
                            ans=input("Stop or Hit: ")
                            if ans=="Stop":
                                compare_score(user_hand, computer_hand)
                            elif ans=="Hit":
                                add_user_card()
                                print(user_hand)
                                print(sum(user_hand))
                                if sum(user_hand)<21:
                                    ans=input("Stop or Hit: ")
                                    if ans=="Stop":
                                        compare_score(user_hand, computer_hand)
                                    elif ans=="Hit":
                                        add_user_card()
                                        print(user_hand)
                                        print(sum(user_hand))
                                        if sum(user_hand)<21:
                                            ans=input("Stop or Hit: ")
                                            if ans=="Stop":
                                                compare_score(user_hand, computer_hand)
                                            elif ans=="Hit":
                                                add_user_card()
                                                print(user_hand)
                                                print(sum(user_hand))
                                                if sum(user_hand)<21:
                                                    ans=input("Stop or Hit: ")
                                                    if ans=="Stop":
                                                        compare_score(user_hand, computer_hand) 
    
    
    
        
