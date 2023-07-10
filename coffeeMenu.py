class Menu:
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

    def getCoffeePrice(self, coffee, size):
        return self.coffee[coffee][size]

    def getMilkPrice(self, milk, size):
        return self.milk[milk][size]

    def getFlavourPrice(self, flavour, size):
        return self.flavourings[flavour][size]