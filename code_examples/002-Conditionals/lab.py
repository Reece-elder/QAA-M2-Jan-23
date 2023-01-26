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