# Ignore the first line 
car_file = open("cars.csv")
months = car_file.readline() # Moving the cursor past the months
car_data = car_file.readlines() # Getting all data

# print(car_data)
# print(car_data[0]) 
# turning ford string into an array
ford = car_data[0].split(",") 
# print(ford)
# Blank array for ford values
ford_nums = []
# Counter to loop array and ignore the first value
counter = 0
for data in ford:
    if counter != 0:
        # Removing " from data
        new_data = data.replace('"','')
        ford_nums.append(new_data) # Adding clean data to array
    counter += 1

print(ford_nums)