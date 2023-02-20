#practice 1: parameters / calculating needed cans 
import math 
  
def paint_calc(height, width, cover):
    needed_cans = math.ceil((height * width) / cover)
    print(f"You need {needed_cans} cans")
    
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#practice 2: prime_number checker 
def prime_checker(number):
    for i in range(2,number): 
        if number % i == 0:
            is_prime = False
    if is_prime:  
        print(f"{number} is a prime number.")
    else: 
        print(f"{number} is not a prime number.")
 
n = int(input("Check this number: "))
prime_checker(number=n)

#practice 4; ceasar_cipher
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def ceasar(given_text, shift_amount, cipher_direction):
  new_text = ""
  for letter in given_text:
      position = alphabet.index(letter)
      if cipher_direction == "encode":
        new_position = position + shift_amount
      else: 
        new_position = position - shift_amount
      new_letter = alphabet[new_position]
      new_text += new_letter 
  print(new_text)

user_decision = "yes"


while user_decision == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  ceasar(given_text = text, shift_amount = shift, cipher_direction = direction)
  user_decision = input("Do you want to play again? If yes, type yes. For no, type no.")

else: 
  print("Goodbye")