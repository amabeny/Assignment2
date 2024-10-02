import data
import cashier
import sandwich_maker

from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()


def main():
    ###  write the rest of the codes ###
    print("Welcome to the Sandwich Maker!")
    sandwich_size = input("Please choose a sandwich size (small, medium, large): ").lower()

    if sandwich_size not in recipes:
        print("Invalid sandwich size. Please try again.")
        return

    order_ingredients = recipes[sandwich_size]["ingredients"]
    cost = recipes[sandwich_size]["cost"]

    coins = cashier_instance.process_coins()
    if cashier_instance.transaction_result(coins, cost):
        if sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients):
            print(f"Here is your {sandwich_size} sandwich. Enjoy!")
        else:
            print("Sorry, we don't have enough ingredients to make your sandwich.")
    else:
        print("Insufficient payment. Please try again.")

if __name__=="__main__":
    main()
