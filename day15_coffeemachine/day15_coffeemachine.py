#coffeemachine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Function to check if there are sufficient resources
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Oh oh, not enough {item} to make your {order}. We are sorry!")
            return False
    return True

# Function to process the coins and return change
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

# Function to check if payment is successful
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global total_money
        total_money += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


coffee_machine_on = True
total_money = 0 

while coffee_machine_on: 
    #asking the user to make a valid input 
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        #checking if the input is valid: if not, ask again 
        if order not in ("espresso", "latte", "cappuccino", "report", "off"):
            print("Sorry, I did not understand that...")
            continue
        else: 
            break

    #if the order is espresso, latte or cappuccino: check if resources are sufficient, get the coins, and make the drink 
    if order in ("espresso", "latte", "cappuccino"):
        #define ingredients for the order and costs
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            print(f"Your {order} costs ${drink['cost']}.")
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                print(f"Here is your {order}. Enjoy!")   
        else: 
            coffee_machine_on = False

    #create a report for an engineer to show how much resources are available in the coffee machine
    elif order == "report": 
        print("Water: " + str(resources["water"]) + " ml")
        print("Milk: " + str(resources["coffee"]) + " ml")
        print("Coffee: " + str(resources["coffee"]) + " g")
        print(f"Money: $"+ str(total_money))

    #if an engineer wants to turn the coffee machine off by typing "off", the program determinates     
    else: 
        coffee_machine_on = False
        break

if coffee_machine_on == False:
    print("Coffee machine off!")
    





