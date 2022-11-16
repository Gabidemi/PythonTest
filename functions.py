def hello_world():
    print('hello world')

hello_world()

def Add(a, b): #Adds a and b
    print(a+b)

Add(9, 10)

def Subtract(a, b): #finds the subtraction property of a and b
    print(a - b)

Subtract(10, 7)

def Divide(a, b): #Finds the division of a and b
    print(a // b)

Divide(20, 2)

def Remainder(a, b): #Finds the remainder of the number
    print(a % b)

Remainder(20, 5)

def exponent(a, b): #Finds the exponent of a and b
    print(a ** b)

exponent(2, 3)

def slope(m, x, b): #slope intercept form equation
    return m * x + b 

x = slope(7, 2, 5)
print(x)