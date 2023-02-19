import random

#choose random word to be guessed from a list of words
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
list_of_words = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel" ,"cat", "clam", "cobra"]
word = random.choice(list_of_words)

#creating ___ that is exactly as long as the randomly chosen word 
total_letters = len(word)
status = ""
for letter in range(total_letters):
    status += "_"
print(f"The chosen word is that long: {status}")

#while loop from here 
hangman_life = 7
hangman_pic = -1

while status != word and hangman_life > 0:
    #input user
    user_letter = input('Which letter do you choose? ')
    user_letter = user_letter.lower()
    print(f"You chose following letter: {user_letter}")

    #check if user_letter is part of word, or not
    #if yes, update the status
    #if no, do not update status but one life less, hangman picture changes 
    if user_letter in word: #e.g. d is in dog 
        print(f"Your letter {user_letter} is in the word!")
        #loop through the word to be guessed, to check where the given user_letter can update the _ (e.g. from ___ to d__ ; for user_letter == d and word==dog)
        for i, element in enumerate(word):
            if element == user_letter:
                status= status[:i] + user_letter + status[i+1:]
            else: 
                i += 1
        print(f"The current status is: {status}")
     
    else: 
        print(f"Your letter {user_letter} is not in word. Try again!")
        print(f"The current status is: {status}")
        # change hangman_life
        hangman_life -= 1
        hangman_pic += 1
        # change the updated hangman 
        print(hangmanpics[hangman_pic])

if hangman_life == 0:
    print("GAME OVER")
    print(f"The word would haven been: {word}")
else: 
    print("CONGRATS")


