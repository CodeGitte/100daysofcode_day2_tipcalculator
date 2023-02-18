#practice 1: calculating average student height from a list without using sum() and len()
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#how many without using len() function
i = 0
for student_height in student_heights:
    i += 1
print(i)

#summing without using the sum() function
total_height = 0
for student_height in student_heights:
    total_height += student_height
print(total_height)

average_height = round(total_height / i)
print(average_height)

#practice 2: printing out the highest score 
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores: 
    if score > highest_score: 
        highest_score = score
    else: 
        pass 

print(f"The hightest score in the class is: {highest_score}")

#practice 3: only print even numbers between 1 and 100: 
total_sum = 0
for i in range(1,101):
    if i % 2 == 0:
        total_sum += i 
    else: 
        pass

print(total_sum)

#practice 4: FizzBuzz
for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0: 
        print("Buzz")
    else:
        print(i)

        

#practice 5: Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chosen_letters = random.choices(letters, k = nr_letters)
chosen_symbols = random.choices(symbols, k = nr_symbols)
chosen_numbers = random.choices(numbers, k = nr_numbers)
pre_password = chosen_letters + chosen_symbols + chosen_numbers
print(pre_password)
random.shuffle(pre_password)
print(pre_password)
password = "".join(pre_password)
print(password)