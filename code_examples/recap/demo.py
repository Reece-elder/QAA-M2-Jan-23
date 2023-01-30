# How can I display "Hello World" in the terminal using Python 
print("Hello World")

# Type your answer in the chat box and only send when I say 

# How could I use for to count from 1 - 10 (only the top line)
for x in range(10):
    print(x + 1)

num = 10
colour = "red"

if num > 5 and colour.title() == "Red":
    print("A")
elif colour == "Blue":
    print("B")
else:
    print("C")


# I want to create a function that takes in 1 number and adds 5 and its called addFive
# What does the top line look like? 

def addFive(num):
    return num + 5

print(addFive(12))

# 17

number = int(input("Please enter your fav number: "))

if number > 10:
    print("Your fav is greater than 10")
else:
    print("Your number is 10 or less than 10")

def returnColour():
    return "Red"

def returnNumber():
    return 100

def returnBool():
    return True

def collabFunction():
    total_string = f"colour: {returnColour()}, number: {returnNumber()}, boolean: {returnBool()}"
    return total_string

print(collabFunction())
