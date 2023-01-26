# Telling Python to import (bring in) the additional inbuilt math package
import math

# Calculator

# DocString - Multiline String that can act as a comment, useful for lots of information to present
print(
    """
        Welcome to QA Calculator! 
        Please select a choice from below: 

        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Power
    """
)

choice = int(input("Please select a number between 1 and 5: "))
num1 = int(input("Please select number 1: "))
num2 = int(input("Please select number 2: "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)

grade = 70

# if grade < 0 and < 100:
#     print("Do something")

# pythagoras
# Length of the long side of a right angled triangle is equal to a^2 + b^2 = c^2 
# a = 2, b = 3
# a = 4 + b = 9 = 13
# C is Square root of 13  3.6

pyth_choice = input("What side of the triangle do you not know? (A, B or C): ").upper()

side_1 = float(input("Please enter side of 1: "))
side_2 = float(input("Please enter side of 2: "))

if pyth_choice == "A" or pyth_choice == "B":
    # A^2 + B^2 = C^2
    # A^2 = C^2 - B&2
    side_3 = ((side_1**2) - (side_2**2))**0.5
    print(side_3)
elif pyth_choice == "C":
    side_3 = ((side_1**2) + (side_2**2))**0.5
    print(side_3)

# print(a_side + b_side)

# c_side = (a_side**2) + (b_side**2) 
# c_side_1 = c_side**0.5
# c_side_2 = math.sqrt(c_side)
# print(f"1: {c_side_1}   2: {c_side_2}")



