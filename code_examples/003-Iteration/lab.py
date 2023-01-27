# Investment Question 
# Starting from £100, aiming to reach £1000 and interst rises by 10% each year
# How many years will it take?
# Simple - Increasing by the same amount each year (starting amount) 

starting = 100
goal = 1000
interest = 0.10
current = starting
years = 0

# Simple interest
# while current < goal:
#     current = current + (starting * interest)
#     years = years + 1
# Compound Interest
while current < goal:
    current = current + (current * interest)
    years += 1 # increments the variable by 1 


print(f"It took {years} years to increase {starting} to {goal} through interest of {interest * 100}%")


# Guessing the number task 
correct = False
guesses = 0
allowed_guesses = 4
min = 10
max = 40
exact_num = 23

# Loop 3 times (or however many guesses I allow)
for x in range(allowed_guesses):

    guess_num = int(input(f"Please enter a guess number between {min} and {max}: "))
    if guess_num == exact_num:
        print("Correct!")
    else:
        guesses += 1 # increase guesses by 1
        # hot is within 4 nums, cold is within 15 nums
        diff = guess_num - exact_num
        print(abs(diff)) 


# Factorial - Factorial 3 = 1 * 2 * 3 = 6

total = 1
factorial = 3

for num in range(1, factorial + 1):
    total = total * num

print(total)
