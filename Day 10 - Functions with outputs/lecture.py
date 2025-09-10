#Functions with outputs

#challenge: add two parameters and turn them into Pascal case
def format_name(first_name, last_name):
    """Take first_name and last_name and combines them in title case""" #adds documentation to the function
    if not first_name or not last_name:
        return "You didn't enter valid inputs!"
        
    return f"{first_name} {last_name}".title()

print(format_name(input("Enter first name: ").lower(), input("Enter last name: ").lower()))

#Docstrings """ can be used for:
#1. Adding info for a function
#2. Creating multiline comments
#3. Creating multiline strings 
