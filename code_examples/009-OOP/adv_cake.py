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

    def changeFlavour(self, newFlav):
        self.flavour = newFlav
        return True


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

cake1.changeFlavour("coffee") # using function to change to coffee
cake1.flavour = "raspberry"   # directly changing value
print(cake1)

# getattr - returns the value of named attribute of object
# setattr - changes the value of named attribute
# delattr - deletes this attribute
# hasattr - checks if attribute is there and returns true or false 
print("*****************************************")
setattr(cake1, "flavour", "almond") # updates AND creates new attributes
print(cake1.flavour) 
delattr(cake1, "candles")
print(hasattr(cake1, "candles")) # returns false
if hasattr(cake1, "candles"):
    print(getattr(cake1, "candles")) # cake has no attr called candles
else: 
    print("Cake 1 has no candles :(")


