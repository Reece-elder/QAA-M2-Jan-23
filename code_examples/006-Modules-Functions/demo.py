# Functions are ways we can 'repeat' blocks of code under specific conditions
# Functions should be used to handle the logic of your application 

# Global / non functional - code

# print(
#     """
#         Welcome to QA Calculator! 
#         Please select a choice from below: 

#         1. Add
#         2. Subtract
#         3. Multiply
#         4. Divide
#         5. Power
#     """
# )

# choice = int(input("Please select a number between 1 and 5: "))
# num1 = int(input("Please select number 1: "))
# num2 = int(input("Please select number 2: "))

# if choice == 1:
#     print(num1 + num2)
# elif choice == 2:
#     print(num1 - num2)

# Functional code is when code is split into repeatable and callable modules

# def - define, defining the function we wish to use
# All functions can take in paramaters (when they are created)
# These are variable placeholders that are set when function is called
def addSum(x, y):
    total = x + y
    print(f"{x} + {y} = {total}")

# Calling the function
addSum(10, 15) # x = 10, y = 15

addSum("Hello", "World") # HelloWorld
# addSum("Hello", 5000)

# Typically all functions should 'return' something 
# All functions should output something from the codeblock for external use

def subSum(x, y):
    total = x - y
    return total # return is the keyword, what is this function returning 

result = subSum(45, 10) # if AddSum() output or returned something result would be equal to it
print(result)

# If your function doesn't need to return anything useful.. make it return True

# CallBack functions, we pass in a function as a paramater to a different function 

def berryFunc(adjective):
    print("Berry func runs")
    berry = f"{adjective}berry"
    return berry

def berryCallback(function):
    print("Berry call back runs")
    return f"Delicious {function}"

# print(berryFunc("blue"))
print(berryCallback(berryFunc("red")))