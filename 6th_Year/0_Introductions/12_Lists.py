animals: list[str] = ["dorg", "car", "bunny", "parrot", "fsh"]

print(*[dog for dog in animals if len(dog) == 3], sep="\n")

names: list[str] = []

for _ in range(int(input("How many names do you want to add? "))):
    names.append(input("Enter a name: "))

print(names)
