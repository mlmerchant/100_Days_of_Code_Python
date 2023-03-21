from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

powered_on = True
selection = None

while powered_on:
    selection = None
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        powered_on = False
    else:
        selection = menu.find_drink(choice)

    if selection:
        if coffee_maker.is_resource_sufficient(selection):
            if money_machine.make_payment(selection.cost):
                coffee_maker.make_coffee(selection)











