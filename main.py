from art import logo

def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def sub(n1, n2):
    return n1 - n2


operations = {"+": add, "-": sub, "*": multiply, "/": divide}

print(logo)
def calculation():
  cont = True
  num1 = float(input("What is your first number?\n"))
  while cont == True:
      for key in operations:
          print(key)
      operation_inp = input("Pick an operation: ")
  
      num2 = float(input("What is your next number?\n"))
  
      calculation_function = operations[operation_inp]
      answer = calculation_function(num1, num2)
  
      print(f"{num1} {operation_inp} {num2} = {answer}")
      new_calc = input(
          f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
      ).lower()
      if new_calc == "y":
          num1 = answer
      elif new_calc == "n":
          cont = False
          calculation()

calculation()
