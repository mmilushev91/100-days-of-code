def print_operators(operations_data):
    for operator in operations_data:
        print(operator)

def calculator(num1, num2, operator, operations_data):
    return operations_data[operator](num1, num2)

print("Calculator project")

operations = {
    "+": lambda a, b : a + b,
    "-": lambda a, b : a - b,
    "*": lambda a, b : a * b,
    "/": lambda a, b : a / b,
}

outer_loop_runs = True

while outer_loop_runs:
    inner_loop_runs = True
    
    first_number = float(input("What's the first number?: "))
    
    while inner_loop_runs:
        print_operators(operations)
        
        operation = input("Pick operation: ")
        second_number = float(input("What's the next number?: "))
        
        result = calculator(first_number, second_number, operation, operations)
        
        print(f"{first_number} {operation} {second_number} = {result}")
        
        first_number = result
        
        restart_inner_loop = input("Type 'y' to continue calculating with 4.0, or type 'n' to start a new calculation: ").lower()
        
        if restart_inner_loop == "n":
            inner_loop_runs = False
