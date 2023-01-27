import random

def rollSix():
    return random.randint(1, 6)

result = rollSix()
print(result)


# Roll 4 six sided dice
def rollDice(size):
    return random.randint(1, size)

# print(rollDice(8))

def rollMultipleDice():
    for x in range(4):
        dice_roll = rollDice(8)
        print(dice_roll)

rollMultipleDice()


# six_side_dice = []
# def four_dices_of_six():
#     for i in range(6):
#         small_roll = []
#         for j in range(4):
#             num = random.randint(1, 6)
#             small_roll.append(num)
#         six_side_dice.append(small_roll)
#     return six_side_dice
# print(f"4 Dices of 6: ",four_dices_of_six())