
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########Deduct the required ingredients from the resources.
        if self.check_resources(order_ingredients):
            for ingredient, amount in order_ingredients.items():
                self.machine_resources[ingredient] -= amount
            print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appétit!")
            return True
        return False