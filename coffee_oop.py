from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import money_machine
print("#########<< Coffee using OOP >> ############")
is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on :
    options = menu.get_items()
    choice = input(f'What would you like? ({options})').lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
    else:
        drink=menu.find_drink(choice)
        #print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
