#practice 1: even or odd number
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else: 
    print("This is an odd number")


#practice 2: bmi calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = int(weight / (height * height))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else: 
    print(f"Your BMI is {bmi}, you are clinically obese.")

#practice 3: 
# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)

# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)


year = int(input("Which year do you want to check? "))


#maybe leap year
elif year % 4 == 0: 
    if year % 100 != 0:
        print("Leap year") 
    elif year % 400 == 0:
        print("Leap year")
    else:
        print("Not leap year")

 
#maybe leap year
if year % 4 == 0: 
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else: 
        print("Leap year")
#no leap year
else:
    print("Not leap year") 



#practice 4: pizza order bill calculator 
#Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else: 
    pass

if extra_cheese == "Y":
    bill +=1
else: 
    pass

print(f"Your final bill is: ${bill}")


# practice 5
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

names = name1 + name2

true_count = names.count("t") + names.count("r") + names.count("u") + names.count("e") 
love_count = names.count("l") + names.count("o") + names.count("v") + names.count("e") 

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")


# practice 6: little game 
print(
    """
             ((~
         ,))))))),
         )))'`')))
         (( ',' ))
          {; = ;}
     \\\  /`'v'`\  ///
      /''`\_/o\_/`''\
     /ooo    |    ooo\
    /===/    |    \===\
   /ooo/     |     \ooo\
  /===(      |      )===\
 /ooooo\_____|_____/ooooo\
/_______\===(E)===/_______\
   (()(~~~~~~~~~~~~~)())
       \           /
       |    /^\    |
       |oooo| |oooo|
       |====| |====|
       )oooo| |oooo(
      /=====| |=====\
     /oooooo| |oooooo\
    /_______| |_______\
        (__)   (__)
         ~~     ~~
    
    """
)
print("Meet Elvis!")
print("Today you have the chance to meet Elvis (the one and only)")
print("but make your decisicion wisely, because otherwise you will die :(")

#first question
dance_or_boogie = input("Do you want to dance or boogie? ")
if dance_or_boogie == "dance":
    print("Elvis doesn´t dance, he boogies. You just died :(")
else: 
    print("Boogie Woogie! Let´s boogie on!")
    cheese_or_cake = input('Ok, next question: cheese or cake? ')
    if cheese_or_cake == "cheese":
        print("Elvis hates cheese. You just died :(")
    else: 
            print("yummmmm yumm yumm cake, Elvis looooooves cake - let´s meet him!")


