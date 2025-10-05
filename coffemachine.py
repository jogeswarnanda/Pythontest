from tarfile import OutsideDestinationError

profit = 0
resource = {
    "Water": 300,
    "Milk": 500,
    "Coffee": 76,
    "Money":2.5
}

MENU = {
    "expresso": {
        "ingredients": {
            "Water": 50,
             "Coffee": 18,
        }, 
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
             "Milk": 150,
             "Coffee": 24,
        }, 
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
             "Milk": 100,
             "Coffee": 24,
        }, 
        "cost": 3.0,
    }
}

def is_resource_sufficient(order_ingredients):
    print(order_ingredients)
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
        
def process_coins():
    """ returns the total when coins inserted """
    print("Please insert coins..")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many Dimes? ")) * 0.1
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many oennies? ")) * 0.01
    return total

def is_transaction_sucessful(money_received, drink_cost):
    """Return true when payment accepted, else retuen false"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your change..${change} .")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money. MOney refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print("Here is your ☕️..Enjoy !!")


is_on = True
while is_on :
    choice = input('What would you like?(espresso/latte/cappuccino)').lower()
    if choice == 'off':
        is_on = False
        print("Machine off")
    elif choice == 'report':
        print(f"Water: {resource['Water']} ml")
        print(f"Milk: {resource['Milk']} ml")
        print(f"Cofee: {resource['Coffee']} gm")
        print(f"Profit: {profit} $")
    else:
        drink = MENU[choice]
        #print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            money_received = process_coins()
            print(money_received)
            if is_transaction_sucessful(money_received,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

            




