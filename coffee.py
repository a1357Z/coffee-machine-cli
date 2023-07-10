class Coffee:
    def __init__(self, size, coffee, milk, cost):
        self.size = size
        self.coffee = coffee
        self.milk = milk
        self.cost = cost

    def __repr__(self):
        return f"Coffee details: size: {self.size}, coffee: {self.coffee}, milk: {self.milk}, cost: {self.cost}"