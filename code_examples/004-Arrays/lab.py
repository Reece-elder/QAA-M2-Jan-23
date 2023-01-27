ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
print(ages)

length = len(ages)
print(length)

# for age in ages:
#     print(age)

# Making a new list and appending the new data to it
# Modify the data in the list directly

print("***********************************")
index = 0
for age in ages:
    # print(age + 1)
    ages[index] += 1
    index += 1

# print(ages)

new_list = []

for age in ages:
    if age < 65 and age > 16:
        print(age)
        new_list.append(age)

print(new_list)
print(ages)