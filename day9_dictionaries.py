#practice 1: changing a dictionary with a loop
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

for student in student_scores:
    if student_scores[student] in range(91,101):
        student_scores[student] = "Outstanding"
    elif student_scores[student] in range(81, 91):
        student_scores[student] =  "Exceeds Expectations"
    elif student_scores[student] in range(71, 81):
        student_scores[student] = "Acceptable"
    else: 
        student_scores[student] = "Fail"

print(student_scores)


#practice 2: nested dictionaries
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    new_country = {
        "country": country, 
        "visits":visits, 
        "cities" : cities
        }
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#practice 3: 
#clean screen 
import os
cls = lambda: os.system('cls')

blind_auction = {}
more_bidders = "yes"
highest_bid = 0

def add_new_entry(new_name, new_bid):
  blind_auction[new_name] = int(new_bid)
  
def get_key(val, my_dict):
  for key, value in my_dict.items():
      if val == value:
          return key

while more_bidders == "yes":
  name = input("What is your name? ")
  bid  = input("What is your bid? ")
  add_new_entry(new_name = name, new_bid = bid)
  more_bidders = input("Is there another bidder? Type yes or no ")
  cls()
else:
  current_bid = blind_auction[name] 
  if current_bid > highest_bid:
    highest_bid = current_bid
    highest_bidder = get_key(highest_bid, blind_auction)
  else: 
    pass 
    
print(f"The winner is {highest_bidder} with a bid of {highest_bid}!")
