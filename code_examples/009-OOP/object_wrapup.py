"""
    Using previous code (calculator, print menu and functions for sums +, -, *, /, raise power)
    Ensure it is functional code (using functions where appropriate)
    
    Convert it to atleast two objects that interact with eachother

    1) Calculator Object running sums 
    2) Printing object which prints what calculator returns 
"""

class calculator:

    def __init__(self, brand):
        self.brand = brand

    def add_sum(self, x, y):
        return x + y

    def sub_sum(self, x, y):
        return x - y

    def mul_sum(self, x, y):
        return x * y

    def div_sum(self, x, y):
        return x / y

    def power_sum(self, x, y):
        return x**y

class calc_controller:

    # What calculator object do I want to belong to this
    def __init__(self, calculator):
        self.calc = calculator

    def getBrand(self):
        return self.calc.brand

    def getChoice(self):
        choice = int(input("Please select choice between 1 - 5: "))

        num1 = int(input("Please choose num1 :"))
        num2 = int(input("Please choose num2 :"))
        if choice == 1:
            print(self.calc.add_sum(num1, num2))
        elif choice == 2:
            print(self.calc.sub_sum(num1, num2))
        elif choice == 3:
            print(self.calc.mul_sum(num1, num2))
        elif choice == 4:
            print(self.calc.div_sum(num1, num2))
        elif choice == 5:
            print(self.calc.power_sum(num1, num2))
        else:
            print("Incorrect choice")

calc1 = calculator("Casio")
cont1 = calc_controller(calc1)

cont1.getChoice()
print(cont1.getBrand())
