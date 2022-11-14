grade = int(input("Input your percentage here: ")) #assigning a variable and turning the input to an integer

if grade > 59 and grade < 73: #Conditions for getting a D
    print("You got a D")
elif grade > 73 and grade < 80: #conditions for getting a C
    print("You got a C")
elif grade > 80 and grade < 90: #Conditions for getting a B
    print("You got a B")
elif grade > 90: #conditions for getting an A
    print("You got an A")
else: #if none of the numbers were inputed, it automatically becomes an F
    print("You got an F")
