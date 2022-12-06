my_file = open("ayo.txt", "a")

#print(my_file.readlines())

my_file.write('Im writing this because i was asked to\n')

my_file.close()

my_file = open("ayo.txt")

for line in my_file.readlines():
    print(line, end="")


