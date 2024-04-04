from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turned_on = True

def coffee_make() :
    user_input = input(f"\n ---------------------- \nHello!\n\n1-Use the machine \n"
                       f"2-See the report\n"
                       f"3-Turn off the machine\n\n"
                       f"Please choose 1/2/3\n")


    if user_input == "1":
        chosen_coffee = input(f"What do you want to drink {my_menu.get_items()} \n")
        if chosen_coffee.lower() in ["latte","espresso","cappuccino"]:
            chosen_coffee = my_menu.find_drink(chosen_coffee)
            can_make = coffee_maker.is_resource_sufficient(chosen_coffee)

            if can_make==False:
                coffee_make()
            else:
                if money_machine.make_payment(chosen_coffee.cost):
                    coffee_maker.make_coffee(chosen_coffee)
                else:
                    coffee_make()
        else:
            print("Incorrect input. Machine is restarting")
            coffee_make()


    elif user_input=="2":
        coffee_maker.report()
        money_machine.report()

    elif user_input == "3":
        global turned_on
        turned_on=False
        print("The machine is being turned off")

    else :
        print("Incorrect entry. Machine is restarting")

while turned_on :
    coffee_make()

