from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def display_operators(operators_data):
    
    for operator in operators_data:
        print(operator)

def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply, 
        "/": divide,
    }
    
    
    # print(logo)
    num1 = float(input("What is the first number: "))
        
    inner_loop_runs = True
        
    while inner_loop_runs:
        display_operators(operations)
            
        action = input("Pick operation: ")
        num2 = float(input("What is the next number: "))
            
        result = operations[action](n1=num1, n2=num2)
        print(f"{num1} {action} {num2} = {result}")
            
        num1 = result
            
        continue_with_result = input(f"Do you want to make another operation with {result} 'y' or 'n': ")
            
        if continue_with_result == "n":
            inner_loop_runs = False
            print("\n" * 20)
            calculator()
            
calculator()
