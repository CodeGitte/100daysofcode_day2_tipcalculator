#practice1: number guessing game

#import libraries
import random

#function: number guessing game 
def number_guessing_game():
    #intro
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    #setting: difficulity level 
    while True: 
        difficulity = input("Choose a difficulty. Type 'easy' or 'hard': ") 
        if difficulity.lower() == "easy":
            attempts = 10
            break
        elif difficulity.lower() == "hard": 
            attempts = 5
            break 
        else: 
            print("Invalid input. Please enter 'easy' or 'hard'.")

    #setting: random number to be guessed 
    random_number = random.randint(1, 100) #randint(a,b) is weirdly enough inclusive b 

    #actual game: while loop runs as long as there are any attempts left over 
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        #the user has to enter an integer as a guess
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue 
        #check if guess is >, < or == to random_number
        if guess > random_number:
            attempts -= 1
            print("Too high")
            print("Guess again")
        elif guess < random_number:
            attempts -= 1
            print("Too low")
            print("Guess again")
        else:
            print(f"Yeah, you guessed right! The number is {random_number}!")
            break 
    #no attempts left over
    if attempts == 0: 
        print(f"No attempts left anymore! The number was {random_number}. Game over!")

number_guessing_game()