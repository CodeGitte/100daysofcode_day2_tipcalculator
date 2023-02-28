from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True
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
        drink = menu.find_drink(order_name = order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            coffee_machine_on = False

    elif order == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        coffee_machine_on = False
        break

if coffee_machine_on == False:
    print("Coffee machine off!")
