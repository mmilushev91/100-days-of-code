#Functions with inputs
#Functions allow us to package code into a named block which can be used
#repeatedly at a later point.

#Challenge:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Greetings")
    print("I hope I found you well")
    print("I gladly welcome you from Bulgaria")
greet()

#Functions with inputs
# When you create a function with inputs, you are defining
# a variable name that will be given to the data that is passed in.
# The name of the input variable, e.g. name in this code here:
# def greet(name): is called the parameter.
# The value of the value of the input variable, e.g. Angela when
# you call the previous greet function: greet("Angela") is called the argument.

def greeting_with_name(name):
    print(f"Hello, {name}!")
    print(f"How do you do, {name}?")
greeting_with_name("Marian")
