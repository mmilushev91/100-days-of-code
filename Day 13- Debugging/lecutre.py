def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# 1. Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#Loopin through the numbers from 1 to 19
# 2. When is the function meant to print "You got it"?
# When i = 20
# 3. What are your assumptions about the value of i?
# i never gets to equal to 20, so the program never gets to
# print the message

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, len(dice_images) - 1)
print(dice_images[dice_num])

#2. Reproduce the bug. Some bugs are sneaky, they only occur under certain conditions. In order to debug them, we need to be able to reliably reproduce the bug and diagnose our problem to figure out which conditions trigger the bug.

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

#3. Playing computer is an important skill in debugging. You need to be able to go through your code line by line as if you were the computer to help you figure out what is going wrong.

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have entered an invalid number! Please enter a number!")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

"""4. Fix any errors (red underlines) that show up in the editor before you run your code. The warnings (yellow) are optional fixes,
sometimes it will cause a problem down the line other times it's fine and the editor just doesn't understand what you are trying to do.
Catching Exceptions
You can use a try/except block in Python to catch any exceptions that might occur. For example if you imagine there could be a chance of user error. 
You can prevent it crashing your code by anticipating it. You trap the dangerous code inside a try block and use an except block to catch any potential errors. 
Then you define what should happen when that error occurs instead of simply just crashing and stopping the code."""

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

"""5. print() is your friend. It can help expose hidden values while your code is running. In a for loop, the loop will follow some rules to perform a repeated block of code.
But during the loop it's difficult to see the intermediate values, that's a perfect example of how you can use print to expose those intermediate values and help you debug your code."""

import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

""" 6. Debugger
Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. This is normally known as the debugger. In many ways, they are like print statements on steroids.

Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

There are a couple of things that are the same in most IDEs which you should be familiar with:

Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.

Step Over - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.

Step Into - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you 
the original code for that function so you can better understand its functionality and how it relates to your problems.

Step Into My Code - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random."""

#7. Run code often
# 8. Rest 
# 9 Ask a friend
# 10. Stackoverflow
