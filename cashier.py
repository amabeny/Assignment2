class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input( " how many quarters?: ")"""
        ## process_coins function
        print("Please insert coins.")
        total = 0
        total += int(input("How many large dollars?: ")) * 1.00
        total += int(input("How many half dollars?: ")) * 0.50
        total += int(input("How many quarters?: ")) * 0.25
        total += int(input("How many nickels?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ## transaction_result function
        return coins >= cost