grade = int(input("Input your percentage here: "))

if grade > 59 and grade < 73:
    print("You got a D")
elif grade > 73 and grade < 80:
    print("You got a C")
elif grade > 80 and grade < 90:
    print("You got a B")
elif grade > 90:
    print("You got an A")
else:
    print("You got an F")
