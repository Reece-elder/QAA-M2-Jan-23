# Selection / Conditionals
# Selection lets us specify what our code should do under certain conditions

# All logic is binary, it either does something or doesn't

check = True # True is a boolean, the opposite is false

# When using == we are checking for values
# When using = we are  this 
if check == True:
    print("check is true")
else:
    print("Check is not true)")

points = int(input("Enter a points number: "))
# points = "five"

if points < 5:
    print("Points less than 5")
elif points > 5:
    print("Points is greater than 5")
else:
    print("Points equal to 5")

# What do we know if points is not less than 5

print("===========================================")
colour = "Red"
# use string.lower() or .upper() tio convert to different cases for validation
if colour.lower() == "red":
    print("colour is red")
else:
    print("Colour is not red")

cakeSize = 20
frosting = False

# Complex conditional statement with multiple conditions 
# OR  - if condition 1 is true or condition 2 is true or both are true
# AND - if cond 1 is true AND cond 2 is true

if frosting == False and cakeSize > 21:
    print("Frosting is false AND cake is bigger than 21")
elif frosting == True:
    print("Frosting is true")
elif cakeSize > 21:
    print("Cake is bigger than 21")
else:
    print("Cake is smaller than 21 and frosting is false")

if frosting == False or cakeSize > 21:
    print("either frosting is false, or cakesize is bigger than 21, or they are both true")

    # When checking a boolean for True or False we can just put in the boolean we're checking
    # Only works this way for True booleans
    if frosting or colour == "red":
        print("Cake size is bigger than 21 ")

    if not frosting:
        print("Cake is not frosted")
