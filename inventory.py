class Inventory:
    def __init__(self):
        self.coffee = {"latte": {
            "small": 10,
            "medium": 15,
            "large": 20
        }, "espresso": {
            "small": 10,
            "medium": 15,
            "large": 20
        }, "cappuccino": {
            "small": 10,
            "medium": 15,
            "large": 20
        }, "mocha": {
            "small": 10,
            "medium": 15,
            "large": 20
        }}

        self.milk = {"whole": {
            "small": 10,
            "medium": 15,
            "large": 20
        }, "skim": {
            "small": 10,
            "medium": 15,
            "large": 20
        }, "soy": {
            "small": 10,
            "medium": 15,
            "large": 20
        }}

        self.flavourings = {"vanilla": {
            "small": 10,
            "medium": 15,
            "large": 20
        }, "caramel": {
            "small": 10,
            "medium": 15,
            "large": 20
        }, "hazelnut": {
            "small": 10,
            "medium": 15,
            "large": 20
        }}

    def checkCoffee(self, coffee, size):
        if coffee not in self.coffee:
            return False
        return self.coffee[coffee][size] > 0

    def checkMilk(self, milk, size):
        if milk not in self.milk:
            return False
        return self.milk[milk][size] > 0

    def checkFlavour(self, flavour, size):
        if flavour not in self.flavourings:
            return False
        return self.flavourings[flavour][size] > 0

    def getCoffee(self, coffee, size):
        self.coffee[coffee][size] = int(self.coffee[coffee][size]) - 1

    def getMilk(self, milk, size):
        self.milk[milk][size] = int(self.milk[milk][size]) - 1

    def getFlavour(self, flavour, size):
        self.flavourings[flavour][size] = int(self.flavourings[flavour][size]) - 1