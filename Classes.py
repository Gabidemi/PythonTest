class Person:
    species = "Homosapien" #This is an attribute

    def hello(self):
        print("Hello World")

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hi(self):
        print("Hi my name is " + self.name)
#"Self" is used to access variables that belongs to the class
    
Ayo = Person("Ayo", 16) #made a variablee for the class "person"
print(Ayo.species) #calls the species class you created
print(Ayo.name) #calls the age object you created
print(Ayo.age) #calls the name object you created
Ayo.hello()

Alyssa = Person("Alyssa", 18)
print(Alyssa.name)
print(Alyssa.age)
Ayo.hi()
Alyssa.hi()

