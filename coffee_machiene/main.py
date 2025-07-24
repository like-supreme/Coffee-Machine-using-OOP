from menu import Menu
from coffee_maker import CoffeeMaker
from money_machiene import MoneyMachine
#=================================================================
money_machine = MoneyMachine() #kolaylık olsun diye kullanacağım bütün classları tanımladım. 
coffee_maker = CoffeeMaker() #obje oluşturup sınıfı görebilirsin
menu = Menu()


coffee_mac_on = True
while coffee_mac_on:
    choose = input(f"What would you like? {menu.get_items()}: you can write 'off' for turnig off and 'report' for see report \n ")
    print(f"{choose} choosed. ")
    if choose == "off":
        print("Turning off...")
        coffee_mac_on = False
        break
    elif choose == "report":   
        coffee_maker.report() 
        money_machine.report()   
        coffee_mac_on = True
    else:
        drink = menu.find_drink(choose)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink) #if off kısmı ve if report kısımlarını ayrı ayrı iflerde tutmak
                    #hatalı if elif else yapısı ile yapılmalı yoksa none çevirebiliyor. 
