from coffeeMachine import CoffeeMachine

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hi, welcome to the coffee machine")
    coffeeMachine = CoffeeMachine()
    # menu = coffeeMachine.getMenu()

    # take user input
    coffee = input("enter the coffee type u want: espresso, cappuccino, latte, or mocha ?")
    milk = input("enter the milk type u want: whole, skim, or soy ?")
    size = input("enter the size: small, medium or large ?")

    coffee = coffeeMachine.makeCoffee(coffee, milk, size)
    print(coffee)

    flavour = input("what flavour u want to add: vanilla, caramel, hazelnut ?")
    coffee = coffeeMachine.addFlavouring(coffee, flavour)

    print(coffee)


