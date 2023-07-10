from addFlavour import AddFlavour
from coffee import Coffee
from coffeeMenu import Menu
from inventory import Inventory


class CoffeeMachine:
    def __init__(self):
        self.menu = Menu()
        self.inventory = Inventory()
        self.coffee = ["espresso", "cappuccino", "latte", "mocha"]
        self.milk = ["whole", "skim", "soy"]
        self.size = ["small", "medium", "large"]
        self.flavouring = ["vanilla", "caramel", "hazelnut"]

    def getMenu(self):
        return self.menu

    def validCoffee(self, coffee):
        for c in self.coffee:
            if c == coffee:
                return True
        return False

    def validMilk(self, milk):
        for c in self.milk:
            if c == milk:
                return True
        return False

    def validSize(self, size):
        for c in self.size:
            if c == size:
                return True
        return False

    def validFlavouring(self, flavouring):
        for c in self.flavouring:
            if c == flavouring:
                return True
        return False

    def makeCoffee(self, coffee, milk, size):
        # todo add check for valid coffee milk and size
        if not self.validCoffee(coffee) or not self.validMilk(milk) or not self.validSize(size):
            print("some invalid value selected")
            return

        print(f'Checking inventory for coffee: {coffee}, milk: {milk}, size: {size}')

        # check if items are available
        coffeeAvailable = self.inventory.checkCoffee(coffee, size)
        print(f"availability of coffee: {coffeeAvailable}")
        milkAvailable = self.inventory.checkMilk(milk, size)
        print(f"availability of milk: {milkAvailable}")

        if not coffeeAvailable or not milkAvailable:
            print("insufficient items")
            return

        # the following has to be a transaction
        # get items from inventory
        self.inventory.getCoffee(coffee, size)
        self.inventory.getMilk(milk, size)

        # get the cost of items
        cost = self.menu.getCoffeePrice(coffee, size)
        cost += self.menu.getMilkPrice(milk, size)

        # make coffee
        return Coffee(size, coffee, milk, cost)

    def addFlavouring(self, coffee, flavour):
        # validate flavour
        if not self.validFlavouring(flavour):
            print("invalid flavour selected")
            return

        # check inventory
        flavourAvailable = self.inventory.checkFlavour(flavour, coffee.size)
        if not flavourAvailable:
            print(f"flavour: {flavour} not available")
            return

        # the following has to be a transaction
        # get flavour from inventory
        self.inventory.getFlavour(flavour, coffee.size)

        # get the cost
        cost = self.menu.getFlavourPrice(flavour, coffee.size)

        # add flavour
        return AddFlavour(coffee, flavour, cost)