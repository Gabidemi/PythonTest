my_file = open("ayo.txt", "r+")

#print(my_file.readlines())

for line in my_file.readlines():
    print(line, end="")

my_file.writelines(['Im writing this because i was asked to'])