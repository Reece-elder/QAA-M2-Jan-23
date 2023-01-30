# Python is really good as a tool to help devs do everyday jobs, 
# Useful tool for people who aren't specifically technical, data scientists, accountants, engineers 
# Python is a really good tool at reading and manipulating any form of 'data'

# Using python we can access and print the contents of our .txt file
# important you are running the file from a directory that can see the .txt
fruit_file = open("fruit.txt")

print(fruit_file) # Not useful data

data = fruit_file.readlines() # get data from file

# print(data[0])
# print(data[1])
# print(data[2])
print(data)

for fruit in data:
    print(fruit)

fruit_file.close() # close the file so we can't make changes / something else can change it

# Exercise - Create a txt file containing favourite animals, use python to loop through and print each