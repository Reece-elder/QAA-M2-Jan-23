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