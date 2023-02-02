# Polymorphism - Objects can take on many different changing forms
# Poly meaning Many / multiple
# Morph meaning changing 

class fish:
    def noise(self):
        return "Glub Glub"

class lion:
    def noise(self):
        return "ROAR"

fish1 = fish()
lion1 = lion()

# print(fish1.noise())
# print(lion1.noise())

# List that contains both types of objects
animalList = [fish1, lion1]

# Polymorphism is more of a side effect of object based language, good code is polymorphic.. 

for animal in animalList:
    print(animal) # Animal is both a fish and a lion at the same time, and can run both commands 
    print(animal.noise()) 

# inheriting attributes and functions from super() / object 
class studentAccount:
    def __init__(self, name):
        self.name = name

    def logout(self):
        return "Student logout"

class teacherAccount:
    def __init__(self, name):
        self.name = name

    def logout(self):
        return "Teacher logout"

peopleList = [studentAccount("Cedrick"), teacherAccount("Mary")]
print(peopleList)

for people in peopleList:
    print(people.name) # people object is both student and teacher, object()
    print(people.logout())