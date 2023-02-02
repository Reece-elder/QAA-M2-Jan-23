def countingApples(list):
    counter = 0

    for word in list:
        if word.lower() == "apple":
            counter += 1
            
    # Functions should NEVER print directly
    return counter

# Sanity test
print(countingApples(["apple", "kiwi", "lemon", "apple", "apple", "egg"]))

