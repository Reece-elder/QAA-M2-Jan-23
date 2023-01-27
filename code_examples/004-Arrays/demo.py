# Arrays - Arrays are collections of multiple types of data (called elements)
# Lists []  - Ordered (index numbers), collections of values, mutable (you can modify them and change values)
# Tuples () - Ordered, immutable (they are set value and can't change), collections of values  
# Sets {}   - Collection of unique values, unordered, mutable (country codes, unique pins)
# Dictionaries {} Key: Value pairs, unordered (by index) but organised by the key, mutable

# Lists 
shapes = ["Square", "triangle", "circle", "pentagon"]

print(shapes)
print(shapes[1]) # Triangle (index 1) 
# All ordered arrays are indexed, meaning you count from 0 to select the element you want 
print(shapes[3])

# Slicing an array
print(shapes[0:2]) # inclusive of lower end, exclusive of upper end

shapes[2] = "semi circle"
print(shapes)

# Append and Remove - Adding elements or removing named elements
shapes.append("star")
shapes.remove("triangle")
print(shapes)

cafe_order = [12, ["latte", "carrot cake"], True, "Mr Anderson"]
print(cafe_order)
# Print off the word "carrot cake"
print(cafe_order[1][1]) # Multi dimensional array

print(len(shapes)) # prints off the 'length' of an array which is how many elements it is 

# Tuples - cannot be modified once declared
colour_tuples = ("red", "green", 123)
print(colour_tuples)
# colour_tuples[1] = "ocean foam"
print(colour_tuples[1])
# colour_tuples.append("blue") 

# Dictionaries - key value pairs
noises = {"cow": "moo!", "duck": "quack!"}
# print(noises)
noises["duck"] = "quacks don't echo"
print(noises["duck"])
noises["chicken"] = "cluck!"
print(noises)

# Sets - unordered, mutable, unique values
number_set = {1, 2,"lime", 2, 5, 7, 12, 142, "apple", "banana", "apple", 5, 6, 90, 142, 90, "lime", 1, 2, 3}
print(number_set)