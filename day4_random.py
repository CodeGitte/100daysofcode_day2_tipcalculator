#practice 1: heads or tails
import random 

zero_one = random.randrange(2)
print(zero_one)

if zero_one == 0:
    print("Tails")
else: 
    print("Heads")


#practice 2: determine who pays
import random 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
how_many = len(names)
payer = random.choice(names)
print(payer)

#practice 3: rock, paper, scissors 
import random 
options_list = [rock, paper, scissors ]

user_decision = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
computer_decision = random.choice(options_list)


if user_decision == "0":
  if computer_decision == rock:
    print("even")
  elif computer_decision == paper:
    print ("computer wins, you loose")
  else: 
    print("computer looses, you win")
elif if user_decision == "1":
  if computer_decision == rock:
    print("computer looses, you win")
  elif computer_decision == paper:
    print ("even")
  else: 
    print("computer wins, you loose")
else: 
  if computer_decision == rock:
    print("computer looses, you win")
  elif computer_decision == paper:
    print ("even")
  else: 
    print("computer wins, you loose")
    