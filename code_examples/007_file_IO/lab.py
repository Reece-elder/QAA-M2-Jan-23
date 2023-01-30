# Ignore the first line 
car_file = open("cars.csv")
months = car_file.readline() # Moving the cursor past the months
car_data = car_file.readlines() # Getting all data

# turning ford string into an array
ford = car_data[0].split(",")
volks = car_data[1].split(",") 
merc = car_data[2].split(",") 

# Blank array for ford values
# Counter to loop array and ignore the first value
# counter = 0
# for data in ford:
#     if counter != 0:
#         # Removing " from data and \n
#         new_data = data.replace('"','').strip()
#         ford_nums.append(int(new_data)) # Adding clean data to array
#     counter += 1

# print(ford_nums)

def cleanArray(array):
    new_array = []
    counter = 0
    for data in array:
        if counter != 0:
            # Removing " from data and \n
            new_data = data.replace('"','').strip()
            new_array.append(int(new_data)) # Adding clean data to array
        counter += 1
    return new_array

def sumOfCars(car_type):
    return sum(car_type)

ford_nums = cleanArray(ford)
volks_nums = cleanArray(volks)

print(sumOfCars(ford_nums))



