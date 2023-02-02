""" Dice ROller file """

from random import randint
DICE_ROLLER = 6
def rolllotsofdice():
    """ Function name.. """
    return randint(1,6)

print(rolllotsofdice())
def rolllotsofdice2():
    """ Function name.. """
    return randint(1,10,)

def rollcustonnumbersss(numberone, numbertwo,):
    """ Function name.. """
    return randint(numberone, numbertwo)

def checkrolls():
    """ Function name.. """
    if rolllotsofdice2() >= 6:
        return "big number!!!"
    return "small number :( "
CHECK_ROLLS = checkrolls()
print(CHECK_ROLLS)
LONG_VAR = "this is a really long variable that is integral to the flow of the code so I can ad"
