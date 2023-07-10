# using the facade design pattern over coffee object
class AddFlavour:
    def __init__(self, coffee, flavour, cost):
        self.size = coffee.size
        self.coffee = coffee.coffee
        self.milk = coffee.milk
        self.flavour = flavour
        self.cost = coffee.cost + cost

    def __repr__(self):
        return f"Coffee details: size: {self.size}, coffee: {self.coffee}, milk: {self.milk}, flavour: {self.flavour}, cost: {self.cost}"
