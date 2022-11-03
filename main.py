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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# functions and variables

def sufficient_resources(coffee_toCheck):

    for items in coffee_toCheck:
        if coffee_toCheck[items] >= resources[items]:
            print(f"Sorry there isn't enough {items}")
            return False
    return True

def check_price(decimal_change,drink_chosen,user_cofee):
    if decimal_change > drink_chosen["cost"]:
        change = decimal_change - drink_chosen["cost"]
        return f'Here is ${change} in change \n Here is your {user_cofee} ☕️'
    else:
        return f'Sorry! You have insufficent funds.'

def successful_transaction(money_recieved, drink_cost):
    if money_recieved > drink_cost:
        global profit
        profit += drink_cost
        return True
    else:
        return False


def deduct_resource(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

# Coffee machine constant
isMachine_on = True

while isMachine_on is True:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ")


    if user_coffee.lower() == "off":
        isMachine_on = False
    elif user_coffee.lower() == "report":
        # prints resources that are still availible
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(profit)
    else:
        drink = MENU[user_coffee]
        sufficient_resources(drink["ingredients"])
        if sufficient_resources(drink["ingredients"]) == True:

            if user_coffee.lower() in MENU:
                print("Please Insert Coins...")
                quaters = float(input("How many quaters?: "))
                dime = float(input("How many dimes?: "))
                nickles = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))

                # Calculates user's total change & rounds to two decimal points
                totalchange_user = (quaters * .25) + (dime * .10) + (nickles * .05) + (pennies * 0.01)
                twodecimal_change = round(totalchange_user,2)
                print(twodecimal_change)

                print(check_price(twodecimal_change,MENU[user_coffee],user_coffee))

                if successful_transaction(twodecimal_change,drink["cost"]):
                    deduct_resource(user_coffee,drink["ingredients"])



