

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random 


def deal_card():
    """returns a random card from a list of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(list_cards): 
    """returns the total sum of a list of cards 
    / in case of blackjack the return is 0
    / check for ace: if sum_cards > 21 then ace != 11 but ace = 1"""
    sum_cards = sum(list_cards)
    num_aces = list_cards.count(11)
    #check for blackjack 
    if len(list_cards) == 2 and sum_cards == 21: 
        return 0
    #check for ace, sum_cards > 21, then ace != 11 but ace = 1 
    if 11 in list_cards and sum(list_cards) > 21:
        list_cards.remove(11)
        list_cards.append(1)
        return sum(list_cards)
    else: 
        return sum_cards

def compare_scores(score1, score2):
    #f the computer and user both have the same score, then it's a draw. 
    if computer_score == user_score:
        print (f"It is a draw! You and the computer both have a score of {user_score}!")
    # If the computer has a blackjack (0), then the user loses. 
    elif computer_score == 0:
        print(f"The computer has a blackjack! You loose!")
    # If the user has a blackjack (0), then the user wins. 
    elif user_score == 0:
        print(f"You have a blackjack! You win!")
    # If the user_score is over 21, then the user loses. 
    elif user_score > 21: 
        print(f"Your score {user_score} is over 21. You loose!")
    # If the computer_score is over 21, then the computer loses. 
    elif computer_score > 21: 
        print(f"The computer score is {computer_score} is over 21. You win!")
    #If none of the above, then the player with the highest score wins.
    elif computer_score > user_score:
        print(f"The computer_score is {computer_score} and your score is {user_score}, the computer wins!")
    else: 
        print(f"The computer_score is {computer_score} and your score is {user_score}, you win!")


intro = input("Let´s start the game!")

user_cards = []
computer_cards = []
should_continue = True

#first card for both computer and user 
user_cards.append(deal_card())
computer_cards.append(deal_card())

#while loop for blackjack 
while should_continue == True: 
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    #if blackjack for user and compunter, or user_score > 21, then break 
    if user_score == 0: 
        should_continue = False
        break
    elif user_score > 21: 
        should_continue = False
        break
    elif computer_score == 0: 
        should_continue = False
        break
    
    #printing current scores (for computer score always hide last card)
    print_user_cards =', '.join(str(card) for card in user_cards)
    if len(computer_cards) == 2: 
        print_computer_cards = str(computer_cards[0])
    else:
        print_computer_cards = ', '.join(str(card) for card in computer_cards[:-1])
    print(f"These are your current cards: {print_user_cards}")
    print(f"These are the all computer`s cards except the last one: {print_computer_cards}")

    #if the user wants to continue playing "y", otherwise "n"
    if input(f"Type 'y' to continue drawing, or type 'n' to stop: ") == 'y':
        should_continue = True 
    else: 
        should_continue = False


if should_continue == False:
    #when user is done, computer should while computer_score < 17, if computer_score > 17 stop 
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    else: 
        compare_scores(user_score, computer_score)




