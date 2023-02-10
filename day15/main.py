# Project Coffe Machine and Setup Local Development Environment

# NOTE:pycharmをお勧めしていた。

# good points of pycharm
# 1. Spell Check
# 2. More Space (You can use many windows)
# 3. Build-In Linter
# 4. Local History
# 5. View Structure(プロジェクト（ディレクト）のそばにstructureタブがありそれを押すと、関数などを目次のように見れる)
# 6. Refactor Rename（すべての名前をリファクタしてくれる。名前で右クリックしてRefactorのRenameを選択）
# 7. Todo Tracking

# TODO:何個かテスト必要。※テストのないので、正確な保証なし

import sys

sys.path.append('../utils')
from input_helper import int_input, yes_no_input
from output_helper import welcome

from data import MENU, resources 

def main():
    
    welcome('Project Coffee Machine')
    
    while True:
        order = get_order_input()
        
        if order == 'report': 
            print_report()
            continue
        
        if not is_resources_sufficient(order):
            # HACK:message
            print('Sorry, running out of ingredients')
            print("You can check resources to Type 'report' ")
            continue
            
            
        print('Please insert coins ')
        
        num_quarters = int_input('How many quarters?: ')
        num_dimes = int_input('How many dimes?: ')
        num_nickles = int_input('How many nickles?: ')
        num_pennies = int_input('How many pennies?: ')
        
        change = calculate_charge(order, num_quarters=num_quarters, num_dimes=num_dimes, num_nickles=num_nickles, num_pennies=num_pennies)
        
        print(change)
        
        # HACK: or chageがスマートでない
        if change or change == 0:
            print(f"Here is ${change} in charge.")
            print(f"Here is your {order:2} ☕ Enjoy!")
            update_resources_of_coffee_machine_by(order)
        else:
            print("Sorry That's not enough money. Money refounded.")
            continue
        
        should_continue = input("Type 'q' to exit or 'a' to get another.: ")
        
        if should_continue == 'q': break

def get_order_input():
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        options = ['report']
        for item in MENU.keys():
            options.append(item)

        if order in options: return order

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}")

def is_resources_sufficient(order):
    water_in_machine = resources["water"]
    coffee_in_machine =  resources["coffee"]
    milk_in_machine = resources['milk']
    
    nessessary_water = MENU[order]['ingredients']['water']
    nessessary_coffee = MENU[order]['ingredients']['coffee']
    nessessary_milk = MENU[order]['ingredients']['milk']
    
    if water_in_machine > nessessary_water or coffee_in_machine > nessessary_coffee  or milk_in_machine  > nessessary_milk:
        return True
    return False

# HACK:名前
def update_resources_of_coffee_machine_by(order):
    
    nessessary_water = MENU[order]['ingredients']['water']
    nessessary_coffee = MENU[order]['ingredients']['coffee']
    nessessary_milk = MENU[order]['ingredients']['milk']
    
    resources["water"] -= nessessary_water
    resources["coffee"]-= nessessary_coffee
    resources['milk'] -= nessessary_milk
    
    

# HACK:インタフェース
def calculate_charge(order, num_quarters=0, num_dimes=0, num_nickles=0, num_pennies=0):
    total = num_quarters * 0.25 
    total += num_dimes * 0.1 
    total += num_nickles * 0.05 
    total += num_pennies * 0.01
    
    price = MENU[order]['cost']
    
    change = total - price
    
    
    if change < 0:
        return False
    
    return change

    
    
    

if __name__ == '__main__':
    main()