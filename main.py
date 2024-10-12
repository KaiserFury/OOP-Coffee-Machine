from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_is_on=True 
menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu_item= MenuItem
while machine_is_on:
    options = menu.get_items()
    customer_ask= input(f"what would like to have ({options})")
    if customer_ask=="off":
        print("Machine is turing off")
        machine_is_on=False
    elif customer_ask=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(customer_ask)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


