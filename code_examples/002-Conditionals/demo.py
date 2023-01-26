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
