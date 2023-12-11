# Inheritance in programming enables a class to inherit attributes and methods from another class, 
# fostering code reusability. This establishes a relationship between a superclass (base class) and 
# a subclass (derived class).


# Exaple->
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using inherited method
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
