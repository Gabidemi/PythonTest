my_file = open("ayo2.txt", "w+")
todolist = []

x = input("What do you want to add to list?")
todolist.append(x)

print(todolist)


while x == x:
    x = input("what else?")

    todolist.append(x)

    print(todolist)

    my_file.write(todolist)

    my_file.close()

    my_file = open("ayo2.txt")

    for line in my_file.readlines():
        print(line, end="")

