from turtle import Turtle, Screen

#creating turtle object
timmy = Turtle()
print(timmy)
#change shape of turtle
timmy.shape("turtle")
#change color of turtle
timmy.color("coral")
#move turtle forward with distance
timmy.forward(100)
#creating screen object
my_screen = Screen()
#returns the height of the screen
print(my_screen.canvheight)
#exit the screen when clicked
my_screen.exitonclick()

from prettytable import PrettyTable

#creating table object
table = PrettyTable()
#adding columns to the table
table.add_column(fieldname="Pokemon Name", column=["Pikachu", "Squirtle", "Charmander"])
table.add_column(fieldname="Type", column=["Electric", "Water", "Fire"])
table.align = "l"
print(table)
