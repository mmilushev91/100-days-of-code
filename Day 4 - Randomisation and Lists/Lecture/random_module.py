#Random module

#modules contain code that is written in other files and can be used
#in the main file by importing and use name of the module. and then
#the module of the function or variable we want to use

import random 

#randint(a, b) generates random integer between a and b inclusive
random_integer = random.randint(1, 10)

#random() generate floating point number between 0 and 10 not inclusive 10
random_number_0_1 = random.random() * 10

#uniform(a, b) generate floating point number between a and b inclusive

#challenge: write program that randomly generates heads or tails

random_number = random.randint(0, 1)

if random_number:
    print("Tails")
else:
    print("Heads")
