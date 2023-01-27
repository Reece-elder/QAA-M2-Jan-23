import random

# Python Functions
# Inbuilt functions which are always accessible
# Package functions we can import from Python / pip
# Custom functions that we define ourselves

# Functions are ways of repeating a block of code when it is called
# Loops run continuously and you can't assign a whole 'loop' 

# Function can be defined with a name, and called by calling that name at any point in time

print("Sends this data to the terminal")
# Functions must be called, by defining the name then with ()

# A lot of python built in functions are focused around data types
# String functions, number functions 

numbers = [19,63,51,7,99,11,23,15,17,8]

# print(min(numbers)) # minimum number from an array
# print(max(numbers)) # max from an array

# print((pow(2,4)))
# num1 = int(input("Please choose num 1: "))
# num2 = random.randint(1, 6)

# print(pow(num1, num2))

float = 5.624864635161
print(round(float, 2))

# Formatting strings
str = "hElLo \nWoRlD!!!!"
print(str)

# Typically numbers don't have functions, but are used in functions 
# Numbers are 'simple' data types, booleans, chars (a, e, 1, +)
# String is a complex data type, it is an array of 'chars'
print(str.lower())
print(str.upper())
print(str.replace("!", ".."))
print(str.replace("!", ""))
print(len(str))
new_str = str.replace("\n", "")

print(new_str.center(40, "*"))

# Split function .csv file 
cities = "london,birmingham,leeds,manchester,bristol"
print(cities[24:34])
city_list = cities.split(",")
print(city_list)
print(city_list)

