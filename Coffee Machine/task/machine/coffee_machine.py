'''class Richards_coffee_maker_component:

    def __init__(self, quantity, name, minimum):
        self.quantity = quantity
        self.name = name
        self.minimum = minimum

'''

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

    def make_espresso(self):
        enough_resources = all([self.water >= 250, self.coffee >= 16, self.cups >= 1])
        if enough_resources:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.coffee -= 16
            self.money += 4
            self.cups -= 1
        elif self.water < 250:
            print("Sorry, not enough water!")
        elif self.coffee < 16:
            print("sorry, not enough coffee!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")


    def make_latte(self):
        enough_resources = all([self.water >= 350, self.milk >= 75, self.coffee >= 20, self.cups >= 1])
        if enough_resources:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.money += 7
            self.cups -= 1
        elif self.water < 350:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.coffee < 20:
            print("sorry, not enough coffee!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")

    def make_cappuccino(self):
        enough_resources = all([self.water >= 200, self.milk >= 100, self.coffee >= 12, self.cups >= 1])
        if enough_resources:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.money += 6
            self.cups -= 1
        elif self.water < 200:
            print("Sorry, not enough water!")
        elif self.milk < 100:
            print("Sorry, not enough milk!")
        elif self.coffee < 12:
            print("sorry, not enough coffee!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def buy_coffee(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        if choice == "1":
            self.make_espresso()
        elif choice == "2":
            self.make_latte()
        elif choice == "3":
            self.make_cappuccino()
        elif choice == "back":
            return
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




'''water = 400
milk = 540
coffee = 120
cups = 9
money = 550'''

'''def get_status():
    print(f"""The coffee machine has:
    {water} of water
    {milk} of milk
    {coffee} of coffee beans
    {cups} of disposable cups
    {money} of money""")'''

'''def make_espresso():
    global water, coffee, money, cups
    water -= 250
    coffee -= 16
    money += 4
    cups -= 1'''

'''def make_latte():
    global water, milk, coffee, money, cups
    water -= 350
    milk -= 75
    coffee -= 20
    money += 7
    cups -= 1'''

'''def make_cappuccino():
    global water, milk, coffee, money, cups
    water -= 200
    milk -= 100
    coffee -= 12
    money += 6
    cups -= 1'''

'''def take_money():
    global money
    money = 0

def fill():
    global water, milk, coffee, cups
    water += input()
    milk += input()
    coffee += input()
    cups += input()

def buy_coffee():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    if choice == "1":
        make_espresso()
    elif choice == "2":
        make_latte()
    elif choice == "3":
        make_cappuccino()

def fill_machine():
    global water, milk, coffee, cups
    water += int(input("Write how many ml water do you want to add: "))
    milk += int(input("Write how many ml milk do you want to add: "))
    coffee += int(input("Write how many grams of coffee beans do you want to add: "))
    cups += int(input("Write how many disposable cups do you want to add: "))

def choose_action():
    action = input("Write action (buy, fill, take) : ")
    if action == "buy":
        buy_coffee()
    elif action == "take":
        take_money()
    elif action == "fill":
        fill_machine()
    else:
        print("Invalid option")
        choose_action()

def use_machine():
    get_status()
    choose_action()
    get_status()'''


'''use_machine()'''






'''water_available = int(input("Write how many ml of water the coffee machine has: ")) // 200
milk_available = int(input("Write how many ml of milk the coffee machine has: ")) // 50
coffee_available = int(input("Write how many grams of coffee beans the coffee machine has: ")) // 15
possible_cups = min([water_available, milk_available, coffee_available])
n = int(input("Write how many cups of coffee you will need: "))
if n == possible_cups:
    print("Yes, I can make that amount of coffee")
elif n < possible_cups:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(str(possible_cups - n)))
elif n > possible_cups:
    print("No, I can only make {} cups of coffee".format(str(possible_cups)))'''

'''water_needed = 200 * int(n)
milk_needed = 50 * int(n)
coffee_beans_needed = 15 * int(n)'''

'''available_cups_water = water_available // 200
available_cups_milk = milk_available // 50
available_cups_coffee = coffee_available // 15'''





'''print("""For {n} cups of coffee you will need:
{water} ml of water
{milk} ml of milk
{coffee_beans} g of coffee beans""".format(n=n, water=str(water_needed), milk=str(milk_needed), coffee_beans=str(coffee_beans_needed))'''


""""print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")"""