MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


# water_amount = resources["water"]
# milk_amount = resources["milk"]
# coffee_amount = resources["coffee"]


def is_enough(type_of_coffee):
    if resources["water"] < MENU[type_of_coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources["milk"] < MENU[type_of_coffee]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < MENU[type_of_coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        print(coffee(choice, (MENU[choice]["cost"])))
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]


def coffee(type_of_coffee, cost_of_coffee):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_paid = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
    print(f"You paid ${total_paid}")
    global change
    change = round(total_paid - cost_of_coffee, 2)
    print(f"Cost of coffee is: {cost_of_coffee}")
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        resources["water"] += MENU[choice]["ingredients"]["water"]
        resources["milk"] += MENU[choice]["ingredients"]["milk"]
        resources["coffee"] += MENU[choice]["ingredients"]["coffee"]

    else:
        return f"Here is ${change} in change. \nHere is your {type_of_coffee} ☕️. Enjoy!"


turning_off = False
Profit = 0
change = 0

while not turning_off:
    choice = input("What would you like? (espresso/latte/cappuccino/report): ")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        is_enough(choice)
        if change < 0:
            Profit = Profit
        else:
            Profit += MENU[choice]["cost"]

    elif choice == "off":
        print("We turned off the coffee machine")
        turning_off = True
    elif choice == "report":

        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${Profit}")
