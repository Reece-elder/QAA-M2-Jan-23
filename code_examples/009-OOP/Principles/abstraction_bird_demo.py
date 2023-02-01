# Abstraction - Making a class 'abstract' it cannot be directly created
# Abstract class is vaguer than a regular class, and used as a high level blueprint 

# In the chat box (BUT DON'T SEND YET)
# def sound(noise_level)
# make a name for a function and a paramater it will need to demonstrate sleeping 
# sleeping(yesOrNo)
# sleep(time)
# sleeping(dream)
# sleep_pattern()

# If we had a list of animals and looped through them to print the sleeping()

# abc - Abstract Base Class
from abc import ABC, abstractmethod 

class animal(ABC): 

    # All animals MUST override this function as at present it doesn't do anything
    @abstractmethod
    def sleep(hours):
        pass # Doesn't do anything 

# animal1 = animal() # You can't create an abstract object 

# My bird to be a child of Animal 
class bird(animal):

    def __init__(self, featherColour):
        self.featherColour = featherColour

    def sleep(hours):
        return f"Sleeping for {hours} hours"

bird1 = bird("blue")

# If you had to loop and run the connectDB() function on all 50 child classes 
for child in ["1", "2", "3"]:
    child.connectDB()
