#practice 1: intro to outputs
def format_name(first_name, last_name):
  first_name_capitalized = first_name.capitalize()
  last_name_capitalized = last_name.capitalize()
  return (f"Your name is {first_name_capitalized} {last_name_capitalized}")

first = input("Please enter your first name: ")
last = input("Please enter your last name: ")

format_name(first_name = first, last_name = last)

#practice 2: calculator
def add(n1, n2):
    output = n1 + n2
    print (f"{n1} + {n2} = {output}")
    return output

def substract(n1, n2):
    output = n1 - n2
    print(f"{n1} - {n2} = {output}")
    return output

def multiply(n1, n2): 
    output = n1 * n2
    print (f"{n1} * {n2} = {output}")
    return output

def divide(n1, n2):
    output = n1 / n2
    print (f"{n1} / {n2} = {output}")
    return output


number_1 = float(input("What´s the first number? "))
wanna_continue = 'y'

while wanna_continue == 'y':
    print(" + \n - \n * \n /")
    chosen_operator = input("Pick an operator: ")
    number_2 = float(input("What´s the next number? "))

    if chosen_operator == "+":
        output = add(number_1, number_2)
        number_1 = output
    elif chosen_operator == "-":
        output = substract(number_1, number_2)
        number_1 = output
    elif chosen_operator == "*":
        output = multiply(number_1, number_2)
        number_1 = output
    else: 
        output = divide(number_1, number_2)
        number_1 = output

    wanna_continue = input(f"Type 'y' to continue calculating with {output}, if not type 'n': ")
else: 
    print("Goodbye")


#another way from the course:

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()