# Iteration - Repeating a block of code for situations you need something to run more than once
# Exercise: print the word "Hello" 100 times 
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")

# While Loops - Run until something is no longer true
# You're not sure how many times it should loop

# For Loops   - Runs a set amount of times
# Used when you are sure how many times 

# Random is a python file that has functions we can use to make random numbers
import random

print(random.randint(1,10)) # generates a random int between 1 and 10

# Make a loop that keeps running until a number is hit

count = 0
dice_roll = random.randint(1, 20)
while dice_roll != 20:
    print("Unlucky roll! Try again!")
    dice_roll = random.randint(1, 20) # rolling the dice again
    print(f"Value of dice: {dice_roll}")
    count = count + 1 # Increase the value of count by 1 

    if dice_roll == 1:
        print("Critical miss! You lose :( ")
        break # If the code hits 'break' the loop stops 

print(f"Number of rolls: {count}")

