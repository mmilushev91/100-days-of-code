from art import logo

def print_operators(operations_data):
    for operator in operations_data:
        print(operator)

def calculator():
    
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    
    print(logo)
    
    first_number = float(input("What's the first number?: "))
    inner_loop_runs = True

    while inner_loop_runs:
        print_operators(operations)

        operation = input("Pick operation: ")
        second_number = float(input("What's the next number?: "))

        result = operations[operation](first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {result}")

        first_number = result

        restart_inner_loop = input(
            "Type 'y' to continue calculating with 4.0, or type 'n' to start a new calculation: ").lower()

        if restart_inner_loop == "n":
            inner_loop_runs = False
            print("\n" * 50)
            calculator()

calculator()
