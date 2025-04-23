import art

# functions defining common operations
def addition(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Made a dictionary containing all operations and their keys as follows
operations = {
    "+": addition,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Building the actual calculator
def calculator():
    print(art.logo)                                     #print the art logo immediately
    should_accumulate = True                            #default accumulate values from initial startup
    n1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)            # if new calculations have it show 20 blank lines and restart calculator
            calculator()

calculator()
