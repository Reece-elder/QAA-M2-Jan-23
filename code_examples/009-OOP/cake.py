
# A class is a type of code that allows you to create 'objects'
# It doesn't have to be the same name of a file, and creates objects of type <cake>
class cake:

    # __init__() is a special function that is called initially when the class runs
    # __init__ acts as a constructor, to create cake objects
    def __init__(self, layers, flavour, vegan, ingredients):
        # layers, flavour.. are all attributes of this object
        # self must be added and allows the function to refer to the object
        self.layers = layers
        # the object has an attribute called objLayers 
        # this is set to whatever the value of 'layers' is
        #spongeCake objLayers attribute is equal to 2 
        self.flavour = flavour
        self.vegan = vegan
        self.ingredients = ingredients

# Outside of the class cake we can make a cake object
# Variable cake1 is equal to whatever our cake class returns
cake1 = cake(2, "vanilla", False, ["flour", "eggs", "milk"])

# Guess 1 - Display the attributes as an list
# Guess 2 - Display attributes as a dictionary (objFlavour: vanilla)

print(cake1)
# When printing an object (default) it tells us where the memory is stored
# <__main__.cake object at 0x0000022048A4EE10>

print(cake1.flavour)
print(cake1.__dir__()) # All attributes / functions of objects 

# Exercise - Create a class for an 'object' of your choice
# Class must contain atleast 4 variables using string, boolean, numbers (ints / floats) and an array
# Create 2x objects of your class and print the attributes you have set