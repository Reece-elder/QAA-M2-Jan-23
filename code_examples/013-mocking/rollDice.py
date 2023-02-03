from random import randint

def printDiceFunc(num):
    total = rollDiceFunc(num)
    return f"Rolled dice of size {num}: {total}"

def rollDiceFunc(num):
    return randint(1, num+1)
