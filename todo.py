print()

while True:
    x = input("What do you want to do? ")

    my_file = open("ayo2.txt", "a")
    
    print()

    my_file.write(x +'\n')

    my_file.close()

    my_file = open("ayo2.txt")

    

    for line in my_file.readlines():
        print(line, end="")

