from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
menu_items_list = menu.get_items().split("/")

while machine_on:
  action = input(f"What would you like? ({menu.get_items()}): ")

  if action == "off":
    machine_on = False
  elif action == "report":
    coffee_maker.report()
    money_machine.report()
    
  elif action in menu_items_list:
    drink =  menu.find_drink(action)
    
    if coffee_maker.is_resource_sufficient(drink=drink):
      if money_machine.make_payment(drink.cost):
         coffee_maker.make_coffee(drink)
