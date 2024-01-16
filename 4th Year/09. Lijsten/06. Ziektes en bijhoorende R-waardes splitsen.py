gegeven = ["Griep", 2.1, "Ebola", 2.5, "Covid", 3.9, "Sars", 5, "Pokken", 6,"Bof" , 7, "Mazelen", 18]
Name = []
R = []

for x in gegeven:
    if isinstance(x, str):
        Name.append(x)
    else:
        R.append(x)

print(Name)
print(R)
