x = [95, 90, 85, 95, 85]
y = []
sum = 0

while sum >= 0:
    z = int(input("What is your grade?: "))
    y.append(z)
    print(y)
    sum = sum + z
        

    if sum > 500:
        print("end")
        break
print("Youe GPA is: " + str(sum/len(x)))


# sum = 0
# for grade in x:
#     sum = sum + grade

# print(sum/ len(x))