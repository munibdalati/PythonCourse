def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, 
             "-": substract,
             "*": multiply,
             "/": divide,
             }
from art import logo
def calculator():
    print(logo)
    
    num1 = float(input("What's is the first number?: "))
    for symbol in operations:
        print (symbol)
    contine_cal = True
    while contine_cal:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's is the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
            
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.") == "y":
            num1 = answer
        else:
            contine_cal = False
            calculator()

calculator()


