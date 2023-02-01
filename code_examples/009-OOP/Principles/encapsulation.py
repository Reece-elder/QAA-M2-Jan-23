# Encapsulation: 
# - Combining all necessary functionality into one module / class where possible 
# - Best practice and security only trusted objects have access to its data

# Within python there isn't a concept of 'private' variables
# Variables that you cannot access from other places

# Private python variables start with an _ and are there so developers know they should be private

class unSafeBankAccount:

    # private email_address
    # print(self.email_address)

    def __init__(self, pin):
        self.pin = pin
        self.money = 500

class SafeIshBankAccount:

    # private String pin = ""

    # Common practice for 'confidential' variables to have a leading _
    def __init__(self, pin, age):
        self._pin = pin
        self._age = age
        self._money = 500

    # Getters and Setters
    # Getters - Get variable or function data
    # Setters - Set variables or function data 

    def checkBalance(self, pin): 
        # If the pin the user entered is same as the acc pin
        if pin == self._pin:
            return self._money
        else: 
            return "Invalid pin!"

    def changeAge(self, age):
        if age < self._age:
            return "Invalid, you can't be younger than you are.."
        else:
            self._age = age

# acc1 = unSafeBankAccount("5555")
acc2 = SafeIshBankAccount("1234", 20)

print(acc2._money)
print(acc2.checkBalance("1234"))
# print(acc2.changeAge(15))

# bank_pin = acc1.pin

# print(acc1.pin)

# Exercise - In a new class or your existing class implement 2x getters that check for validation (i.e password)
# And 2x setters that don't let you add silly data (wingspan, wingspan cannot be less than 0 )