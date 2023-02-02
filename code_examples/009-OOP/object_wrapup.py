"""
    Using previous code (calculator, print menu and functions for sums +, -, *, /, raise power)
    Ensure it is functional code (using functions where appropriate)
    
    Convert it to atleast two objects that interact with eachother

    1) Calculator Object running sums 
    2) Printing object which prints what calculator returns 
"""

def add_sum(x, y):
    return x + y

def sub_sum(x, y):
    return x - y

def mul_sum(x, y):
    return x * y

def div_sum(x, y):
    return x / y

def power_sum(x, y):
    return x**y

def getChoice():
    choice = int(input("Please select choice between 1 - 5: "))

    num1 = int(input("Please choose num1 :"))
    num2 = int(input("Please choose num2 :"))
    if choice == 1:
        print(add_sum(num1, num2))
    elif choice == 2:
        print(sub_sum(num1, num2))
    elif choice == 3:
        print(mul_sum(num1, num2))
    elif choice == 4:
        print(div_sum(num1, num2))
    elif choice == 5:
        print(power_sum(num1, num2))
    else:
        print("Incorrect choice")
