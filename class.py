class MyClass:
    attribute = "This is a class attribute"

    def method(self):
        return "This is a class method"

'''
A class is a blueprint for creating objects. It defines a structure
that encapsulates attributes and functions. 
Above class with one attribute and one method.
'''    

'''
A constructor is a special method used to set up an object when it is
created. 
The constructor is named __init__(), and it is used to give the object its
initial values or properties0 
'''

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# When a new object Dog is created, the __init__() method automatically
# runs and sets the name and breed for that specific dog.

dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.breed)   
dog1.bark()        

#In this case, __init__() is the constructor that initializes dog1 with a
#name and breed right when the object is created. 

'''
Instance variable are variables that are unique to each object created
from a class. They store data that is specific to an instance of the
class. 
for example: 
self.name = name ; instance variable for dog's name.
self.breed = breed ; instance variable for dog's breed.
'''

'''
Unlike instance variable that are unique to each object, class variables are shared by all 
instances(objects) of a class and are defined outside any methods. 
'''
class Dog:
    species = 'Golden Retriever'
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
dog1 = Dog("Buddy", "pug")
print(dog1.species)        

