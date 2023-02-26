MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def generate_report(materials, cash):
    """Generates a report of materials and cash."""
    print(f"Water: {materials['water']}ml")
    print(f"Milk: {materials['water']}ml")
    print(f"Coffee: {materials['coffee']}g")
    print(f"Money: ${cash:.2f}")


def count_change():
    """Asks for change and then returns a sum."""
    money_in = 0
    money_in += int(input("how many quarters?: ")) * .25
    money_in += int(input("how many dimes?: ")) * .1
    money_in += int(input("how many nickles?: ")) * .05
    money_in += int(input("how many pennies?: ")) * .01
    return money_in


def check_resources(selection, stock):
    """verifies that enough stock exists to serve a selection."""
    if selection['water'] > stock['water']:
        return "water"
    elif selection['coffee'] > stock['coffee']:
        return "coffee"
    elif 'milk' not in selection.keys():
        return "OK"
    elif selection['milk'] > stock['milk']:
        return "milk"
    else:
        return "OK"


# Start with no money.
money = 0

# Program main loop
choice = "N/A"
while choice != "off":
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        generate_report(resources, money)
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        resources_verification_code = check_resources(MENU[choice]["ingredients"], resources)
        money_from_customer = count_change()
        if not resources_verification_code == "OK":
            print(f"Sorry there is not enough {resources_verification_code}.")
        elif money_from_customer < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            # Manage the money
            change_for_customer = money_from_customer - MENU[choice]["cost"]
            money += money_from_customer - change_for_customer
            # Deduct used Resources
            resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
            if 'milk' in MENU[choice]["ingredients"].keys():
                resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["coffee"]
            # Deliver the product
            print(f"Here is ${change_for_customer:.2f} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")




