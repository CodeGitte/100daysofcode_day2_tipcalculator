#import libraries
import random 
from game_data import data
from art import logo, vs



def higherlowergame(data, logo):
  """
  input: list of dictionaries, each containing 'name', 'follower_count', 'description', 'country'
  goal of game: compare two people and guess who has more followers
  """
  #showcase logo
  game_on = True
  print(logo)
  score = 0 

  A = random.choice(data)
  B = random.choice(data)

  while game_on: 
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"With B: {B['name']}, a {B['description']}, from {B['country']}.")
    while True: 
      try:
        guess_user = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess_user != "A" and guess_user != "B":
          raise ValueError
        break
      except ValueError:
        print("Invalid input. Please enter 'A' or 'B'.")

    if A['follower_count'] > B ['follower_count'] and guess_user == "A":
      score += 1 
      print(f"You are right! You're new score is: {score}")
      try: 
        A = A
        B = random.choice(data)
      except: 
        A == B
        continue 
      
    elif B['follower_count'] > A ['follower_count'] and guess_user == "B":
      score += 1 
      print(f"You are right! You're new score is: {score}")
      try: 
        A = B
        B = random.choice(data)
      except: 
        A == B
        continue

    else: 
    #B['follower_count'] > A ['follower_count'] and guess_user == "A" \
    #or B['follower_count'] < A ['follower_count'] and guess_user == "B":
      game_on = False
        

  if game_on == False: 
    print(f"Sorry, you lost. Your final score is {score}.")

higherlowergame(data, logo)



