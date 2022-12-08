class Person:
    species = "Homosapien" #This is an attribute

    def hello(self):
        print("Hello World")

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hi(self):
        print("Hi my name is " + self.name)


class Student(Person):
    role = 'student'

#"Self" is used to access variables that belongs to the class
    
Ayo = Student("Ayo", 16) #made a variablee for the class "person"
print(Ayo.species) #calls the species class you created
print(Ayo.name) #calls the age object you created
print(Ayo.age) #calls the name object you created
Ayo.hello()

Alyssa = Student("Alyssa", 18)
print(Alyssa.name)
print(Alyssa.age)
Ayo.hi()
Alyssa.hi()

#class inheritance allows to define classes that inherit all the methods and properties from another class
#Parent class gives the inheritance
#Child class inherits from the parent

class Teacher(Person): #"Person" is the parent class and "Teacher" is the child
    role = 'teacher'
    
    def hi(self):
        print("Hi my name is Mx. " + self.name)

forlenza = Teacher("Forlenza", 184)
print(forlenza.role)

forlenza.hi()


