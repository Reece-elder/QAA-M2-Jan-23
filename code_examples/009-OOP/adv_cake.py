class cake:

    def __init__(self, layers, flavour, vegan, ingredients):
        self.layers = layers
        self.flavour = flavour
        self.vegan = vegan
        self.ingredients = ingredients

    # Objects can also contain functions
    # python class functions MUST include the word self
    # self is referring to this specific object
    def bake(self):
        return f"Almost finished cooking your {self.flavour} cake"

    # When printing any complex object (arrays, strings, cake) we run the __str__()
    def __str__(self):
        return f"flavour: {self.flavour}  layers: {self.layers}  ingredients: {self.ingredients}"


cake1 = cake(2, "vanilla", False, ["flour", "eggs", "milk"])
cake2 = cake(4, "choc", True, ["cocoa", "oil", "gluten free flour"])
cake3 = cake(1, "plain", False, ["flour", "eggs"])

# we don't pass in a 'self' but self refers to the object we are running
print(cake1.bake()) 
# print(cake.bake()) - there is no 'self' for cake as it is a class, a static method

print(cake1.flavour)
print(cake1.ingredients)
print(cake1.layers)

print(cake2.__str__())
print(cake2)

# Exercise - In your class override the __str__ method to return key: value pairs for attributes
# Add a custom function that returns some text and includes an attribute