List = ["Rimuru", "Naofumi", "Raphtalia", "Meliodas", "Monke"]

print(List)

List.append("Tarmiel") #add an item to a list

print(List)

print(List[2]) #picks an item from a list

print(List[-1]) #prints the last item in a list

List[0] = "Light" #Renaming something in a list
print(List)

del List[2] #Deletes an item from a list
print(List)

# Tuple = ("Genshin", "7DS", "ME3", "Duel Links", "Dear Days") #Tuple list

print(len(List)) #prints the length of a list in integers

List.sort() #Descending order from list ( A - Z)
print(List)

List.reverse() #Ascending order from list ( Z - A)
print(List)

List2 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] #2nd list

print(List + List2) #combines 2 lists together

print(" | ".join(List + List2)) #removes the (" ") from your list

print("Anna, Wesley, Saint".split(",")) #converts the string into a list
