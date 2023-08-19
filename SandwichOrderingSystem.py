class Sandwich:
    def __init__(self, sandwich_type):
        self.sandwich_type = sandwich_type
        self.price = 6.99
        self.bread = None
        self.toasted = False
        self.cheese = None
        self.spread = None
        self.toppings = []
        self.additions = []

    def set_bread(self, bread_type):
        self.bread = bread_type

    def set_toasted(self, toasted):
        self.toasted = toasted

    def set_cheese(self, cheese_type):
        self.cheese = cheese_type
        self.price += 0.70

    def set_spread(self, spread_type):
        self.spread = spread_type

    #def get_toasted_status(self):


    def add_topping(self, topping_type):
        self.toppings.append(topping_type)

    def add_addition(self, addition_type):
        self.additions.append(addition_type)
        if addition_type == "Extra Cheese":
            self.price += 0.70
        elif addition_type == "Smoked Bacon":
            self.price += 1.40
        elif addition_type == "Extra Meat":
            self.price += 2.00

    def getPrice(self):
        return self.price

    def sandwich_status(self):
        sandwich  = self.sandwich_type
        if self.bread:
            sandwich += " on " + self.bread
        if self.toasted:
            sandwich += " toasted"
        if self.cheese:
            sandwich += " with " + self.cheese + " cheese"
        if self.spread:
            sandwich += " and " + self.spread
        if self.toppings:
            sandwich += " with " + ", ".join(self.toppings)
        sandwich += " - $" + str(round(self.price, 2))
        return sandwich

    def __str__(self):
        return self.sandwich_status()

class Beverage:
    def __init__(self, beverage_type):
        self.beverage_type = beverage_type
        self.price = 0

    def getPrice(self):
        return self.price

    def beverageStatement(self):
        return self.beverage_type + " - $" + str(self.price)

    def __str__(self):
        return self.beverageStatement()


class Order:
    def __int__(self):
        self.sandwich = None #These are set to none because we are going to set them during the ordering inputs
        self.beverage = None

    def set_sandwich(self, sandwich):
        self.sandwich = sandwich

    def set_beverage(self, beverage):
        self.beverage = beverage

    def getTotal(self):
        total = 0
        if self.sandwich:
            total += self.sandwich.getPrice()
        if self.beverage:
            total += self.beverage.getPrice()
        return round(total, 2)

    def orderStatements(self):
        order = "" # this order string initizes a blank string
        if self.sandwich:
            order += str(self.sandwich) + "\n"
        if self.beverage:
            order += str(self.beverage) + "\n"
        order += "Total: $" + str(self.getTotal())
        return order

def sandwichChoices():
    print("Enter your desired sandwich:")
    print("Turkey")
    print("Ham")
    print("Roast Beef")
    print("Tuna Fish Salad")
    print("Roasted Portabella Mushroom")
    print()

def breadChoices():
    print("Enter your desired bread")
    print("White")
    print("Multigrain")
    print("Rye")
    print()

def cheeseChoices():
    print("Enter your desired cheese: ")
    print("American")
    print("Provolone")
    print("Swiss")
    print("Cheddar")
    print("Pepper Jack")
    print()

def spreadChoices():
    print("Enter your desired spread: ")
    print("Mayo")
    print("Spicy mustard")
    print("Honey mustard")
    print("Buffalo")
    print("Chipotle")
    print("Horseradish")
    print("Garlic aioli")
    print()

def toppingChoices():
    print("Enter your desired topping: ")
    print("Lettuce")
    print("Tomatoes")
    print("Onions")
    print("Pickles")
    print("Hot peppers")
    print("Spinach")
    print("Cucumbers")
    print()

def additionChoices():
    print("Enter your desired additions: ")
    print("Extra Cheese")
    print("Smoked Bacon")
    print("Extra Meat")
    print()

def beverageChoices():
    print("Enter your desired beverage: ")
    print("Tea")
    print("Water")
    print("Soda")
    print()


def main():

    order = Order()
    print("Welcome to the Sandwich Ordering System")

    #sandwich
    sandwichChoices()
    userSandwich = input()
    print()
    sandwich = Sandwich(userSandwich)

    #bread
    breadChoices()
    userBread = input()
    print()
    sandwich.set_bread(userBread)

    #Toast status
    userToasted = input("Is the bread toasted?, Enter y for yes or n for no: ")
    if userToasted == "y":
        sandwich.set_toasted(True)
    elif userToasted == "n":
        sandwich.set_toasted(False)

    #Cheese
    cheeseChoices()
    userCheese = input()
    print()
    sandwich.set_cheese(userCheese)

    #Spread
    spreadChoices()
    userSpread = input()
    print()
    sandwich.set_spread(userSpread)

    #Topping
    while True:
        toppingChoices()
        userTopping = input()
        sandwich.add_topping(userTopping)

        userToppingRepeat = input("Would you like to add another topping? Enter y for yes or n for no ")
        if userToppingRepeat == "n":
            break
        else:
            continue

    while True:
        additionChoices()
        userAddition = input()
        sandwich.add_addition(userAddition)

        if  userAddition == "Extra Cheese":
            sandwich.price += 0.70
        elif userAddition == "Smoked Bacon":
            sandwich.price += 1.40
        elif userAddition == "Extra Meat":
            sandwich.price += 2.39

        userAdditionRepeat = input("Would you like to add another addition? Enter y for yes or n for no ")
        if userAdditionRepeat == "n":
            break
        else:
            continue

    #Beverage
    beverageChoices()
    userBeverage = input()
    beverage = Beverage(userBeverage)

    if userBeverage == "Tea":
        beverage.price = 2.85
    elif userBeverage == "Water":
        beverage.price = 1.49
    elif userBeverage == "Soda":
        beverage.price = 2.39

    order.set_sandwich(sandwich)
    order.set_beverage(beverage)

    #print(sandwich.sandwich_status())#this statement outputs the order details of the sandwich
    #print(beverage.beverageStatement()) #this statement outputs the order details of the beverage

    print(order.orderStatements())








    #This print statement block is what the sandwich object has
    #print("Sandwich Type: ", sandwich.sandwich_type)
    #print("Sandwich Bread: " , sandwich.bread)
    #print("Sandwich Toast Status", sandwich.toasted)
    #print("Sandwich Cheese: ", sandwich.cheese)
    #print("Sandwich Spread: ", sandwich.spread)
    #print("Sandwich Topping: ", sandwich.toppings)
    #print("Sandwich Additions: ", sandwich.additions)
    #print("Sandwich Price: ", sandwich.getPrice())
    #print()
    #Beverage
    #print("Beverage Type: ", beverage.beverage_type)
    #print("Beverage Price:", beverage.getPrice())




if __name__ == "__main__":
    main()
