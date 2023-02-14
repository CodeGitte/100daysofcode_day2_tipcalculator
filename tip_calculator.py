#Tip calculator 
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
chosen_percentage_tip = int(input("What percentage tip would you like tot give? 10, 12, or 15?"))
amount_people = int(input("How many people to split the bill?"))
total_tip = chosen_percentage_tip / 100 * total_bill
amount_per_person = round(((total_bill + total_tip) / amount_people), 2)
print(f"Each person should pay: ${amount_per_person}")