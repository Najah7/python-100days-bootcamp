from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    
    while True:
        # わかりやすさのために最初にすべてインスタンス化した
        menu = Menu()
        coffee_maker = CoffeeMaker()
        money_machine = MoneyMachine()
        
        # Taking customer order
        while True:
            choice = input(f"What would you like? ({menu.get_items()})")
            # HACK:スライス使っているのをもっとスマートに
            menu_list = menu.get_items().split('/')[:3]
            
            # reportコマンドをハンドル
            if choice == 'report':
                coffee_maker.report()
                continue
            
            # 電源Off（オーダを終了させる）
            if choice == 'off':
                print('Bye👋')
                exit()
            
            # バリデーション
            if choice in menu_list:break
            
        # get drink object by customer order
        ordered_drink = menu.find_drink(choice)
        
        # check condition of the coffee maker  
        if not coffee_maker.is_resource_sufficient(ordered_drink): break
        
        # payment process
        is_accepted = money_machine.make_payment(ordered_drink.cost)
        
        
        if is_accepted: coffee_maker.make_coffee(ordered_drink)
            
            
if __name__ == '__main__':
    main()