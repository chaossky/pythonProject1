
import random
user_cards=[]
computer_cards=[]

def deal_card():
    """
        Return a random card from the deck using the random.choice function
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """
        Take a list of cards and return the score calculated from the cards
    """
    if sum(cards)==21 and len(cards)==2:
        return 0;
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score, computer_score):
    """
        Compare the scores of the user and computer and return the winner
    """
    if user_score>21 and computer_score>21:
        return "Your went Over.You Lose!?"
    
    if user_score==computer_score:
        return "Draw!!! ?"
    elif computer_score==0:
        return "Lose, opponent has blackjack ?"
    elif user_score > 21:
        return "You went over. You lose ?"
    elif computer_score > 21:
        return "Opponent went over. You win ?"
    elif user_score > computer_score:
        return "You win ?"
    else:
        return "You lose ?"

def play_game():
    print("Welcome to Blackjack!?")

    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
    # call the deal_card function and add the card to the user_cards 
    # then sum the cards and print the score
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f" Your cards are {user_cards}, your score is {user_score}")
        print(f" Computer's first cards are {computer_cards[0]}, computer's score is {computer_score}")
    # check if the user_score and computer_score
    # then decide the results of the game
        if user_score==0 or computer_score or user_score>21:
            is_game_over=True
        else:
            # ask if the user wants to hit or stay
            user_should_deal:input("Type 'y' to get another card, type 'n' to pass.")
        if user_should_deal=='y':
            user_cards.append(deal_card())
        else:
            is_game_over=True

    

#Hint 12: Once the user is done, it's time to let the computer play. 
# The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    
    print (f" Your final hands are {user_cards}, final score is {user_score}")
    print (f" Computer's final hands are {computer_cards}, final score is {computer_score}")
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    print (compare_score(user_score, computer_score))
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

