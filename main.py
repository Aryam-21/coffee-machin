MENU = {
     "espresso": {
         "ingredients": {
             "water": 50,
             "milk": 18,
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
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.0,
     },
}
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resource[item]:
            print(f"sorry there is insufficient {item}.")
            return False
    return True
def process_coin():
    total = int(input("how many quarter do you have: "))* 0.25
    total += int(input("how many dimes do you have: ")) * 0.10
    total += int(input("how many nickles do you have: ")) * 0.05
    total += int(input("how many  pennies do you have: ")) * 0.01
    return total
def is_transaction_successful(entered_money, drink_cost):
    if entered_money >= drink_cost:
        change = round(entered_money - drink_cost, 2)
        print(f"your change is ${change} take it.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry there is no enough money.")
        return False
def make_coffe(drink_name, order_ingredient):
    for item in order_ingredient:
        resource[item] -= order_ingredient[item]
    print(f"here is your {drink_name}, take it")

is_on = True

while is_on:
    choice = input("what do you want? (espresso,latte, cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"there is {resource['water']}ml water.")
        print(f"there is {resource['milk']}ml milk.")
        print(f"there is {resource['coffee']}g coffee.")
        print(f"there is {profit} profit.")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(choice, drink["ingredients"])
        else:
            is_on = False






