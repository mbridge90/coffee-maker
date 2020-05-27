class Coffee_maker:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def get_status(self):
        print(f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money""")

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def buy_coffee(self):
        coffees = {
            "1": {"water": 250, "milk": 0, "coffee": 16, "money": 4},
            "2": {"water": 350, "milk": 75, "coffee": 20, "money": 7},
            "3": {"water": 200, "milk": 100, "coffee": 12, "money": 6}
        }
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - return to previous menu: ")
        if choice == "back":
            return

        elif choice in ["1", "2", "3"]:
            enough_resources = all([self.water >= coffees[choice]["water"], self.milk >= coffees[choice]["milk"], self.coffee >= coffees[choice]["coffee"], self.cups >= 1])
            if enough_resources:
                print("I have enough resources, making you a coffee!")
                self.water -= coffees[choice]["water"]
                self.milk -= coffees[choice]["milk"]
                self.coffee -= coffees[choice]["coffee"]
                self.money += coffees[choice]["money"]
                self.cups -= 1
            elif self.water < coffees[choice]["water"]:
                print("Sorry, not enough water!")
            elif self.milk < coffees[choice]["milk"]:
                print("Sorry, not enough milk!")
            elif self.coffee < coffees[choice]["coffee"]:
                print("sorry, not enough coffee!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")

        else:
            print("Invalid option, please try again.")
            self.buy_coffee()

    def fill_machine(self):
        self.water += int(input("Write how many ml water do you want to add: "))
        self.milk += int(input("Write how many ml milk do you want to add: "))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups do you want to add: "))

    def use_machine(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit) : ")
            if action == "buy":
                self.buy_coffee()
            elif action == "take":
                self.take_money()
            elif action == "fill":
                self.fill_machine()
            elif action == "exit":
                break
            elif action == "remaining":
                self.get_status()
            else:
                print("Invalid option")


my_coffee_maker = Coffee_maker(400, 540, 120, 9, 550)

my_coffee_maker.use_machine()