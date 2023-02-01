# Parent class (Bird)

class bird: 

    def __init__(self, beak, featherColour, age):
        self.wingspan = 12
        self.beak = beak
        self.featherColour = featherColour
        self.age = age

    def sound(self):
        return "*Generic Squawk sound*"

# Specify Penguin is a child of Bird, by using (parent)
class penguin(bird):

    def __init__(self, beak, featherColour, age, waddleSpeed):
        # Run our parent __init__ to create a bird we can build on
        # in inheritance, super refers to the parent
        # Creating a bird object and passing values (bird1 = bird())
        super().__init__(beak, featherColour, age) 
        self.waddleSpeed = waddleSpeed

penguin1 = penguin("pointed", "black and white", 8, 900)
print(penguin1.sound())
print(penguin1.age)
print(penguin1.wingspan)

class eagle(bird):

    def __init__(self, beak, featherColour, age, flySpeed):
        # Run our parent __init__ to create a bird we can build on
        # in inheritance, super refers to the parent
        # Creating a bird object and passing values (bird1 = bird())
        super().__init__(beak, featherColour, age) 
        self.flySpeed = flySpeed

    # Override attributes and functionality (replacing the default use case)
    def sound(self):
        return "*Western Movie Eagle Sound*"

eagle1 = eagle("serrated", "brownish", 18, 89)
print(eagle1.sound())

# Parent object with 100 + child classes 

# Exercise 

